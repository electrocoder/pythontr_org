from django import forms

class PythonAuthorsForm(forms.Form):
    """
    python kullanicilari icin kayit ekrani
    """
    ad_soyad = forms.CharField(max_length=100)
    resim_yolu = forms.ImageField(required=False)
    web_adresi = forms.CharField(required=False)
    e_posta = forms.EmailField()
    makale_bilgi = forms.CharField ( widget=forms.widgets.Textarea() )
