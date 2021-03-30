from django.db import models


# class SuggestionForm(models.Model):
#     number = models.IntegerField(verbose_name="شماره")
#     issued_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="تاریخ")
#     deanship = models.CharField(max_length=100, verbose_name="مقام مربوطه")
#     department = models.CharField(max_length=100, verbose_name="ریاست مربوطه")
#     topic = models.CharField(max_length=100, verbose_name="موضوغ")
#     description = models.TextField(verbose_name="توضحات")
#     dean = models.CharField(max_length=30, verbose_name="اسم ریس")
#     dean_commandment = models.TextField(verbose_name="حکم ریس")
#     addminstartion_commandment = models.TextField(verbose_name="حکم بخش اداری")
#     advice_commitee = models.TextField(verbose_name="نظر هیت")
#     addminstration_final = models.TextField(verbose_name="اجرات بخش اداری")

class Well(models.Model):
    well_id = models.CharField(max_length=20)
    well_type = models.CharField(max_length=30)
    depth = models.IntegerField()
    y = models.IntegerField()
    x = models.IntegerField()
    provence = models.CharField(max_length=15)  #choiceable 
    owener = models.CharField(max_length=15)    #choiceavle ???
    address = models.CharField(max_length=100)


class Monitor(models.Model):
    well = models.ForeignKey(Well, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    EC_us_cm = models.IntegerField()
    temprature = models.IntegerField()
    PH = models.IntegerField()
    salinity = models.IntegerField()
    TDS_mg_lit = models.IntegerField()

    
