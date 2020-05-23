from django.db import models
from phone_field import PhoneField


class Company_B00(models.Model):
    Company_Rec = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Address_1 = models.CharField(max_length=100)
    Address_2 = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Zip_Code = models.IntegerField()

    class Meta:
        verbose_name = 'Company'

    def __str__(self):
        return self.Company_Rec


class Insurance_B00(models.Model):
    Insurance_Rec = models.CharField(max_length=100)
    Address_1 = models.CharField(max_length=100)
    Address_2 = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Zip_Code = models.IntegerField()
    phone = PhoneField(blank=True, help_text='Contact phone number')

    class Meta:
        verbose_name = 'Insurance B00'

    def __str__(self):
        return self.Insurance_Rec


class Insurance_B01(models.Model):
    Insurance_Representative_Rec = models.CharField(max_length=200)
    Insurance_Rec = models.ForeignKey(Insurance_B00, verbose_name='Insurance Rec',
                                      on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    phone_1 = PhoneField(blank=True, help_text='Contact phone number')
    phone_2 = PhoneField(blank=True, help_text='Contact phone number')
    eMail_Address = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Insurance B01'

    def __str__(self):
        return self.Insurance_Representative_Rec
