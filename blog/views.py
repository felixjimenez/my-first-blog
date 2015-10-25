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
    alumnos = Alumno.objects.filter().order_by('apellido')
    return render(request,'blog/alumn_list.html',{'alumnos':alumnos})
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
def nota_info1(request):
    notas = Nota.objects.filter().order_by('fechaevalua')
    return render(request,'blog/notas_list.html',{'notas':notas})
def nota_info2(request):
    notas = Nota.objects.filter().order_by('fechaevalua')
    return render(request,'blog/notas_list.html',{'notas':notas})
def nota_bada1(request):
    notas = Nota.objects.filter().order_by('fechaevalua')
    return render(request,'blog/notas_list.html',{'notas':notas})
def nota_leng2(request):
    notas = Nota.objects.filter().order_by('fechaevalua')
    return render(request,'blog/notas_list.html',{'notas':notas})
def inscripcion_bada1(request):
    inscripciones = Inscripcion.objects.filter(seccion = 1).order_by('alumno')
    return render(request,'blog/inscripcion_list.html',{'inscripciones':inscripciones})
def inscripcion_leng2(request):
    inscripciones = Inscripcion.objects.filter(seccion = 3).order_by('alumno')
    return render(request,'blog/inscripcion_list.html',{'inscripciones':inscripciones})
def inscripcion_info1(request):
    inscripciones = Inscripcion.objects.filter(seccion = 4).order_by('alumno')
    return render(request,'blog/inscripcion_list.html',{'inscripciones':inscripciones})
def inscripcion_audi1(request):
    inscripciones = Inscripcion.objects.filter(seccion = 2).order_by('alumno')
    return render(request,'blog/inscripcion_list.html',{'inscripciones':inscripciones})
def inscripcion_info2(request):
    inscripciones = Inscripcion.objects.filter(seccion = 5).order_by('alumno')
    return render(request,'blog/inscripcion_list.html',{'inscripciones':inscripciones})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post})
