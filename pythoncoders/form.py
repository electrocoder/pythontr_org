from django import forms

class PythonCodersForm(forms.Form):
    """
    python kullanicilari icin kayit ekrani
    """
    ad_soyad = forms.CharField(max_length=100)
    resim_yolu = forms.ImageField(required=False)
    web_adresi = forms.CharField(required=False)
    e_posta = forms.EmailField()
    kisa_bilgi = forms.CharField(max_length = 200, required=False)    
    git_adresi = forms.CharField(max_length = 175, required=False)    
    cep_telefonu = forms.CharField(max_length = 11, required=False)    
    python_bilgi_seviyesi = forms.CharField(max_length = 2, required=False)    
