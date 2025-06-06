# Generated by Django 4.2.20 on 2025-05-06 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=16, verbose_name="课程名称")),
                (
                    "status",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[(1, "进行中"), (2, "未开始"), (3, "已结课")],
                        default=1,
                        null=True,
                    ),
                ),
                ("introduction", models.TextField(max_length=1024)),
                ("course_class", models.CharField(max_length=16)),
                (
                    "year",
                    models.SmallIntegerField(
                        choices=[
                            (1, "2026-2027"),
                            (2, "2025-2026"),
                            (3, "2024-1025"),
                            (4, "2023-2024"),
                        ]
                    ),
                ),
                ("term", models.SmallIntegerField()),
                (
                    "mode",
                    models.SmallIntegerField(
                        choices=[
                            (1, "混合模式"),
                            (2, "线上课程"),
                            (3, "线下课程"),
                            (4, "其他"),
                        ]
                    ),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "account",
                    models.CharField(
                        max_length=16,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="账号",
                    ),
                ),
                ("password", models.CharField(max_length=16)),
                (
                    "serial_number",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="编号"
                    ),
                ),
                (
                    "role",
                    models.SmallIntegerField(
                        choices=[(1, "教师"), (2, "学生")], verbose_name="身份"
                    ),
                ),
                ("name", models.CharField(max_length=10)),
                ("avatar", models.ImageField(blank=True, null=True, upload_to="")),
                ("school", models.CharField(max_length=16)),
                ("major", models.CharField(blank=True, max_length=16, null=True)),
                ("phone", models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Login",
        ),
        migrations.AddField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app01.user"
            ),
        ),
    ]
