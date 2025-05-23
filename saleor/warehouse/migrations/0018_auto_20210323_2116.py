# Generated by Django 3.1.7 on 2021-03-23 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0034_remove_checkout_quantity"),
        ("warehouse", "0017_preorderallocation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity_reserved", models.PositiveIntegerField(default=0)),
                ("reserved_until", models.DateTimeField()),
                (
                    "checkout_line",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to="checkout.checkoutline",
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to="warehouse.stock",
                    ),
                ),
            ],
            options={
                "ordering": ("pk",),
            },
        ),
        # nosemgrep: add-index-concurrently
        migrations.AddIndex(
            model_name="reservation",
            index=models.Index(
                fields=["checkout_line", "reserved_until"],
                name="warehouse_r_checkou_b66369_idx",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="reservation",
            unique_together={("checkout_line", "stock")},
        ),
    ]
