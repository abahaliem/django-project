from django.shortcuts import render

def index (request):
    context ={
        'page_title':'Dokumentasi PSD',
        'sub_judul':'deskripsi',
        'action':'Solusi',
    }

    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']

    return render (request,'index.html',context)