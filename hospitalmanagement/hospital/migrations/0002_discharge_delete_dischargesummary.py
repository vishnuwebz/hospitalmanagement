# Generated by Django 5.0.6 on 2024-06-18 21:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discharge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("discharge_date", models.DateField(default=django.utils.timezone.now)),
                ("discharge_reason", models.TextField()),
                ("discharge_note", models.TextField()),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.doctor",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.patient",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="DischargeSummary",
        ),
    ]