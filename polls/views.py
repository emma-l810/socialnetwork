from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    """
    first view (home page) - move login to own view?
    """
    # checks if any form data has been submitted
    if request.POST:
        # checks if the form submitted is the login form (by checking for username input)
        if 'inputUsername' in request.POST.keys():
            # attempt authentication of login info
            user = authenticate(username=request.POST['inputUsername'],
                password=request.POST['inputPassword'])
            if user is not None:
                # if the user exists, then log in the user
                login(request, user)
            else:
                # go on to the next check
                pass
        # checks if the form submitted is the logout form
        elif 'logout' in request.POST.keys():
            # kill the section
            logout(request)

    # sets loggedIn variable to be used in HTML
    if request.user.is_authenticated:
        loggedIn = True
    else:
        loggedIn = False

    # gets all posts and comments from the respective models
    allposts = Post.objects.order_by('-pub_date')
    allcomments = Comment.objects.order_by('-pub_date')

    # creates json
    context = {
        'allposts': allposts,
        'allcomments': allcomments,
        'loggedIn': loggedIn,
        'user': request.user
        }

    return render(request, 'polls/index.html', context)

def profile(request):
    """
    for the user profile (profile page) -> for login=true only
    """
    context = {}
    return render(request, 'polls/profile.html', context)

# def messages(request):
#     """
#     for the reply box -> for login=true only
#     """
#     context = {}
#     return render(request, 'polls/reply.html', context)
