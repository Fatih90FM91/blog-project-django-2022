# Generated by Django 3.2.12 on 2022-03-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]