# Generated by Django 2.2.6 on 2019-11-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0005_auto_20191123_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='login',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='login',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.AddField(
            model_name='mentor',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]