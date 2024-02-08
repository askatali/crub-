from django.urls import path
from next.views import EmailCreateView


urlpatterns = [

    path('create/', EmailCreateView.as_view(), name='create')




]