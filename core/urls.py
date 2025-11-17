from django.urls import path
from .views import home, our_story

urlpatterns = [
    path('', home, name='home'),
    path('our-story/', our_story, name='our_story'),

]
