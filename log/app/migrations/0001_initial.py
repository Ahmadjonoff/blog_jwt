# Generated by Django 4.0.4 on 2022-04-13 08:18

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
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('yosh', models.PositiveIntegerField()),
                ('kasb', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Talks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=30)),
                ('video', models.URLField()),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.muallif')),
            ],
        ),
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=30)),
                ('matn', models.TextField()),
                ('rasm', models.URLField()),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.muallif')),
            ],
        ),
    ]
