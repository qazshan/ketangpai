# Create your views here.
import os
from django.utils.dateparse import parse_datetime
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404, JsonResponse
from django.conf import settings
from django import template
from django.db.models import Count

from django.shortcuts import render,redirect,HttpResponse
from app01 import models

# register = template.Library()

def login(request):
    error = None
    if request.method == "POST":
        account = request.POST.get('account')
        password = request.POST.get('password')
        if not account or not password:
            error = "账号和密码不能为空"
        else:
            user = models.User.objects.filter(account=account).first()
            if not user:
                error = "账号不存在"
            elif user.password != password:
                error = "密码错误"
            else:
                if user.role == 1:
                    return redirect('teacher_main', user_account=user.account)
                else:
                    return redirect('student_main', user_account=user.account)
    return render(request, 'login.html', {'error': error})

def register(request):
    if request.method == "POST":
        #todo 优化：两次密码不一致的情况
        account = request.POST.get('account')
        password = ""
        if request.POST.get('password2') == request.POST.get('password1'):
            password = request.POST.get('password1')
        name = request.POST.get('name')
        school = request.POST.get('school')
        role = request.POST.get('role')
        models.User.objects.create(account=account,password=password,name=name,school=school,role=role)
        #todo JS实现弹窗提示注册成功 不然注册之后直接跳转到登录太突兀了
        return redirect('login')
    return render(request,'register.html')

def student_main(request,user_account):
    user = models.User.objects.get(account=user_account)
    objects = models.Student_Course.objects.filter(student_id=user_account)
    courses = []
    for obj in objects:
        row_course = models.Course.objects.filter(id=obj.course_id).first()
        courses.append(row_course)
    if request.method == "POST":
        if 'search' in request.POST:
            keyword = request.POST.get('keyword')
            # todo 搜索没有返回的处理
            if keyword:
                # 使用 icontains 进行不区分大小写的模糊搜索
                courses = models.Course.objects.filter(name__icontains=keyword)

        if 'add' in request.POST:
            course_id = request.POST.get('course_id')
            models.Student_Course.objects.create(student_id=user_account,course_id=course_id)
            return redirect('student_main',user_account = user_account)

    # 实现统计人数
    # courses = models.Course.objects.filter(
    #     # 筛选该用户选的课程 双下划线实现跨表查找
    #     student_course__student_id=user_account
    # ).annotate(
    #     student_count=Count('student_course')  # 统计每门课程的选课人数
    # )
    return render(request,'studentmain.html',{'user':user,'courses':courses})

def teacher_main(request, user_account):    #todo 此处传递的是user_account
    user = models.User.objects.get(account=user_account)
    print('测试一下', user)
    if request.method == "POST":
        return redirect('create_course',user_account = user_account)
    courses = models.Course.objects.filter(teacher_id=user_account)
    for course in courses:
        print(course.name)
    return render(request, 'teachermain.html',{'user':user,'courses':courses})

def create_course(request,user_account):
    if request.method == "POST":
        teacher = models.User.objects.get(account=user_account)
        name = request.POST.get('name')
        course_class = request.POST.get('course_class')
        year = request.POST.get('year')
        term = request.POST.get('term')
        mode = request.POST.get('mode')
        introduction = request.POST.get('introduction')
        models.Course.objects.create(name=name, teacher=teacher, course_class=course_class, year=year, term=term, mode=mode, introduction=introduction)
        return redirect('teacher_main',user_account = user_account)
    return render(request, 'create_course.html')
