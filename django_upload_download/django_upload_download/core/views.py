from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from core.models import FileHandler
from core.forms import FileHandlerForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('core:index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request,'core/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('core:login')
# Create your views here. Class base view(CBV)
class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        get_files = FileHandler.objects.all()
        context['form'] = FileHandlerForm()  # Khởi tạo một instance của form
        context['get_files'] = get_files
        context = {'form':FileHandlerForm,'get_files':get_files}
        return context
    
    def post(self,request,**kwargs):
        context = {}
        if request.method == 'POST':
            form = FileHandlerForm(request.POST,request.FILES)

            if form.is_valid():
                FileHandler.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))
                
                return redirect('core:index')
            else:
                context['form'] = form
        else:
            context['form'] = form
        
        return redirect('core:index')
    
    
