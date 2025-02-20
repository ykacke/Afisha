from django.urls import path
from .import views

urlpatterns = [

    path('directors/', views.director_list_view,),
    path('directors/<int:id>/', views.director_detail_view,),

    path('movies/', views.movie_list_view,),
    path('movies/<int:id>/', views.movie_detail_view,),

    path('review/', views.review_list_view,),
    path('review/<int:id>/', views.review_detail_view,),

]   