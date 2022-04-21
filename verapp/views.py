from django.shortcuts import render,HttpResponse
from verapp import views
from .forms import StudentRegistration
from .models import StudebtRegistration
from django.http import HttpResponseRedirect
from django.db.models import Avg,Sum,Max,Count,Min
from django.db.models import Q,F
from django.contrib import messages
from django.views import View
#from django.db.models import 
def student_view(request):
    if(request.method=='POST'):
        form=StudentRegistration(request.POST)
        if(form.is_valid()):
            fm=form.cleaned_data['studentName']
            fm2=form.cleaned_data['studentId']
            fm3=form.cleaned_data['studentClass']
            fm4=form.cleaned_data['StudentGuardiandName']
            fm5=form.cleaned_data['StudentCollegeName']
            fm6=form.cleaned_data['studentPasssword']
            reg=StudebtRegistration(studentName=fm,studentId=fm2,studentClass=fm3,StudentGuardiandName=fm4,StudentCollegeName=fm5,studentPasssword=fm6)
            reg.save()
            #messages.add_message(request,messages.SUCCESS,'YOUR A/C HAS BEEN CREATED SUCCESFULLY !!!')
            #messages.info(request,'now ypu can login !!!')           '''DEBUG=10,INFO=20,SUCCESS=25,# WARNING: 30,ERRORR=40'''
            #print(messages.get_level(request))
            #messages.set_level(request,messages.DEBUG)
            #messages.debug(request,'yhis is debug!!!')
            #print(messages.get_level(request))
            messages.info(request,'info')
            messages.success(request,'susscess')
            messages.warning(request,'WARNING: ')
            messages.error(request,'error')
    else:
        form=StudentRegistration()
    #StudebtRegistration.objects.filter(studentId=F('studentClass')*2)
    stu=StudebtRegistration.objects.all()
    average=stu.aggregate(Avg('studentId'))#aggregate functions
    max=stu.aggregate(Max('studentId'))#aggregate functions#aggregate functions#aggregate functions
    min=stu.aggregate(Min('studentId'))#aggregate functions#aggregate functions
    su1m=stu.aggregate(Sum('studentId'))#aggregate functions
    count=stu.aggregate(Count('studentId'))#aggregate functions
    gg=StudebtRegistration.objects.filter(studentId=F('studentClass'))#filter
    #gg1=StudebtRegistration.objects.filter(studentName='abhinadas Sahoo')#filter
    #using prefetch
    #gg1=StudebtRegistration.objects.order_by('vgtudentName')#asc
    gg1=StudebtRegistration.objects.order_by('-studentName')#desc
    #gg1=StudebtRegistration.objects.order_by('?')#changes randomly
    
    #reverse
    gg5=StudebtRegistration.objects.order_by('studentName').reverse()[:5]
    #values
    gg5=StudebtRegistration.objects.values('studentId','studentName')
    #delete
    #gg5=StudebtRegistration.objects.filter(studentId=1364).delete()
    #values_list-for tuple
    #gg5=StudebtRegistration.objects.values_list('studentId','studentPasssword',named=True)
    #using default EventVillian
    #for updating
    #gg5=StudebtRegistration.objects.all().update(studentClass=10)
    #if we are using date fields then
    #gg5=StudebtRegistration.objects.dates('pass_date-column name','year')
    #gg5=StudebtRegistration.objects.dates('pass_date','month')
    #gg5=StudebtRegistration.objects.dates('pass_date','year')
    #and |or operator
    #gg5=StudebtRegistration.objects.filter(studentId=201)&StudebtRegistration.objects.filter(studentName='Kalapata Rassa')
    #gg5=StudebtRegistration.objects.filter(studentId=201) or StudebtRegistration.objects.filter(studentName='Kalapata Rassa')    
    #or
    #from django.db.models import Q
    #gg5=StudebtRegistration.objects.filter(Q(studentId=201) & Q(studentName='Kalapata Rassa'))
    #gg5=StudebtRegistration.objects.filter(Q(studentId=201) |Q(studentName='Kalapata Rassa'))
    #gg5=StudebtRegistration.objects.select_for_update(of=('studentId','studentName'))
    return render(request,'adddndshow.html',{'forms':form,'students':stu,'average':average,'max':max,'min':min,'count':count,'gg':gg,'#gg1':gg5})


def delete_data(request,id):
    if (request.method=='POST'):
        user=StudebtRegistration.objects.get(pk=id)
        user.delete()
        return HttpResponse('deleted succesfully')
    
    
def edit_data(request,id):
    if(request.method=='POST'):
        user=StudebtRegistration.objects.get(pk=id)
        stk=StudentRegistration(request.POST,instance=user)
        if (stk.is_valid()):
            stk.save()
    else:
        user=StudebtRegistration.objects.get(pk=id)
        stk=StudentRegistration(instance=user)
    return render(request,'update.html',{'form23':stk})
dd

class Mview(View):
        name="Sonam"
        def get(self,request):
            return HttpResponse(self.name)
