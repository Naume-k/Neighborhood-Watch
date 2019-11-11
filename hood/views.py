from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .forms import NewPostForm, NewBusinessForm, NewProfileForm
from .models import Profile, Businesses, Posts

# Create your views here.

def home(request):
    try:
        profile = Profile.objects.filter(user_id=request.user.id)
        arr = []
        for new in profile:
            arr.append(new.neighbourhood.id)
        if len(arr)>0:
            id = arr[0]
            posts=Posts.objects.filter(neighbourhood=id)
        else:
            posts=Posts.objects.filter(neighbourhood=10000000000)
    except Exception as e:
        raise Http404()
    
    return render(request,'home.html', {"posts":posts, "profile":profile})


def businesses(request):
    current_user = request.user
    try:
        profile = Profile.objects.filter(user=request.user)
        arr=[]
        for biz in profile:
            arr.append(biz.neighbourhood.id)
        if len(arr)>0:
            id=arr[0]
            businesses=Businesses.objects.filter(business_neighbourhood=id)
        else:
            businesses=Businesses.objects.filter(business_neighbourhood=10000000000)
    except Exception as e:
        raise Http404()
        
        title = "Neighborhoods Businesses"

    return render(request,'businesses.html', {"id":id, "businesses":businesses})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.poster_id = current_user.id
            post.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.userId = request.user.id
            profile.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        form = NewProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request,'edit_profile.html',{'form':form})

def profile(request):
    current_user = request.user
    posts = Posts.objects.filter(profile = current_user)

    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{ 'profile':profile,'posts':posts,'current_user':current_user})




@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('businesses')

    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {"form": form})


def search_results(request):
    if 'business' in request.GET and request.GET ["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Businesses.search_by_business_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {"message":message, "businesses":searched_businesses})

    else:
        message = "You haven't searched for any businesses yet!"
        return render (request, 'search.html', {"message": message})