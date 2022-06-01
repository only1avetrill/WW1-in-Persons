# Generated by Django 4.0.4 on 2022-06-01 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0022_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=1000, verbose_name='Текст')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_comment', to='main.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Комментарий новости',
                'verbose_name_plural': 'Комментарии новости',
            },
        ),
    ]
