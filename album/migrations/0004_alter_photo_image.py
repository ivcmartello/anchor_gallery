# Generated by Django 3.2.5 on 2021-07-16 19:28

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_rename_photo_uuid_like_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='images'),
        ),
    ]
