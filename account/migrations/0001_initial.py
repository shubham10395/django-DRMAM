# Generated by Django 2.0.13 on 2019-04-22 15:01

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
            name='classinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField(default=1)),
                ('projector', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='labinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_incharge', models.CharField(max_length=50)),
                ('no_of_pc', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('starage', models.IntegerField()),
                ('name_of_os', models.CharField(max_length=50)),
                ('account_labinfo_id', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='classinfo',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.labinfo'),
        ),
    ]
