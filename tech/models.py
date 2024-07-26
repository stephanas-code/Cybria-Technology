from django.db import models

# Create your models here.
Skills = (
        ('Front-End Development, 6 months, ₦45,000','Front-End Development, 6 months, ₦45,000'),
        ('Back-End Development, 6 months, ₦50,000','Back-End Development, 6 months, ₦50,000'),
        ('Full-Stack Development, 12 months, ₦85,000','Full-Stack Development, 12 months, ₦85,000'),
        ('Computer Hardware Engineering, 9 months, ₦60,000','Computer Hardware Engineering, 9 months, ₦60,000'),
        ('Data Analysis, 8 months, ₦70,000','Data Analysis, 8 months, ₦70,000'),
    )

    
class Becomeadeveloper(models.Model):
    firstname = models.CharField(max_length=100)
    lastname  = models.CharField(max_length=100)
    email     = models.EmailField()
    phone     = models.CharField(max_length=100)
    skills    = models.CharField(max_length =50 , choices=Skills, default="Front-End Development, 6 months, ₦45,000")


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    subject  = models.CharField(max_length=100)
    email     = models.EmailField()
    message     = models.CharField(max_length=300)
   