# Generated by Django 3.0.5 on 2020-04-27 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('birth_date', models.DateTimeField(verbose_name='birth_date')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_event', models.CharField(max_length=128)),
                ('director', models.CharField(max_length=128)),
                ('comment_about_event', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=64)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.City')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=128)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performace_date', models.DateTimeField(verbose_name='perform date')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=8)),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.Street')),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_fest', models.CharField(max_length=128)),
                ('festival_date', models.DateTimeField(verbose_name='fest date')),
                ('fest_events', models.ManyToManyField(blank='True', to='site_app.Event')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.Place')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_festivals',
            field=models.ManyToManyField(blank='True', to='site_app.Festival'),
        ),
        migrations.CreateModel(
            name='ActorEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=512)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.Actor')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.Role')),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.Gender'),
        ),
    ]