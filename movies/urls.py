from django.urls import path
from movies import views

urlpatterns=[
	path('movies/',views.MovieList.as_view()),
	path('movies/<int:pk>/',views.MovieDetail.as_view()),
	path('movies-by-user/',views.MoviesByUser.as_view()),
	path('users/', views.UserCreate.as_view()),
]