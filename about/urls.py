from django.urls import include, path

from . import views

app_name = 'about'

me_patterns = [
    path('biography/', views.me_biography, name='biography'),
    path('facts/', views.me_facts, name='facts'),
]

city_patterns = [
    path('info/', views.city_info, name='info'),
    path('places/', views.city_places, name='places'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('me/', include((me_patterns, 'me'))),
    path('city/', include((city_patterns, 'city'))),
]
