from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.city_name}'


class Street(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    street_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.city.city_name}, {self.street_name}'


class Place(models.Model):
    street = models.ForeignKey(Street, on_delete=models.PROTECT)
    number = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.street.city.city_name}, {self.street.street_name} {self.number}'


class Festival(models.Model):
    title_fest = models.CharField(max_length=128)
    festival_date = models.DateTimeField('fest date')
    place = models.ForeignKey(Place, on_delete=models.PROTECT)
    fest_events = models.ManyToManyField('Event', blank="True")

    def __str__(self):
        return f'{self.title_fest} {self.festival_date} {self.place} '


class Gender(models.Model):
    gender = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.gender}'


class Actor(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    birth_date = models.DateTimeField('birth_date')
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Event(models.Model):
    title_event = models.CharField(max_length=128)
    director = models.CharField(max_length=128)
    comment_about_event = models.CharField(max_length=512)

    event_festivals = models.ManyToManyField(
        'Festival', through=Festival.fest_events.through, blank="True")

    def __str__(self):
        return f'{self.title_event}'


class Poster(models.Model):
    performace_date = models.DateTimeField('perform date')
    event = models.ForeignKey(Event, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.performace_date}'


class Role(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    role = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.role}'


class ActorEvent(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    actor = models.ForeignKey(Actor, on_delete=models.PROTECT)
    notes = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.event} {self.actor} {self.notes}'


# class EventFestival(models.Model):
#     festival = models.ForeignKey(Festival, on_delete=models.PROTECT)
#     event = models.ForeignKey(Event, on_delete=models.PROTECT)
