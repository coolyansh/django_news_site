from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('world',views.world,name='world'),
    path('sports',views.sports,name='sports'),
    path('entertainment',views.entertainment,name='entertainment'),
    path('business',views.business,name='business'),
    path('science',views.science,name='science'),
    path('tech',views.tech,name='tech'),
    path('search',views.search,name='search'),
    path('about',views.about,name='about'),
    path('convert',views.convert,name='convert'),
    path('convert/json',views.convert_json,name='convert_json')
]