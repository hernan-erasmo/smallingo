# Generated by Django 5.0.3 on 2024-03-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallingovideo',
            name='audio_fragment',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='smallingovideo',
            name='audio_fragment_speech',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='smallingovideo',
            name='audio_fragment_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smallingovideo',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smallingovideo',
            name='pixels_tall',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smallingovideo',
            name='video_ocr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smallingovideo',
            name='video_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
