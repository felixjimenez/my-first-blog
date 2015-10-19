from .forms import PostForm
from .models import  Alumno, Aula, Carrera, Inscripcion, Institucion, Materia, Nota, Post, Seccion
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.save()
             return redirect('blog.views.post_detail', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})

def seccion_list(request):
    secciones = Seccion.objects.filter().order_by()
    return render(request,'blog/seccion_list.html',{'secciones':secciones})

def alumn_list(request):
    alumnos = Alumno.objects.filter().order_by()
    return render(request,'blog/alumn_list.html',{'alumnos':alumnos})

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def inscripcion_list(request):
    inscripciones = Inscripcion.objects.filter(fecha__lte = timezone.now()).order_by('seccion')
    return render(request,'blog/inscripcion_list.html',{'inscripciones':inscripciones})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
