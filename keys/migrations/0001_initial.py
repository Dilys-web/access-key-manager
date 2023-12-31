# Generated by Django 4.2.2 on 2023-06-23 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import keys.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('expired', 'Expired'), ('revoked', 'Revoked')], default='active', max_length=20)),
                ('procurement_date', models.DateTimeField(auto_now_add=True)),
                ('expiry_date', models.DateTimeField(default=keys.models.get_default_expiry_date)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-procurement_date'],
            },
        ),
    ]
