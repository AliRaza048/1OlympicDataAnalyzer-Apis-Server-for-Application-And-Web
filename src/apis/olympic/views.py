# olympics/views.py
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import os

from .bll import helper
from .bll.preprocessor import dataset
from .serializers import MedalTallySerializer, MedallTallySerializer

df = dataset()


class MedalTallyPagination(PageNumberPagination):
    page_size = 50  # Number of records per page
    page_size_query_param = 'page_size'
    max_page_size = 100


class MedalTallyView(APIView):
    def get(self, request, format=None):
        # Load CSV data from file
        file_path = os.path.join(os.path.dirname(__file__), 'dataset.csv')
        data = pd.read_csv(file_path)

        year = request.query_params.get('year', 'Overall')
        country = request.query_params.get('country', 'Overall')

        # Filter data based on year and country
        if year != 'Overall':
            data = data[data['Year'] == int(year)]
        if country != 'Overall':
            data = data[data['region'] == country]

        # Calculate Total medals for each item
        data['Total'] = data['Gold'].astype(int) + data['Silver'].astype(int) + data['Bronze'].astype(int)

        # Convert DataFrame to dictionary
        data = data.to_dict(orient='records')

        paginator = MedalTallyPagination()
        paginated_data = paginator.paginate_queryset(data, request)
        serializer = MedalTallySerializer(paginated_data, many=True)

        return paginator.get_paginated_response(serializer.data)

class UniqueYearsCountriesAndSportsView(APIView):

    def get(self, request, format=None):
        # Load CSV data from file
        data = {'Year': pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int),
                'region': df['region'].astype(str),'Sport':df['Sport'].astype(str)}
        years = sorted(data['Year'].unique().tolist())
        countries = sorted(data['region'].unique().tolist())
        sports = sorted(data['Sport'].unique().tolist())


        return Response({
            'years': years,
            'countries': countries,
            'sports':sports
        }, status=status.HTTP_200_OK)




class MedallTallyView(APIView):
    def get(self,request,year,country):
        # years = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)
        # regions = df['region'].astype(str)
        medal_tally = helper.fetch_medal_tally(df,year,country)

        return Response(medal_tally)


class AnalysisOverYearView(APIView):

    def get(self,request,analyser):

        nations_over_time = helper.data_over_time(df, analyser)
        return Response(nations_over_time)




class HeatMapNoEventsView(APIView):
    def get(self,request):
        pt = helper.overall_event_heatmap(df)
        return Response({'heatmap': pt.to_dict()})


class SuccessFullAthletsView(APIView):
    def get(self,request,selected_sport):

        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()

        x = helper.most_successful(df, selected_sport)


        return Response(x)



class CountrywiseAnalysis(APIView):
    def get(self,request,selected_country):
        country_list = df['region'].dropna().unique().tolist()
        country_list.sort()

        country_df = helper.yearwise_medal_tally(df, selected_country)
        pt = helper.country_event_heatmap(df, selected_country)
        top10_df = helper.most_successful_countrywise(df, selected_country)

        return Response({'countries':country_list,'country_analyse':country_df,'heatmap':pt,'top10':top10_df})



class AthletsWiseAnalysis(APIView):
    def get(self,request,):
        athlete_df = df.drop_duplicates(subset=['Name', 'region'])
        x1 = athlete_df['Age'].dropna()
        x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
        x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
        x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
        return Response({'x1':x1,'x2':x2,'x3':x3,'x4':x4})


class FamousSportsAnalysis(APIView):
    def get(self,request):
        x = []
        name = []
        famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                         'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                         'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                         'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                         'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                         'Tennis', 'Golf', 'Softball', 'Archery',
                         'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                         'Rhythmic Gymnastics', 'Rugby Sevens',
                         'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
        for sport in famous_sports:
            athlete_df = df.drop_duplicates(subset=['Name', 'region'])

            temp_df = athlete_df[athlete_df['Sport'] == sport]
            x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
            name.append(sport)

        return Response({'x':x,'name':name})


class HeightVsWeight(APIView):

    def get(self, request, selected_sport):
        temp_df = helper.weight_v_height(df, selected_sport)
        data = temp_df.to_dict(orient='records')
        return Response(data)


class MenVsWomen(APIView):
    def get(self, request):
        final = helper.men_vs_women(df)
        data = final.to_dict(orient='records')
        return Response(data)
















