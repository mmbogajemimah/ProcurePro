# Generated by Django 4.1.4 on 2023-01-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_alter_bids_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tender",
            name="owner",
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]