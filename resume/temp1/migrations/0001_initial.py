# Generated by Django 4.0 on 2021-12-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temp1model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('degree', models.CharField(max_length=100)),
                ('propoint_1', models.CharField(max_length=200)),
                ('propoint_2', models.CharField(max_length=200)),
                ('propoint_3', models.CharField(blank=True, max_length=200)),
                ('propoint_4', models.CharField(blank=True, max_length=200)),
                ('lang_1', models.CharField(max_length=20)),
                ('lang_2', models.CharField(blank=True, max_length=20)),
                ('lang_3', models.CharField(blank=True, max_length=20)),
                ('Address', models.CharField(max_length=200)),
                ('Date_of_birth', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mobileno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('course_1', models.CharField(max_length=50)),
                ('school_1', models.CharField(max_length=200)),
                ('percent_1', models.CharField(max_length=50)),
                ('year_1', models.CharField(max_length=50)),
                ('course_2', models.CharField(max_length=50)),
                ('school_2', models.CharField(max_length=200)),
                ('percent_2', models.CharField(max_length=50)),
                ('year_2', models.CharField(max_length=50)),
                ('course_3', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=200)),
                ('percent_3', models.CharField(max_length=50)),
                ('year_3', models.CharField(max_length=50)),
                ('skill_1', models.CharField(blank=True, max_length=100)),
                ('skill_2', models.CharField(blank=True, max_length=100)),
                ('skill_3', models.CharField(blank=True, max_length=100)),
                ('skill_4', models.CharField(blank=True, max_length=100)),
                ('skill_5', models.CharField(blank=True, max_length=100)),
                ('hobby_1', models.CharField(max_length=100)),
                ('hobby_2', models.CharField(blank=True, max_length=100)),
                ('hobby_3', models.CharField(blank=True, max_length=100)),
                ('intern_1', models.CharField(blank=True, max_length=100)),
                ('intern_2', models.CharField(blank=True, max_length=100)),
                ('declare', models.CharField(max_length=500)),
            ],
        ),
    ]
