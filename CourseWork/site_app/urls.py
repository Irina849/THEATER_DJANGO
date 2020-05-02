from django.urls import path
from django.views.generic.list import ListView
from django.views.generic.dates import ArchiveIndexView
from django.views.generic import TemplateView
from .models import Actor, Event, Festival, ActorEvent, Poster
from . import views
from .views import NextE

urlpatterns = [
    path('index/', views.index, name='index'),
    path('actors/', ListView.as_view(template_name="index_actor.html",
                                     model=Actor, context_object_name='actors')),
    path('events/', ListView.as_view(template_name="index_event.html",
                                     model=Poster, context_object_name='posters')),
    path('fests/', ListView.as_view(template_name="index_fest.html",
                                    model=Festival, context_object_name='fests')),
    path('actor_event/', ListView.as_view(template_name="index_actor_event.html",
                                          model=ActorEvent, context_object_name='actor_event')),
    path('past_events/', ArchiveIndexView.as_view(template_name='past_events.html',
                                                  model=Poster, date_field='performace_date', context_object_name='pastEvents')),
    path('next_events/', NextE.as_view(template_name='next_events.html',
                                       model=Poster, context_object_name='nextEvents')),
    path('home/', TemplateView.as_view(template_name='home.html')),



]