# def create_course(request, user_account):
#     error_msg = None
#     if request.method == "POST":
#         try:
#             # 获取并验证数据
#             teacher = models.User.objects.get(account=user_account)
#             name = request.POST.get('name')
#             course_class = request.POST.get('course_class')
#             year = request.POST.get('year')
#             term = request.POST.get('term')
#             mode = request.POST.get('mode')
#             introduction = request.POST.get('introduction')
#             print(teacher, name, course_class, year, term, mode, introduction)
#             # 基础验证
#             if not all([name, course_class, year, term,mode]):
#                 error_msg = "请填写所有必填字段"
#                 raise ValueError(error_msg)
#             # 创建课程
#             models.Course.objects.create(
#                 name=name,
#                 teacher=teacher,
#                 course_class=course_class,
#                 year=year,
#                 term=term,
#                 mode=mode,
#                 introduction=introduction
#             )
#             return redirect('teacher_main', user_account=user_account)
#         except Exception as e:
#             if not error_msg:
#                 error_msg = f"创建课程失败: {str(e)}"
#     return render(request, 'create_course.html', {'error': error_msg})
# def create_course(request, user_account):
#     error_msg = None
#     if request.method == "POST":
#         try:
#             # 获取数据并去除空白
#             teacher = models.User.objects.get(account=user_account)
#             name = request.POST.get('name', '').strip()
#             course_class = request.POST.get('course_class', '').strip()
#             year = request.POST.get('year', '')
#             term = request.POST.get('term', '')
#             mode = request.POST.get('mode', '')
#             introduction = request.POST.get('introduction', '').strip()
#
#             # ==== 新增验证逻辑 ====
#             # 1. 检查必填字段
#             required_fields = {
#                 '课程名称': name,
#                 '教学班级': course_class,
#                 '学年': year,
#                 '学期': term,
#                 '教学模式': mode
#             }
#
#             missing_fields = [k for k, v in required_fields.items() if not v]
#             if missing_fields:
#                 error_msg = f"请填写以下必填字段：{', '.join(missing_fields)}"
#                 raise ValueError(error_msg)
#
#             # 2. 类型转换验证
#             try:
#                 year = int(year)
#                 term = int(term)
#                 mode = int(mode)
#             except ValueError:
#                 error_msg = "选项值必须为数字"
#                 raise
#
#             # 3. 选项范围验证
#             valid_year_choices = {choice[0] for choice in models.Course.year_choices}
#             if year not in valid_year_choices:
#                 error_msg = f"无效的学年选择，有效值为：{', '.join(map(str, valid_year_choices))}"
#                 raise ValueError(error_msg)
#
#             if term not in {1, 2, 3}:
#                 error_msg = "学期必须为1、2或3"
#                 raise ValueError(error_msg)
#
#             valid_mode_choices = {choice[0] for choice in models.Course.mode_choices}
#             if mode not in valid_mode_choices:
#                 error_msg = f"无效的教学模式，有效值为：{', '.join(map(str, valid_mode_choices))}"
#                 raise ValueError(error_msg)
#
#             # ==== 创建课程 ====
#             models.Course.objects.create(
#                 name=name,
#                 teacher=teacher,
#                 course_class=course_class,
#                 year=year,
#                 term=term,
#                 mode=mode,
#                 introduction=introduction
#             )
#
#             # 记录成功日志
#             print(f"[SUCCESS] 课程创建成功：{name}")
#             return redirect('teacher_main', user_account=user_account)
#
#         except Exception as e:
#             # 错误处理
#             if not error_msg:
#                 error_msg = f"系统错误：{str(e)}"
#             print(f"[ERROR] 课程创建失败：{error_msg}")
#
#     return render(request, 'create_course.html', {'error': error_msg})

#根据用户身份的不同在统一界面渲染不同的东西 or 直接两个课程内容的界面 倾向后者
def course_detail_student(request,course_id,user_account):
    user = models.User.objects.get(account=user_account)
    chapters = models.Chapter.objects.filter(course_id=course_id)
    assignments = models.Assignment.objects.filter(course_id=course_id)
    students = models.Student_Course.objects.filter(course_id=course_id)
    return render(request, 'course_detail_student.html', {"user":user,'course':models.Course.objects.filter(id=course_id).first(),'chapters':chapters,'assignments':assignments,"students":students})

