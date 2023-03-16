# Generated by Django 3.2.16 on 2023-03-16 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import food_app.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planperiod',
            options={'verbose_name': 'Срок подписки', 'verbose_name_plural': 'Сроки подписок'},
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to=food_app.models.get_uploading_path, verbose_name='Аватар')),
                ('subscribe', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='subscribes', to='food_app.subscription', verbose_name='Подписка')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
