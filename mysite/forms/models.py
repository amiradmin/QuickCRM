from django.db import models
# from training.models import TesCandidate

# Create your models here.

class Field(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    type = models.CharField(max_length=256, null=True, blank=True )
    label = models.CharField(max_length=256, null=True, blank=True )
    require = models.BooleanField(null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Forms(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    dbName = models.CharField(max_length=256, null=True, blank=True )
    fields = models.ManyToManyField( 'Field',null=True, blank=True )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    colorCode = models.CharField(max_length=256, null=True, blank=True )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class FormsList(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   
    
class TwiEnrolmentForm(models.Model):
    twiCandidateID = models.CharField(max_length=1024, null=True, blank=True )
    eventName = models.CharField(max_length=1024, null=True, blank=True )
    eventDate = models.DateField( null=True, blank=True )
    firstName = models.CharField(max_length=1024, null=True, blank=True )
    middleName = models.CharField(max_length=1024, null=True, blank=True )
    lastName = models.CharField(max_length=1024, null=True, blank=True )
    birthOfDate = models.DateField( null=True, blank=True )
    permanentPrivateAddress = models.CharField(max_length=2048, null=True, blank=True )
    Postcode = models.CharField(max_length=1024, null=True, blank=True )
    CarRegNo = models.CharField(max_length=1024, null=True, blank=True )
    privateTel = models.CharField(max_length=1024, null=True, blank=True )
    emergencyTel = models.CharField(max_length=1024, null=True, blank=True )
    phone = models.CharField(max_length=1024, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    correspondenceAddress = models.CharField(max_length=2048, null=True, blank=True )
    invoiceAddress = models.CharField(max_length=2048, null=True, blank=True )
    sponsoringCompanyAndaddress = models.CharField(max_length=2048, null=True, blank=True )
    sponsorPostcode = models.CharField(max_length=1024, null=True, blank=True )
    sponsorContactName = models.CharField(max_length=1024, null=True, blank=True )
    sponsorTel = models.CharField(max_length=1024, null=True, blank=True )
    sponsorFax = models.CharField(max_length=1024, null=True, blank=True )
    sponsorEmail = models.EmailField( null=True, blank=True )
    disability = models.BooleanField( null=True, blank=True )
    sponsorStatus = models.BooleanField( null=True, blank=True )
    venue = models.CharField(max_length=1024, null=True, blank=True )
    hearAbout  = models.CharField(max_length=5000, null=True, blank=True )
    GDPRstatement = models.BooleanField( null=True, blank=True )
    weldingSocietyOrTwi = models.BooleanField( null=True, blank=True )
    bookingRef= models.CharField(max_length=1024, null=True, blank=True )
    examinationType= models.CharField(max_length=1024, null=True, blank=True )
    examinationBody= models.CharField(max_length=1024, null=True, blank=True )
    
    uploadedForm = models.FileField(upload_to='uploadedForm',null=True,blank=True)
    uploadedSign = models.FileField(upload_to='uploadedForm',null=True,blank=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MainForm(models.Model):
    TYPE_CHOICES = (
    ("Standard", "Standard"),
    ("TOFD", "TOFD"),
    ("CSWIP", "CSWIP"),
    ("LRUT", "LRUT"),
   
)
    name = models.CharField(max_length=256, null=True, blank=True )
    colorCode = models.CharField(max_length=256, null=True, blank=True )
    temp = models.CharField(max_length=256, null=True, blank=True )
    category = models.CharField(choices=TYPE_CHOICES,max_length=256, null=True, blank=True )
    # tesCandidate = models.ManyToManyField(TesCandidate,null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name