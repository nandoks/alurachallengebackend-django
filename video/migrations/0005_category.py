# Generated by Django 3.2.5 on 2021-07-26 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20210721_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=7)),
                ('video', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='video.video')),
            ],
        ),
    ]
