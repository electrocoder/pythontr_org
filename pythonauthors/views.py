#-*- coding:utf-8 -*- 
from myproject.pythoncoders.models import PythonCoders
from myproject.pythoncoders.form import PythonCodersForm
from myproject.pythonauthors.models import PythonAuthors
from myproject.pythonauthors.form import PythonAuthorsForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import Context, loader
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
import os, time, datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

DIRNAME = os.path.dirname(__file__)

@csrf_exempt
def contact(request):
    ret=[]
    if request.method == 'POST': # If the form has been submitted...
        form = PythonAuthorsForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid():
            ad_soyad = form.cleaned_data['ad_soyad']
            resim_yolu = form.cleaned_data['resim_yolu']
            web_adresi = form.cleaned_data['web_adresi']
            e_posta = form.cleaned_data['e_posta']
            makale_bilgi = form.cleaned_data['makale_bilgi']
                    
            from django.core.mail import send_mail
            mesaj="Katkinizdan dolayı tesekkur ederiz.\n\n Makaleniz onaylandiktan sonra yayinlanacaktir.\n\n Sorularınız ve proje ihtiyacınız için admin@pythontr.org mail adresimize veya 'python programcilari' Google grubumuza danışabilirsiniz.\n\n www.pythontr.org"
            send_mail('sayin ' + ad_soyad + ' pythoncular arasindasiniz', mesaj, 'admin@pythontr.org', [e_posta], fail_silently=False)
            ret.append("Sayin " + ad_soyad +" makale desteginiz icin tesekkur ederiz...")
            ret.append("'" + e_posta + "' adresine bilgilendirme icin bir e posta gonderdik.")
            
            send_mail('sayin admin yeni makale var', ' gonderen : ' + e_posta + ' site : ' + web_adresi + ' icerik : ' + makale_bilgi, 'admin@pythontr.org', ['electrocoder@gmail.com'], fail_silently=False)
            
            PythonAuthors(pythonauthors_name=ad_soyad,
                         pythonauthors_photo=resim_yolu,
                         pythonauthors_web=web_adresi,
                         pythonauthors_email=e_posta,
                         pythonauthors_content=makale_bilgi).save()
            
            x = Context({
                      'ret':ret,
                      })            
            #return HttpResponse(ret) # Redirect after POST
            return render_to_response('pythonauthors/thanks.html', {'ret':ret,})            
        
    else:
        form = PythonAuthorsForm() # An unbound form
        ret.append(" else ")
    return render_to_response('pythonauthors/pythonauthors.html', {'form': form,})
    #return HttpResponse('son...') # Redirect after POST  

def list(request):
    """
    kayitli python programcilarinin listesi
    """
    try:
        all_coder = PythonCoders.objects.all().filter().order_by('-pythonauthors_name')
        
        x = Context({
                  'all_coder':all_coder,
                  })
        
    except:
        raise Http404
            
    return render_to_response('pythonauthors/python-programcilari-liste.html', x)    
