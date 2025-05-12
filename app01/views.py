# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from app01 import models

def login(request):
    if request.method == "POST":
        account = request.POST['account']
        password = request.POST['password']
        print(account,password)
        #还有账号不存在的情况没判断 优化：逻辑判断
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

    return render(request, 'teachermain.html',{'user':user})

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
def course_detail_student(request,course_id):
    return render(request, 'course_detail_student.html', {'course':models.Course.objects.filter(id=course_id).first()})