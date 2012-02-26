from django.db import models
import datetime

class CodeBanks(models.Model):
    Author=models.CharField("Yazar", max_length=50)
    Title=models.CharField("Baslik", max_length=150)
    Tags=models.CharField("Etiket(ler)", max_length=20)
    Body=models.TextField("Icerik", help_text = 'Bu alanda HTML kullanabilirsiniz. Alt satir icin < br> kullanin.')
    Catogori=models.CharField("Katogori", max_length=20)
    Pubdate=models.DateTimeField("Yayin tarihi")
    Update=models.DateTimeField("Guncelleme tarihi")
    Publish=models.BooleanField("Yayinlansinmi?")
    Link=models.SlugField("Kisa link")
    Image=models.CharField("Resim")
    Video=models.CharField("Video")
    OtherDownloadLink=models.CharField("Diger indirme linki")
    
    def __unicode__(self):
        return self.Title
    
    def was_published_today(self):
        return self.Pubdate.date()==datetime.date.today()
    
