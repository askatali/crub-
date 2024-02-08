from django.urls import path
from asmovie.views import MovieDetail, MovieList, MovieCreateView, MovieUpdateView

urlpatterns = [
    path('kino/', MovieList.as_view(), name='kino'),
    path('detail/<int:id>/', MovieDetail.as_view(), name='detail'),
    path('create/', MovieCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='update')
]