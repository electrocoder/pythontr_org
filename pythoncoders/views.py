#-*- coding:utf-8 -*- 
from myproject.pythoncoders.models import PythonCoders
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import Context, loader
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
import os, time
from django.http import HttpResponse
from myproject.pythoncoders.form import PythonCodersForm
from django.http import HttpResponseRedirect
# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

DIRNAME = os.path.dirname(__file__)

@csrf_exempt
def contact(request):
    ret=[]
    if request.method == 'POST': # If the form has been submitted...
        form = PythonCodersForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid():
            ad_soyad = form.cleaned_data['ad_soyad']
            resim_yolu = form.cleaned_data['resim_yolu']
            web_adresi = form.cleaned_data['web_adresi']
            e_posta = form.cleaned_data['e_posta']
            kisa_bilgi = form.cleaned_data['kisa_bilgi']
            git_adresi = form.cleaned_data['git_adresi']
            cep_telefonu = form.cleaned_data['cep_telefonu']
            python_bilgi_seviyesi = form.cleaned_data['python_bilgi_seviyesi']
                    
            from django.core.mail import send_mail
            #send_mail('sayin ' + ad_soyad + ' pythoncular arasindasiniz', 'her turlu sorununuz icin bizler buradayiz', 'admin@pythontr.org', [e_posta])
            ret.append("Sayin " + ad_soyad +" katiliminiz icin tesekkur ederiz...")
            x = Context({
                      'ret':ret,
                      })            
            #return HttpResponse(ret) # Redirect after POST
            return render_to_response('pythoncoders/thanks.html', {'ret':ret,})            
        
    else:
        form = PythonCodersForm() # An unbound form
        ret.append(" else ")
    return render_to_response('pythoncoders/pythoncoders.html', {'form': form,})
    #return HttpResponse('son...') # Redirect after POST  
