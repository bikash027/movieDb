from rest_framework import serializers
from movies.models import Movie
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
	creator= serializers.ReadOnlyField(source='creator.username')
	class Meta:
		model= Movie
		fields=['id', 'name', 'date', 'genre', 'rating', 'creator']

class UserSerializer(serializers.ModelSerializer):
	movies = serializers.StringRelatedField(many=True,read_only=True)
	password= serializers.CharField(write_only=True)
	class Meta:
		model= User
		fields= ['id','username','password','movies']
	def create(self, validated_data):
		user= User.objects.create(username=validated_data.get('username'))
		user.set_password(validated_data.get('password'))
		user.save()
		return user	