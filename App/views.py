from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks=Task.objects.all()
    #lấy tất cả các task từ cơ sở dữ liệu
    return render(request,'index.html',{'tasks':tasks})

def newlisttodo(request):
    todo_tasks=Task.objects.filter(status='todo')
    working_tasks=Task.objects.filter(status='working')
    done_tasks=Task.objects.filter(status='done')
    edit_id=request.GET.get('edit_id')
    print(edit_id)
    return render(request,'newtodo.html',{
        'todo_tasks':todo_tasks,
        'working_tasks':working_tasks,
        'done_tasks':done_tasks,
        'edit_id':int(edit_id) if edit_id else None,
    })

#thêm task vào cơ sở dữ liệu
def add_task(request):
    if request.method=='POST':
        #lấy trường dữ liệu task_description từ form
        task_description=request.POST.get('task_description')
        status=request.POST.get('status','todo')
        if task_description:
            #lưu task vào cơ sở dữ liệu
            Task.objects.create(description=task_description,status=status)
        # chuyển hướng về trang chính
        return redirect('newlisttodo')
    else:
        # chuyển hướng về trang chính
        return redirect('newlisttodo')
#xóa task khỏi cơ sở dữ liệu

def delete_task(request,task_id):
    #lấy task theo id
    task=Task.objects.get(id=task_id)
    #xoá task
    task.delete()
    # chuyển hướng về trang chính
    return redirect('newlisttodo')
    
def edit_task(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method =='POST':
        description = request.POST.get('description','').strip()
        status = request.POST.get('status', task.status)
        if description:
            task.description = description
        if status in dict(Task.STATUS_CHOICES):
            task.status = status
        task.save()
        return redirect('newlisttodo')
    


















def baitho(request):
    return HttpResponse('Xin Chào Baitho')
# Create your views here.

def amDuong(request,a):
    a=int(a)
    if a>0:
        return HttpResponse(f'{a} là số dương')
    else:
        return HttpResponse(f'{a} là số âm')
    
def phepNhan(request,a):
    a=int(a)
    result=''
    for i in range(1,11,1):
        result+=f'{a}x{i}={a*i}<br>'
    
    return HttpResponse(result)

