# Generated by Django 4.2 on 2023-05-17 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0002_account_created_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="level",
        ),
        migrations.RemoveField(
            model_name="account",
            name="lft",
        ),
        migrations.RemoveField(
            model_name="account",
            name="rght",
        ),
        migrations.RemoveField(
            model_name="account",
            name="tree_id",
        ),
        migrations.AlterField(
            model_name="account",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="accounts_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="industry",
            field=models.ManyToManyField(
                blank=True, related_name="accounts", to="accounts.industry"
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="users",
            field=models.ManyToManyField(
                blank=True, related_name="account", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]