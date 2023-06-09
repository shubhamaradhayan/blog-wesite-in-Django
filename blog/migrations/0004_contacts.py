# Generated by Django 4.2.1 on 2023-05-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('msg', models.TextField(max_length=300)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
