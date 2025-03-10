# Generated by Django 5.1.5 on 2025-02-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('user_name', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Текст обращения')),
                ('contact_method', models.CharField(choices=[('call', 'Перезвонить'), ('whatsapp', 'Написать в WhatsApp')], max_length=20, verbose_name='Способ обращения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
    ]
