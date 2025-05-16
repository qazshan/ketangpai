# Create your views here.
import os
from django.utils.dateparse import parse_datetime
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404, JsonResponse
from django.conf import settings

from django.shortcuts import render,redirect,HttpResponse
from app01 import models

def login(request):
    if request.method == "POST":
        account = request.POST['account']
        password = request.POST['password']
        print(account,password)
        #todo 还有账号不存在的情况没判断 优化：逻辑判断
        row_obj = models.User.objects.filter(account = account).first()
        if row_obj.password:
            if row_obj.password == password:
                if row_obj.role == 1:
                    return redirect('teacher_main',user_account = row_obj.account)    #todo 将user_id改成nid?
                else:
                    return redirect('student_main',user_account = row_obj.account)
            else:
                return HttpResponse("登录失败，密码错误")
        else:
            return HttpResponse("账号不存在")
    #     {'account':account,'password':password,'role':role}
    return render(request,'login.html')

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
    if request.method == "POST":
        course_id = request.POST.get('course_id')
        course = models.Course.objects.filter(id=course_id).first()
        models.Student_Course.objects.create(student=user,course=course)
        #todo 这里添加课程之后还要手动刷新，有没有方法优化，用render？
        return redirect('student_main',user_account = user_account)
    objects = models.Student_Course.objects.filter(student_id=user_account)
    courses = []
    for obj in objects:
        row_course = models.Course.objects.filter(id=obj.course_id).first()
        # print(row_course.name)
        courses.append(row_course)
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

#根据用户身份的不同在统一界面渲染不同的东西 or 直接两个课程内容的界面 倾向后者
def course_detail_student(request,course_id,user_account):
    user = models.User.objects.get(account=user_account)
    chapters = models.Chapter.objects.filter(course_id=course_id)
    assignments = models.Assignment.objects.filter(course_id=course_id)
    students = models.Student_Course.objects.filter(course_id=course_id)
    return render(request, 'course_detail_student.html', {"user":user,'course':models.Course.objects.filter(id=course_id).first(),'chapters':chapters,'assignments':assignments,"students":students})

def course_detail_teacher(request,course_id):
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
    return render(request, 'course_detail_teacher.html', {'course':models.Course.objects.filter(id=course_id).first(),'chapters':chapters,'assignments':assignments,"students":students})

def assignment_detail_student(request,assignment_id,user_account):
    user = models.User.objects.get(account=user_account)
    assignment = get_object_or_404(models.Assignment, id=assignment_id)
    return render(request, "assignment_detail_student.html",{'user':user,'assignment':assignment})

def download_assignment(request,assignment_id):
    try:
        assignment = models.Assignment.objects.get(id=assignment_id)
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
        else: #编辑信息
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