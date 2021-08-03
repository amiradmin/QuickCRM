from django.db import models
from training.models import Category, TesCandidate,Event



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


    

    
class TwiEnrolmentForm(models.Model):
    eventID = models.CharField(max_length=256, null=True, blank=True )
    candidate = models.ForeignKey(TesCandidate,related_name="candidate", on_delete=models.CASCADE)
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
    weldingSociety = models.BooleanField( null=True, blank=True )
    twiEmployee = models.BooleanField( null=True, blank=True )
    bookingRef= models.CharField(max_length=1024, null=True, blank=True )
    examinationType= models.CharField(max_length=1024, null=True, blank=True )
    examinationBody= models.CharField(max_length=1024, null=True, blank=True )
    
    PCN_BGASApprovalNumber = models.CharField(max_length=1024, null=True, blank=True )
    currentCSWIPQualifications = models.CharField(max_length=1024, null=True, blank=True )
    CSWIPWeldingexamination = models.CharField(max_length=1024, null=True, blank=True )
    experience = models.CharField(max_length=1024, null=True, blank=True )
    experienceRequirements = models.CharField(max_length=4096, null=True, blank=True )
    underwaterInspectionExam = models.CharField(max_length=128, null=True, blank=True )
    NDTexamination = models.CharField(max_length=128, null=True, blank=True )
    NDTexaminationLevel = models.CharField(max_length=128, null=True, blank=True )
    NDTIndustrySector = models.CharField(max_length=128, null=True, blank=True )
    NDTexaminationCategories = models.CharField(max_length=256, null=True, blank=True )
    plantInspection  = models.CharField(max_length=256, null=True, blank=True )
    plantInspectionLevel  = models.CharField(max_length=2048, null=True, blank=True )
    plantInspectionLevel1  = models.CharField(max_length=2048, null=True, blank=True )
    plantInspectionLevel2  = models.CharField(max_length=2048, null=True, blank=True )
    plantInspectionRequirements  = models.CharField(max_length=4096, null=True, blank=True )
    otherExaminations  = models.CharField(max_length=1024, null=True, blank=True )
    otherExaminationsTitleRequired  = models.CharField(max_length=1024, null=True, blank=True )
    VerifierName  = models.CharField(max_length=512, null=True, blank=True )
    VerifierCompanyPosition  = models.CharField(max_length=512, null=True, blank=True )
    VerifierProfessionalRelation  = models.CharField(max_length=512, null=True, blank=True )
    VerifierTelephone = models.CharField(max_length=512, null=True, blank=True )
    VerifierEmail = models.CharField(max_length=512, null=True, blank=True )
    VerifierDate = models.DateField( null=True, blank=True )
    confirmation = models.BooleanField( null=True, blank=True )
    
    uploadedForm = models.FileField(upload_to='uploadedForm',null=True,blank=True)
    uploadedSign = models.FileField(upload_to='uploadedForm',null=True,blank=True)
    uploadedVerifierSign = models.FileField(upload_to='uploadedForm',null=True,blank=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lastName



class BGAsExperienceForm(models.Model):

    eventID = models.CharField(max_length=256, null=True, blank=True )
    candidate = models.ForeignKey(TesCandidate,related_name="bgas_candidate", on_delete=models.CASCADE)
    twiCandidateID = models.CharField(max_length=1024, null=True, blank=True )
    eventName = models.CharField(max_length=1024, null=True, blank=True )
    eventDate = models.DateField( null=True, blank=True )
    firstName = models.CharField(max_length=1024, null=True, blank=True )
    middleName = models.CharField(max_length=1024, null=True, blank=True )
    lastName = models.CharField(max_length=1024, null=True, blank=True )
    birthOfDate = models.DateField( null=True, blank=True )
    confirmation = models.BooleanField( null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lastName

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

class General(models.Model):

    event = models.ForeignKey(Event,related_name="general_event", on_delete=models.CASCADE)
    formCategory = models.ForeignKey(Category,related_name="form_category_training", on_delete=models.CASCADE)
    twiEnrolmentForm = models.ManyToManyField('TwiEnrolmentForm',  null=True, blank=True)
    bgasExperienceForm =models.ManyToManyField('BGAsExperienceForm',  null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name