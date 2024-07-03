from django.urls import path

from src.apis.olympic.views import( MedalTallyView, UniqueYearsCountriesAndSportsView, MedallTallyView

                                ,AnalysisOverYearView,AthletsWiseAnalysis
                                    ,HeatMapNoEventsView,SuccessFullAthletsView,
                                    CountrywiseAnalysis
                                    ,
                                    FamousSportsAnalysis,
                                    HeightVsWeight,
                                    MenVsWomen)

app_name = 'olympic'

urlpatterns = [
    path('medal_tally/', MedalTallyView.as_view(), name='medal_tally'),
    path('unique_years_countries_sports/', UniqueYearsCountriesAndSportsView.as_view(), name='unique_years_countries_sports'),
    path('medaltally/<str:year>/<str:country>', MedallTallyView.as_view(), name='medaltally'),
    path('analyse_year/<str:analyser>', AnalysisOverYearView.as_view(), name='analyse_year'),
    path('heatmap_noevents/', HeatMapNoEventsView.as_view(), name='heatmap_noevents'),
    path('successful_athlets/<str:selected_sport>', SuccessFullAthletsView.as_view(), name='successful_athlets'),
    path('countrywise_analysis/<str:selected_country>', CountrywiseAnalysis.as_view(), name='countrywise_analysis'),
   # COUNTRY WISE

]

urlpatterns +=[
    path('athletswise_analysis/', AthletsWiseAnalysis.as_view(), name='athletswise_analysis'),
    path('famous_sport/', FamousSportsAnalysis.as_view(), name='famous_sport'),
    path('height_weight/<str:selected_sport>', HeightVsWeight.as_view(), name='height_weight'),

    path('men_women/', MenVsWomen.as_view(), name='height_weight'),

]

