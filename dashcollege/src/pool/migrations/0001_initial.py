# Generated by Django 2.0.4 on 2018-10-06 02:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoolCab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='Owner')),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('start', models.CharField(default='IIITD', max_length=200, verbose_name='Start')),
                ('end', models.CharField(default='IIITD', max_length=200, verbose_name='End')),
                ('waittime', models.DurationField(blank=True, null=True, verbose_name='Wait time')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Object picture')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('avaiable', models.BooleanField(default=True, verbose_name='Available')),
            ],
            options={
                'db_table': 'pool_cab',
            },
        ),
        migrations.CreateModel(
            name='PoolFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='Order by')),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('what', models.CharField(max_length=200, verbose_name='What')),
                ('when', models.CharField(max_length=200, verbose_name='Wait time')),
                ('waittime', models.DurationField(verbose_name='Wait time')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Object picture')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('avaiable', models.BooleanField(default=True, verbose_name='Available')),
            ],
            options={
                'db_table': 'pool_food',
            },
        ),
        migrations.CreateModel(
            name='PoolResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='Owner')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Object picture')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('avaiable', models.BooleanField(default=True, verbose_name='Available')),
            ],
            options={
                'db_table': 'pool_resource',
            },
        ),
        migrations.CreateModel(
            name='StoreResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='Owner')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('price', models.BigIntegerField(verbose_name='Price')),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Object picture')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('avaiable', models.BooleanField(default=True, verbose_name='Available')),
            ],
            options={
                'db_table': 'pool_store',
            },
        ),
    ]