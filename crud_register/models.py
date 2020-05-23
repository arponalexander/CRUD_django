from django.db import models
from phone_field import PhoneField


class Company_B00(models.Model):
    company_Rec = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_Code = models.IntegerField()
    active_status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Company'

    def __str__(self):
        return self.company_Rec


class Insurance_B00(models.Model):
    insurance_Rec = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_Code = models.IntegerField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.insurance_Rec


class Insurance_B01(models.Model):
    insurance_Representative_Rec = models.CharField(max_length=200)
    insurance_Rec = models.ForeignKey(Insurance_B00,
                                      on_delete=models.CASCADE)
    first_Name = models.CharField(max_length=200)
    last_Name = models.CharField(max_length=200)
    phone_1 = PhoneField(blank=True, help_text='Contact phone number')
    phone_2 = PhoneField(blank=True, help_text='Contact phone number')
    eMail_Address = models.CharField(max_length=200)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.insurance_Representative_Rec
