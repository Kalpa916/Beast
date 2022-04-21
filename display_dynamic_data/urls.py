
from django.contrib import admin
from django.urls import path
from verapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.student_view),
    path('Delete/<int:id>/',views.delete_data,name='delete_'),
    path('<int:id>/',views.edit_data,name='update_'),
    path('clds',views.Mview.as_view(),name='clds')
]

