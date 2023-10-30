from django.shortcuts import render
from django.views import generic 
from .models import post 

class PostList(generic.ListView):
    model = Post 
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    tempalte_name = 'index.html'
    paginate_by = 6 