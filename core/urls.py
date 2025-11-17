from django.urls import path
from .views import home, our_story, detail

urlpatterns = [
    path('', home, name='home'),
    path('our-story/', our_story, name='our_story'),
    path('detail/', detail, name='detail'),

]
