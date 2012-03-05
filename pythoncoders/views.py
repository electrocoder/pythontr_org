#-*- coding:utf-8 -*- 
from myproject.pythoncoders.models import PythonCoders
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import Context, loader
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
<<<<<<< HEAD
import os, time, datetime
from django.http import HttpResponse
from myproject.pythoncoders.form import PythonCodersForm
from django.http import HttpResponseRedirect

=======
import os, time
from django.http import HttpResponse
from myproject.pythoncoders.form import PythonCodersForm
from django.http import HttpResponseRedirect
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
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
<<<<<<< HEAD
            okul_durumu = form.cleaned_data['okul_durumu']
            is_durumu = form.cleaned_data['is_durumu']
=======
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
            git_adresi = form.cleaned_data['git_adresi']
            cep_telefonu = form.cleaned_data['cep_telefonu']
            python_bilgi_seviyesi = form.cleaned_data['python_bilgi_seviyesi']
                    
            from django.core.mail import send_mail
<<<<<<< HEAD
            mesaj="Sorularınız ve proje ihtiyacınız için admin@pythontr.org mail adresimize veya 'python programcilari' Google grubumuza danışabilirsiniz.\n\n www.pythontr.org"
            send_mail('sayin ' + ad_soyad + ' pythoncular arasindasiniz', mesaj, 'admin@pythontr.org', [e_posta], fail_silently=False)
            ret.append("Sayin " + ad_soyad +" katiliminiz icin tesekkur ederiz...")
            ret.append("'" + e_posta + "' adresine bilgilendirme icin bir e posta gonderdik.")
            
            send_mail('sayin admin', 'yeni coder var', 'admin@pythontr.org', ['electrocoder@gmail.com'], fail_silently=False)
            
            PythonCoders(pythoncoders_name=ad_soyad,
                         pythoncoders_photo=resim_yolu,
                         pythoncoders_web=web_adresi,
                         pythoncoders_email=e_posta,
                         pythoncoders_bio=kisa_bilgi,
                         pythoncoders_school=okul_durumu,
                         pythoncoders_job=is_durumu,
                         pythoncoders_git=git_adresi,
                         pythoncoders_mobil=cep_telefonu,
                         pythoncoders_star=python_bilgi_seviyesi,
                         pythoncoders_pubdate=datetime.datetime.now()).save()
            
=======
            #send_mail('sayin ' + ad_soyad + ' pythoncular arasindasiniz', 'her turlu sorununuz icin bizler buradayiz', 'admin@pythontr.org', [e_posta])
            ret.append("Sayin " + ad_soyad +" katiliminiz icin tesekkur ederiz...")
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
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
<<<<<<< HEAD

def list(request):
    """
    kayitli python programcilarinin listesi
    """
    try:
        all_coder = PythonCoders.objects.all().filter().order_by('-pythoncoders_pubdate')
        
        x = Context({
                  'all_coder':all_coder,
                  })
        
    except:
        raise Http404
            
    return render_to_response('pythoncoders/python-programcilari-liste.html', x)    
=======
>>>>>>> b8149290e5e381e24a6bcc14e2a300edf0b9ae60
