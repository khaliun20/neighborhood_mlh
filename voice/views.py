from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm #add this
from .models import Thread, Label, Message
from .forms import ThreadForm, MessageForm
from django.contrib.auth.decorators import login_required


def start(request):
    return render(request, 'voice/start.html')

def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    threads = Thread.objects.filter(label__name__icontains=q)
    labels = Label.objects.all()
    context = {'threads': threads, 'labels': labels}
    return render(request, 'voice/homepage.html', context)

def thread(request, pk):
    thread= Thread.objects.get(id=pk)
    thread_messages = thread.message_set.all().order_by('-created')
    if request.method =="POST":
          message = Message.objects.create(
                
                user = request.user,
                thread = thread,
                body = request.POST.get('body')
          )
          return redirect('thread', pk = thread.id)

    context = {'thread': thread, 'thread_messages': thread_messages}
    return render(request, 'voice/thread.html', context)

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("start")

def register_request(request):
	if request.method == "POST":
		#created instance of NewUserForm and initialize it with data from request.POST
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			#return to the homepage view of the voice app
			return redirect("/login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="voice/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="voice/login.html", context={"login_form":form})

@login_required(login_url ='login')
def createThread(request):
    form = ThreadForm()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'voice/thread_form.html', context)


@login_required(login_url ='login')
def updateThread(request, pk):
    thread = Thread.objects.get(id=pk)
    form = ThreadForm(instance=thread)

    if request.method == "POST":
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'voice/thread_form.html', context)

@login_required(login_url ='login')
def deleteThread(request, pk):
      thread = Thread.objects.get(id=pk)
      if request.method == "POST":
            thread.delete()
            return redirect('homepage')
      return render (request, 'voice/delete.html', {'obj':thread})