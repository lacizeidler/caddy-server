# Generated by Django 4.0.3 on 2022-03-10 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GolfCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Golfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HoleByHole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('share', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.golfcourse')),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.golfer')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.golfer')),
            ],
        ),
        migrations.CreateModel(
            name='NumOfHoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('content', models.CharField(max_length=200)),
                ('image_url', models.ImageField(upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.golfcourse')),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.golfer')),
                ('likes', models.ManyToManyField(related_name='likes', through='caddyhackapi.Like', to='caddyhackapi.golfer')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.post'),
        ),
        migrations.CreateModel(
            name='IndividualHole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('par', models.IntegerField()),
                ('score', models.IntegerField()),
                ('hole_num', models.IntegerField()),
                ('hole_by_hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.holebyhole')),
            ],
        ),
        migrations.AddField(
            model_name='holebyhole',
            name='num_of_holes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.numofholes'),
        ),
        migrations.CreateModel(
            name='FinalScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('score', models.IntegerField()),
                ('share', models.BooleanField()),
                ('par', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.golfcourse')),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.golfer')),
                ('num_of_holes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.numofholes')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.golfer')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddyhackapi.post')),
            ],
        ),
    ]
