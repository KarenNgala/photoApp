# Generated by Django 3.1 on 2020-08-13 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_insta', '0007_auto_20200813_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='related_post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_insta.image'),
            preserve_default=False,
        ),
    ]