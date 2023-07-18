# Generated by Django 4.1 on 2023-07-14 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("scheduling_data", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="module",
            old_name="end",
            new_name="end_date",
        ),
        migrations.RenameField(
            model_name="module",
            old_name="start",
            new_name="start_date",
        ),
        migrations.RemoveField(
            model_name="assistantmembership",
            name="laboratory",
        ),
        migrations.RemoveField(
            model_name="group",
            name="semester",
        ),
        migrations.RemoveField(
            model_name="groupmembership",
            name="laboratory",
        ),
        migrations.RemoveField(
            model_name="groupmembership",
            name="module",
        ),
        migrations.AlterField(
            model_name="assistantmembership",
            name="assistant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assistant_memberships",
                to="scheduling_data.assistant",
            ),
        ),
        migrations.AlterField(
            model_name="assistantmembership",
            name="module",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assistant_memberships",
                to="scheduling_data.module",
            ),
        ),
        migrations.AlterField(
            model_name="groupmembership",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group_memberships",
                to="scheduling_data.group",
            ),
        ),
        migrations.AlterField(
            model_name="groupmembership",
            name="participant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group_memberships",
                to="scheduling_data.participant",
            ),
        ),
    ]