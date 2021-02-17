# Generated by Django 3.1.6 on 2021-02-08 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='games',
            name='description',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='games',
            name='number_of_players',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
