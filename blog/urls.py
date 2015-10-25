from django.conf.urls import include, url
from . import views

urlpatterns = [
       url(r'^post', views.post_list),
       url(r'^alumnos', views.alumn_list),
       url(r'^info1',   views.inscripcion_info1),
       url(r'^leng2',   views.inscripcion_leng2),
       url(r'^bada1',   views.inscripcion_bada1),
       url(r'^$',       views.inscripcion_info2),
       url(r'^audi1',   views.inscripcion_audi1),
       url(r'^ninfo1',  views.nota_info1),
       url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
       url(r'^post/new/$', views.post_new, name='post_new'),
       ]