def course_detail_teacher(request,course_id,user_account):
    user = models.User.objects.get(account=user_account)
    if request.method == "POST":
        print("post方法")
        if 'form1' in request.POST:
            title = request.POST.get('chapter_name')
            content = request.POST.get('content')
            models.Chapter.objects.create(title=title, content=content, course_id=course_id)
        if "form2" in request.POST:
            print("form2的提交")
            title = request.POST.get('title')
            description = request.POST.get('description')
            file = request.FILES.get('filepath')
            type = request.POST.get('inlineRadioOptions')
            due_date_str = request.POST.get('due-date')
            due_date = parse_datetime(due_date_str)
            db_file_path = os.path.join("static", "assignment", file.name)
            file_path = os.path.join("app01", db_file_path)
            f = open(file_path, mode='wb')
            for chunk in file.chunks():
                f.write(chunk)
            f.close()
            print(file_path,title,type,due_date)
            models.Assignment.objects.create(course_id=course_id,title=title, filepath=db_file_path, description=description, type=type, due_date=due_date)
    chapters = models.Chapter.objects.filter(course_id=course_id)
    assignments = models.Assignment.objects.filter(course_id=course_id)
    students = models.Student_Course.objects.filter(course_id=course_id)
    # todo 能不能实现添加作业之后render到作业的页面
    return render(request, 'course_detail_teacher.html', {'user': user,'course':models.Course.objects.filter(id=course_id).first(),'chapters':chapters,'assignments':assignments,"students":students})

def submission_judge(request,user_account,assignment_id):
    try:
        # 尝试获取数据
        models.Submission.objects.get(student_id=user_account,assignment_id=assignment_id)
        return True
    except models.Submission.DoesNotExist:
        return False
def assignment_detail_student(request,assignment_id,user_account):
    user = models.User.objects.get(account=user_account)
    assignment = get_object_or_404(models.Assignment, id=assignment_id)
    had_submitted = submission_judge(request,user_account,assignment_id)
    submission = []
    if had_submitted:
        submission = models.Submission.objects.get(student_id=user_account,assignment_id=assignment_id)
    if request.method == "POST":
        file = request.FILES.get('filepath')
        message = request.POST.get('message')
        db_file_path = os.path.join("static", "submission", file.name)
        file_path = os.path.join("app01", db_file_path)
        f = open(file_path, mode='wb')
        for chunk in file.chunks():
            f.write(chunk)
        f.close()
        submission = models.Submission.objects.create(student=user,assignment=assignment, filepath=db_file_path, message=message)
        had_submitted = True

        return render(request, "assignment_detail_student.html",
                      {'user': user, 'assignment': assignment, 'had_submitted': had_submitted, 'submission':submission})
    return render(request, "assignment_detail_student.html",
                  {'user':user,'assignment':assignment,'had_submitted':had_submitted,'submission':submission})

def download_file(request,file_id):
    try:
        assignment = models.Assignment.objects.get(id=file_id)
        # 拼接想要下载的文件的完整文件路径: [项目根目录]/app01/static/assignment/filepath
        file_path = os.path.join(
            settings.BASE_DIR,  # 项目根目录
            'app01',  # app01 文件夹
            assignment.filepath  # 数据库中存储的路径
        )
        # 标准化路径（处理斜杠方向问题）
        file_path = os.path.normpath(file_path)
        # 安全检查：确保文件在 app01/static 目录内
        static_dir = os.path.join(settings.BASE_DIR, 'app01', 'static')
        if not file_path.startswith(static_dir):
            raise Http404("非法访问")
        # 检查文件是否存在
        if not os.path.exists(file_path):
            raise Http404("文件不存在")
        # 打开文件并返回响应
        response = FileResponse(open(file_path, 'rb'))
        # 设置 Content-Disposition 强制下载
        response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
        # print("1234567890")
        return response

    except models.Assignment.DoesNotExist:
        raise Http404("作业不存在")
    except Exception as e:
        raise Http404(f"下载失败: {str(e)}")

