# Generated by Django 3.0.1 on 2020-12-09 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ELearningApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_name', models.CharField(max_length=128)),
                ('TID', models.CharField(default='19MCA1027', max_length=128)),
                ('Teacher_permanent_address', models.TextField(max_length=500)),
                ('Teacher_residential_address', models.TextField(max_length=500)),
                ('Secondary_examination', models.CharField(choices=[('1', 'WBBSE'), ('2', 'BBSE'), ('3', 'DBSE')], max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='organization',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]