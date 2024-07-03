from rest_framework import serializers

class MedalTallySerializer(serializers.Serializer):
    region = serializers.CharField()
    Year = serializers.CharField()
    Gold = serializers.IntegerField()
    Silver = serializers.IntegerField()
    Bronze = serializers.IntegerField()
    Total = serializers.IntegerField()


class MedallTallySerializer(serializers.Serializer):
    year = serializers.CharField()
    country = serializers.CharField()