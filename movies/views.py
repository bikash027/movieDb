from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from movies.permissions import IsCreatorOrReadOnly
from movies.models import Movie
from movies.serializers import MovieSerializer, UserSerializer
from django.contrib.auth.models import User

class MovieList(generics.ListCreateAPIView):
	permission_classes= [permissions.IsAuthenticatedOrReadOnly]
	queryset= Movie.objects.all()
	serializer_class=MovieSerializer
	def get(self, request, *args, **kwargs):
		search=request.GET.get('search','')
		self.queryset=self.queryset.filter(name__icontains=search)

		sort_by=request.GET.get('sort-by')
		if sort_by=='name':
			self.queryset=self.queryset.order_by('name')

		elif sort_by=='date':
			self.queryset=self.queryset.order_by('date')

		return super().get(request, args, kwargs)

	def perform_create(self, serializer):
		serializer.save(creator= self.request.user)

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes= [permissions.IsAuthenticatedOrReadOnly,
						 IsCreatorOrReadOnly]
	queryset= Movie.objects.all()
	serializer_class=MovieSerializer

class UserCreate(generics.ListCreateAPIView):
	queryset= User.objects.all()
	serializer_class= UserSerializer

class MoviesByUser(generics.ListAPIView):
	queryset=Movie.objects.all()
	serializer_class= MovieSerializer
	def get(self, request, *args, **kwargs):
		user_id= request.GET.get('user-id','')
		username= request.GET.get('username','')
		if user_id !='':
			self.queryset=self.queryset.filter(creator_id=user_id)
		elif username!='':
			try:
				user= User.objects.get(username=username)
				self.queryset=self.queryset.filter(creator_id=user.id)
			except:
				self.queryset=Movie.objects.none()
		return super().get(request, args, kwargs)
