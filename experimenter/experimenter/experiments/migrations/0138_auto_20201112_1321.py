# Generated by Django 3.1.3 on 2020-11-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0137_auto_20201110_1809"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nimbusexperiment",
            name="targeting_config_slug",
            field=models.CharField(
                blank=True,
                choices=[
                    ("all_english", "All English"),
                    ("us_only", "Us Only"),
                    ("first_run", "Targeting First Run"),
                    ("first_run_chrome", "Targeting First Run Chrome Attribution"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]