from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponseRedirect
# # Create your views here.
# def ShowData(request):
#     if request.method=='POST':
#         fm=StudentForm(request.POST)
#         if fm.is_valid():
#             print('name',fm.cleaned_data['name'])
#             print('email',fm.cleaned_data['email'])
#             print('contact',fm.cleaned_data['contact'])
#             print('password',fm.cleaned_data['password'])
#     else:
#         fm=StudentForm()
#     return render(request,'home.html',{'form':fm})

def Success(request):
    return render (request,'success.html',)

def ShowData(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            print('name',name)
            print('email',email)
            print('password',password)
            return HttpResponseRedirect('/core/suc/') #urls of funxtion
            # return render(request, 'success.html',{'nm':name})
           
    else :
         fm=StudentForm()
    return render(request,'home.html',{'form':fm})
