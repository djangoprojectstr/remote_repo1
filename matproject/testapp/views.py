from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# from django.core.files.storage import FileSystemStorage
from testapp.forms import UserForm,Studsform,EditForm,Estudsform
# from testapp.forms import EditForm,Estudsform
from django.core.mail import send_mail
from django.conf import settings
# from django.conf import settings
from django.contrib.auth.hashers import check_password
from testapp.models import Matr
# from django.core.exceptions import ObjectDoesNotExist
# from django.http import HttpResponse, Http404
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
# Create your views here.
# @login_required
def homeview(request):
    return render(request,'testApp/home.html')


# @login_required
# def feedbackview(request):
#     return render(request,'testApp/feedback.html')
@login_required
def matchview(request):
    return render(request,'testApp/match.html')

def logoutview(request):
    return render(request,'testApp/logout.html')

def akhilview(request):
    return render(request,'testApp/akhil.html')

def siriview(request):
    return render(request,'testApp/siri.html')

def depview(request):
    return render(request,'testApp/dep.html')

def subview(request):
    return render(request,'testApp/sub.html')

def indexview(request):
    return render(request,'testApp/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = Studsform(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'photo' in request.FILES:
                print('found it')
                profile.photo = request.FILES['photo']
            profile.save()
            return redirect("/accounts/login")
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = Studsform()
    return render(request,'testapp/singup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})




@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'testApp/profile.html', args)






import datetime
@login_required
def wish(request):
    date=datetime.datetime.now()
    msg=None
    h=int(date.strftime('%H'))
    if h<12:
        msg='!!!! Very Very Good Morning!!!'
    elif h<16:
        msg='!!!! Very Very Good AfterNoon!!!'
    elif h<21:
        msg='!!!! Very Very Good Evening!!!'
    else:
        msg='!!!! Very Very Good Night!!!'
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'testApp/profile.html',context=my_dict)











@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)
        profile_form = Estudsform(request.POST, request.FILES, instance=request.user.matr)  # request.FILES is show the selected image or file

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('/accounts/login')
    else:
        form = EditForm(instance=request.user)
        profile_form = Estudsform(instance=request.user.matr)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'testapp/edit_profile.html', args)


@login_required
def fbkview(request):

	if request.method == 'POST':
		message = request.POST['message']
		send_mail('Contact Form',
		 message,
		 settings.EMAIL_HOST_USER,
		 ['python566775@gmail.com'],
		 fail_silently=False)
	return render(request, 'testapp/feedback.html')







def index(request):

	if request.method == 'POST':
		message = request.POST['message']
        # name = request.POST['name']
        # email= request.POST['email']

		send_mail('Contact Form',
		 message,
		 settings.EMAIL_HOST_USER,
		 ['python566775@gmail.com'],
		 fail_silently=False)
	return render(request, 'testapp/home.html')



# from django.core.mail import send_mail
# from testapp.forms import EmailSendForm

# def fbkview(request,id):
#         post=get_object_or_404(Post,id=id,status='published')
#         sent=False
#         if request.method=='POST':
#              form=EmailSendForm(request.POST)
#              if form.is_valid():
#                  cd=form.cleaned_data
#                  subject='{}({}) recommends you to read"{}"'.format(cd['name'],cd['email'],post.title)
#                  post_url=request.build_absolute_uri(post.get_absolute_url())
#                  message='Read Post At:\n {}\n\n{}\'s Comments:\n{}'.format(post_url,cd['name'],cd['comments'])
#                  send_mail(subject,message,'python@blog.com',[cd['to']])
#                  sent=True
#         else:
#             form=EmailSendForm()
#         return render(request,'testapp/feedback.html',{'form':form,'post':post,'sent':sent})
