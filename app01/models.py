from django.db import models

# Create your models here.
class Login(models.Model):
    #自动生成id
    account = models.CharField(verbose_name="账号", max_length=16, unique=True)
    password = models.CharField(max_length=16)
    serial_number = models.CharField(verbose_name="编号", max_length=16)
    role_choices = (
        (1, "教师"),
        (2,"学生")
    )
    role = models.SmallIntegerField(verbose_name="身份", choices=role_choices)

class User(models.Model):
    # todo 未来修改 注册时account自动生成而非手动输入 使用手机号/邮箱
    account = models.CharField(verbose_name="账号", max_length=16, unique=True, primary_key=True)
    password = models.CharField(max_length=16)
    serial_number = models.CharField(verbose_name="编号", max_length=16,null=True,blank=True)
    role_choices = (
        (1, "教师"),
        (2,"学生")
    )
    role = models.SmallIntegerField(verbose_name="身份", choices=role_choices)
    name = models.CharField(max_length=10)
    avatar = models.ImageField(null=True, blank=True)
    school = models.CharField(max_length=16)
    major = models.CharField(max_length=16, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="课程名称", max_length=16)
    teacher = models.ForeignKey(to="app01.User", to_field="account", on_delete=models.CASCADE)
    status_choices = (
        (1, "进行中"),
        (2,"未开始"),
        (3,"已结课")
    )
    status = models.SmallIntegerField(default=1, choices=status_choices, null=True, blank=True)
    introduction = models.TextField(max_length=1024)
    course_class = models.CharField(max_length=16)
    year_choices = (
        (1, "2026-2027"),
        (2, "2025-2026"),
        (3, "2024-1025"),
        (4, "2023-2024"),
    )
    year = models.SmallIntegerField(choices=year_choices)
    term = models.SmallIntegerField()
    mode_choices = (
        (1, "混合模式"),
        (2, "线上课程"),
        (3, "线下课程"),
        (4, "其他")
    )
    mode = models.SmallIntegerField(choices=mode_choices)
    image = models.ImageField(null=True, blank=True)

class Student_Course(models.Model):
    # 关联 User 模型，当关联的学生记录被删除时，该关联记录也会被删除
    student = models.ForeignKey(to="app01.User", to_field="account",on_delete=models.CASCADE)
    course = models.ForeignKey(to="app01.Course",to_field="id", on_delete=models.CASCADE)

    class Meta:
        # 用于创建一个唯一性约束，确保指定的字段组合在表中是唯一的，但它并不会将这些字段设置为主键。
        unique_together = ('student', 'course')

    def __str__(self):
        return f"Student: {self.student.account},{self.student.name}, Course: {self.course.name}"