# Generated by Django 4.2.1 on 2023-05-07 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_app', '0002_alter_friendship_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date created'),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='member_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_1', to=settings.AUTH_USER_MODEL, verbose_name='Member 1'),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='member_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_2', to=settings.AUTH_USER_MODEL, verbose_name='Member 2'),
        ),
        migrations.AlterField(
            model_name='friendshiprequest',
            name='is_received',
            field=models.BooleanField(default=False, verbose_name='Is received'),
        ),
        migrations.AlterField(
            model_name='friendshiprequest',
            name='request_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='Request from'),
        ),
        migrations.AlterField(
            model_name='friendshiprequest',
            name='request_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='Request to'),
        ),
    ]
