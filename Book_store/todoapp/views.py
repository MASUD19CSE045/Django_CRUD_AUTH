from django.shortcuts import render,redirect
from todoapp.forms import TodoItemModel
from todoapp.forms import TodoItemForm
# Create your views here.
def addtodo(request):
    if request.method=='POST':
        form=TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showtodo')
    else:
        form=TodoItemForm()
    return render(request,"add.html", {'form':form})

def updatetodo(request,id):
    todo = TodoItemModel.objects.get(pk = id )
    form = TodoItemForm(instance = todo)
    if request.method =='POST':
        todo = TodoItemForm(request.POST,instance = todo)
        if todo.is_valid():
            todo.save()
            return redirect("showtodo")
    return render(request,"add.html",{'form':form})

def showtodo(request):
    form=TodoItemModel.objects.all()
    return render(request,"showtodo.html" ,{"form":form})


def delete_todo(request,id):
    todo = TodoItemModel.objects.get(pk = id ).delete()
    return redirect('showtodo')