# Generated by Django 4.2.1 on 2023-05-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.FileField(upload_to='uploads'),
        ),
    ]
