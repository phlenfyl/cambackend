from django.urls import path

from .views import *

app_name ='sermon'


urlpatterns = [
    path('authorcl/', AuthorListAndCreateView.as_view(), name= 'authorcl'),
    path('sermoncl/', SermonListAndCreateView.as_view(), name= 'sermoncl'),
    path('rud/<str:slug>/', SermonRUDView.as_view(), name= 'rud'),
]