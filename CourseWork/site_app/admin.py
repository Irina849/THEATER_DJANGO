from django.contrib import admin
from .models import Actor, Event, Place, Role, Poster, ActorEvent, Festival, City, Street, Gender

admin.site.register(Actor)
admin.site.register(Gender)
admin.site.register(Role)
admin.site.register(Event)
admin.site.register(Poster)
admin.site.register(ActorEvent)
admin.site.register(Festival)
admin.site.register(Place)
admin.site.register(City)
admin.site.register(Street)
