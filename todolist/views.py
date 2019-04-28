from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        if request.POST['待办事项'] == '':
            return render(request,'todolist/home.html',{'未输入事项':'请输入事项'})
        else:
            content = {'待办事项':request.POST['待办事项']}
            return render(request,'todolist/home.html',content)
    if request.method == 'GET':
        return render(request,'todolist/home.html')

def about(request):
    return render(request,'todolist/about.html')

def edit(request):
    return render(request,'todolist/edit.html')