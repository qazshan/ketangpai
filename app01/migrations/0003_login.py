# Generated by Django 4.2.20 on 2025-05-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_course_user_delete_login_course_teacher"),
    ]

    operations = [
        migrations.CreateModel(
            name="Login",
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
                (
                    "account",
                    models.CharField(max_length=16, unique=True, verbose_name="账号"),
                ),
                ("password", models.CharField(max_length=16)),
                ("serial_number", models.CharField(max_length=16, verbose_name="编号")),
                (
                    "role",
                    models.SmallIntegerField(
                        choices=[(1, "教师"), (2, "学生"), (3, "管理员")],
                        verbose_name="身份",
                    ),
                ),
            ],
        ),
    ]
