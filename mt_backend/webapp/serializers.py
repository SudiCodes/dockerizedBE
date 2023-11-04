from webapp.models import Genre, CastMember, Title
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class CastMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = CastMember
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    casts = CastMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = '__all__'

    def to_representation(self, instance):
        data = super(TitleSerializer, self).to_representation(instance)

        # Extract genre names
        data['genre'] = [genre['name'] for genre in data['genre']]

        # Extract cast member names
        data['casts'] = [
            f"{cast['name']} {cast['surname']}" for cast in data['casts']]

        return data
