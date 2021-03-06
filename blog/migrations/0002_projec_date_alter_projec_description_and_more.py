# Generated by Django 4.0.1 on 2022-02-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projec',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='projec',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='projec',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/images/'),
        ),
    ]
