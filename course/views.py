from django.shortcuts import render
from django.http import Http404
from social_django.models import UserSocialAuth
# from .forms import RegistrationForm
from .models import Course,Youtube_links,Chapiter
from django.views.generic import DetailView,ListView
from django.shortcuts import get_object_or_404
# Create your views here.

# def home(request):
    # if request.user.is_authenticated():
    #     return redirect('/home/')
    # if request.method=='POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/home/')
    # else:
    #     form = RegistrationForm()
    # user = UserSocialAuth.field_names()
    # user_id = -1
    # if request.user.is_authenticated:
    #     try:
    #         user_id = request.user.social_auth.get(provider='facebook').uid
    #     except:
    #         pass
    # context = {'Course':Course.objects.all(),'user_id':user_id}
    # return render(request, 'home.html', context)
    # "user.social_auth.exists()","user.social_auth.filter(provider='facebook'):"
class Home(ListView):
    model = Course
    template_name = 'home.html'


class DetailCourse(DetailView):
    model = Course
    context_object_name = 'course'



def detail_video(request,slug,chpiter_slug,pk):
    ch= get_object_or_404(Chapiter,chpiterSlug=chpiter_slug)
    int_pk = int(pk)
    if ch.course.slug == slug:
        if int_pk == 1:
            if not (ch.course in request.user.course_set.all()):# and request.user in ch.course.enrolled.all()):
                request.user.course_set.add(ch.course)
                # ch.course.enrolled.add(request.user)
                request.user.chapiter_set.add(ch)
        videos = ch.youtube_links_set.all()
        if len(videos)<int_pk:
            raise Http404("video does not exist")
    else:
        raise Http404("course does not exist")
    context = {'chapiter':ch,'video':videos[int_pk-1]}
    return render(request,'course/detail_video.html',context)


