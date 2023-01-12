# Generated by Django 4.1.4 on 2023-01-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_alter_bids_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tender",
            name="category",
            field=models.CharField(
                choices=[
                    ("Advertising", "Advertising"),
                    ("Agriculture", "Agriculture"),
                    ("Chemicals", "Chemicals"),
                    ("Construction", "Construction"),
                    ("Economics", "Economics"),
                    ("Education", "Education"),
                    ("Energy", "Energy"),
                    ("Engineering", "Engineering"),
                    ("Finance", "Finance"),
                    ("Food", "Food"),
                    ("Forestry", "Forestry"),
                    ("Goods", "Goods"),
                    ("Healthcare", "Healthcare"),
                    ("Infrastructure", "Infrastructure"),
                    ("Manufacturing", "Manufacturing"),
                    ("Market Research", "Market Research"),
                    ("Mining", "Mining"),
                    ("Pharmaceuticals", "Pharmaceuticals"),
                    ("Production", "Production"),
                    ("Real Estate", "Real Estate"),
                    ("Research", "Research"),
                    ("Retail", "Retail"),
                    ("Telecommunications", "Telecommunications"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]