def user_set(request,user_account):
    user = models.User.objects.get(account=user_account)
    if request.method == "GET":
        return render(request, "user_set.html", {"user": user})
    elif request.method == "POST":
        action = request.POST.get('action')
        if action == 'update_role':  # 处理角色更新
            role_value = request.POST.get('role_value')
            # 将角色文本值映射为模型中的整数值
            role_mapping = {'教师': 1, '学生': 2}
            role_code = role_mapping.get(role_value)
            if role_code is not None:
                user.role = role_code
                user.save()
                return JsonResponse({
                    'status': 'success',
                    'message': '角色更新成功',
                    'role_display': user.get_role_display()  # 返回角色的显示文本
                })
            else:
                return JsonResponse({'status': 'error', 'message': '无效的角色选择'}, status=400)
        if action == 'update_phone':  # 处理手机号修改
            new_phone = request.POST.get('new_phone')
            if new_phone:
                user.phone = new_phone
                user.save()
                return JsonResponse({'status': 'success', 'message': '手机号更新成功'})
            else:
                return JsonResponse({'status': 'error', 'message': '新手机号不能为空'}, status=400)
        if action == 'update_pw':  # 处理密码修改
            pw1 = request.POST.get('pw1')
            pw2 = request.POST.get('pw2')
            if pw1 and pw2 and pw1 == pw2:
                user.password=pw1
                user.save()
                return JsonResponse({'status': 'success', 'message': '密码更新成功'})
            else:
                return JsonResponse({'status': 'error', 'message': '两次密码输入不相等或密码输入不完整！'}, status=400)
        else:   #编辑信息
            name = request.POST.get('name')
            serial_number = request.POST.get('serial_number')
            school = request.POST.get('school')
            major = request.POST.get('major')
            if name:
                user.name = name
            if serial_number:
                user.serial_number = serial_number
            if school:
                user.school = school
            if major:
                user.major = major
            user.save()
            return HttpResponse("数据更新成功")

def submission_detail_teacher(request,user_account,assignment_id):
    user = models.User.objects.get(account = user_account)
    assignment =models.Assignment.objects.get(id=assignment_id)
    course = models.Course.objects.get(id=assignment.course_id)
    records = models.Student_Course.objects.filter(course=course)
    students = []
    for record in records:
        student = models.User.objects.get(account=record.student.account)
        students.append(student)
    # 仅传递已交作业的学生id
    submited_students = []
    submissions = models.Submission.objects.filter(assignment=assignment)
    for submission in submissions:
        if submission.student in students:
            submited_students.append(submission.student.account)
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        score = request.POST.get('score')
        if student_id and score:
            # todo 这里需要添加一个save逻辑，否则会跳出一个保存失败，建议调试的时候把下面的else返回那行注释掉
            print(student_id, score)
            for submission in submissions:
                if submission.student.account==student_id:
                    models.Submission.objects.filter(id=submission.id).update(grade=score)
            return JsonResponse({'status': 'success', 'message': '成绩修改成功！'})
        else:
            return JsonResponse({'status': 'error', 'message': '成绩丢失或学生ID不存在！'}, status=400)
    return render(request,"submission_detail_teacher.html",{'assignment':assignment,"user":user,'submissions':submissions,'students':students,'submited_students':submited_students})

def a_submission_detail(request, user_account,assignment_id,submission_id):
    user = models.User.objects.get(account=user_account)
    assignment =models.Assignment.objects.get(id=assignment_id)
    submission = models.Submission.objects.get(id=submission_id)
    if request.method == "POST":
        grade = request.POST.get('grade')
        models.Submission.objects.filter(id=submission_id).update(grade=grade)
        feedback = request.POST.get('feedback')
        if feedback:
            models.Submission.objects.filter(id=submission_id).update(feedback=feedback)
        return redirect('submission_detail_teacher', user_account,assignment_id)
    return render(request,"submission_detail_teacher_a_student.html",{'assignment':assignment,"user":user,'submission':submission})

