# Generated by Django 4.0.3 on 2022-03-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arikeapp', '0016_alter_disease_deleted_alter_district_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family_detail',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Non-binary')]),
        ),
    ]
