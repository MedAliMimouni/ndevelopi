from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from urllib.request import urlopen
from re import findall
from django.shortcuts import reverse
# Create your models here.

class Course(models.Model):

    title        = models.CharField(max_length=50, help_text="your cource's title")

    short_summary= models.CharField(max_length=80, help_text="simple and short summary",blank=True,null=True)

    summary      = models.TextField(max_length=1000, help_text="Enter a brief description of the cource")

    image        = models.FileField(null=True,blank=True)

    date = models.DateField()

    github_url   = models.URLField(max_length=256,help_text="Enter the github url page that includes all commits")

    requirements = models.ManyToManyField("Requirements", help_text="Select the requirments for this book")

    authors      = models.ForeignKey("Authors",null=True,help_text="Who are the author of this cource ")

    slug         = models.SlugField(help_text="enter a slug for the course (a slug is the name in the url exemple you enter html the link will be ndevelopi/html/ ...")

    enrolled     = models.ManyToManyField(User)



    def __str__(self):
        return self.title


class Chapiter(models.Model):

    name   = models.CharField(max_length=256,help_text="your chpiter title")

    chpiterSlug = models.SlugField(null=True,blank=True,help_text="enter a slug for the course (a slug is the name in the url exemple you enter html the link will be ndevelopi/html/ ...")

    youtube_url = models.URLField(max_length=256, help_text="Enter the yourtube url playlist",blank=True,null=True)

    course = models.ForeignKey('Course',on_delete=models.CASCADE)

    completed = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.name


class Youtube_links(models.Model):

    link = models.URLField(max_length=256,help_text="url video")

    name = models.CharField(max_length=256,null=True)

    index = models.PositiveSmallIntegerField(blank=True,null=True)

    chapiter = models.ForeignKey('Chapiter', on_delete=models.CASCADE)

    seen = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('video', kwargs={'slug':self.chapiter.course.slug,'chpiter_slug':self.chapiter.chpiterSlug,'pk':str(self.index).zfill(2)})



def get_playlist_links(playlist_url):
    page_elements = urlopen(playlist_url).readlines()
    video_elements = [str(el,'utf-8') for el in page_elements if 'pl-video-title-link' in str(el,"utf-8")]  # Filter out unnecessary lines
    video_urls = [v.split('href="',1)[1].split('" ',1)[0] for v in video_elements]  # Grab the video urls from the elements
    return ['https://www.youtube.com/embed/' + v[9:v.index("&amp")] for v in video_urls]

def create_youtube_links(sender,**kwargs):
    if kwargs['created']:
        play_list_url = kwargs['instance'].youtube_url
        t=get_playlist_links(playlist_url=str(play_list_url))
        for count, i in enumerate(t,1):
            name = get_name(i)
            x = Youtube_links(link=i,name=name,index=count,chapiter =kwargs['instance'])
            x.save()

def get_name(link):
    html = str(urlopen(link).read(),'utf-8')
    return findall("<title>(.*?) - YouTube",html)[0]


post_save.connect(create_youtube_links,sender=Chapiter)

class Requirements(models.Model):

    name = models.CharField(max_length=150,help_text="requirment subject (like html)")

    info = models.TextField(max_length=300,help_text="basic info of what should the student learn for this subject ")

    def __str__(self):
        return self.name

class Goals(models.Model):

    name = models.CharField(max_length=150,help_text="requirment subject (like html)")

    info = models.TextField(max_length=300,help_text="basic info of what should the student learn for this subject ")

    course = models.ForeignKey('Course', on_delete=models.CASCADE)

class Authors(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField(null=True, blank=True)

    email = models.EmailField(max_length=254)

    overview = models.TextField(max_length=1000,help_text="write a brief overview")

    instagram_acc = models.URLField(max_length=200,help_text="enter your instagram's link",blank=True,null=True)

    facebook_acc = models.URLField(max_length=200,help_text="enter your facebook's link",blank=True,null=True)

    github_acc = models.URLField(max_length=200,help_text="enter your github's link",blank=True,null=True)

    youtube_acc = models.URLField(max_length=200,help_text="enter your instagram's link",blank=True,null=True)

    def __str__(self):
        return self.last_name
