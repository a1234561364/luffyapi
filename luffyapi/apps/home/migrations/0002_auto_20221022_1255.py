# Generated by Django 2.2.2 on 2022-10-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(default=True, help_text='图片尺寸必须是:3840x800', upload_to='banner', verbose_name='轮播图'),
        ),
    ]
