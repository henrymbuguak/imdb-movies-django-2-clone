from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('movies', views.MovieList.as_view(), name='movie_list'),
    path('top/ten/movies', views.TopMovies.as_view(), name='top_ten_movie'),
    path('movie/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),
    path('movie/vote/<int:movie_id>/create', views.CreateVote.as_view(), name='create_vote'),
    path('movie/vote/<int:movie_id>/update/<int:pk>', views.UpdateVote.as_view(), name='update_vote'),
    path('movie/<int:movie_id>/upload/image', views.MovieImageUpload.as_view(), name='movie_image_upload')
]

