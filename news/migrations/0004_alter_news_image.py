# Generated by Django 4.2.3 on 2024-10-17 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="image",
            field=models.ImageField(null=True, upload_to="img/"),
        ),
    ]
