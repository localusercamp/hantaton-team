# Generated by Django 2.2.6 on 2019-11-23 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount_of_allowed_projects', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('third_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uber.Company')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('master', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uber.Mentor')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uber.University')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uber.Project')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uber.University')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('third_name', models.CharField(blank=True, max_length=50, null=True)),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='uber.University')),
                ('work_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uber.WorkGroup')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uber.University'),
        ),
    ]
