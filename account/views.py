from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from .forms import UserRegisterForm
from .models import UserProfileInfo
# Create your views here.
class RegisterView(View):
    template_name = 'register.html'
    form_class = UserRegisterForm
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{'form':self.form_class()})
    
    def post(self, request):
        form= self.form_class(request.POST)
        
        
        if form.is_valid():
            user_type= request.POST.get('user_type')
            if user_type == 'EMPLOYER':
                UserProfileInfo.objects.create(user=form.save(),user_types=user_type)
                return render(request,'employer_home.html')
            
            elif user_type == 'JOBSEEKER':
                UserProfileInfo.objects.create(user=form.save(),user_types=user_type)
                return render(request,'job_seeker_home.html')
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})