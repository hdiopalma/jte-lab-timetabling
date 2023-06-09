# Generated by Django 4.1 on 2023-07-13 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Assistant",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("nim", models.CharField(max_length=12)),
                ("regular_schedule", models.JSONField()),
                ("prefered_schedule", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Laboratory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="Semester",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name="Participant",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("nim", models.CharField(max_length=12)),
                ("regular_schedule", models.JSONField()),
                (
                    "semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.semester",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32)),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                (
                    "laboratory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.laboratory",
                    ),
                ),
                (
                    "semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.semester",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GroupMembership",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.group",
                    ),
                ),
                (
                    "laboratory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.laboratory",
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.module",
                    ),
                ),
                (
                    "participant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.participant",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="group",
            name="module",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="scheduling_data.module"
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="semester",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="scheduling_data.semester",
            ),
        ),
        migrations.CreateModel(
            name="Chapter",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.module",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AssistantMembership",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "assistant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.assistant",
                    ),
                ),
                (
                    "laboratory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.laboratory",
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scheduling_data.module",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="assistant",
            name="laboratory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="scheduling_data.laboratory",
            ),
        ),
        migrations.AddField(
            model_name="assistant",
            name="semester",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="scheduling_data.semester",
            ),
        ),
    ]
