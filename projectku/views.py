from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm
from .models import doc_psd
from django.http import HttpResponseRedirect

def index (request):
    posts = doc_psd.objects.all()
    context ={
        'page_title':'Dokumentasi PSD',
        'sub_judul':'deskripsi',
        'action':'Solusi',
        'wfm' : 'Segment WFM Problem',
        'posts':posts,
    }
    return render (request,'projectku/index.html',context)

def create(request):
    post_form = PostForm()
    if request.method == 'POST':
        doc_psd.objects.create(
            title = request.POST.get('judul'),
            body = request.POST.get('body'),
            category = request.POST.get('category'),
        )

        return HttpResponseRedirect("/projectku/")

    context = {
        'page_title':'create post',
        'sub_judul':'Dokumentasi PSD',
        'post_form':post_form,
    }
    return render(request,'projectku/create.html',context)