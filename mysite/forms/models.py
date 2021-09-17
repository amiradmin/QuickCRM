from django.db import models
from training.models import Category, TesCandidate,Event,Product,FormsList as Guideline



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


class FormList(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    candidate = models.ForeignKey(TesCandidate, related_name="candidate_form", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="event_form", on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, related_name="category_form", on_delete=models.CASCADE, null=True, blank=True)
    guideline = models.ForeignKey(Guideline, related_name="guideline_form", on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, related_name="event_form", on_delete=models.CASCADE, null=True, blank=True)
    FormID = models.CharField(max_length=128, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

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
    otherExaminationsTitle  = models.CharField(max_length=1024, null=True, blank=True )
    VerifierName  = models.CharField(max_length=512, null=True, blank=True )
    VerifierCompanyPosition  = models.CharField(max_length=512, null=True, blank=True )
    VerifierProfessionalRelation  = models.CharField(max_length=512, null=True, blank=True )
    VerifierTelephone = models.CharField(max_length=512, null=True, blank=True )
    VerifierEmail = models.CharField(max_length=512, null=True, blank=True )
    VerifierDate = models.DateField( null=True, blank=True )
    confirmation = models.BooleanField( null=True, blank=True )
    confirmation = models.BooleanField(null=True, blank=True)
    
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
    PreCertificationExperience = models.CharField(max_length=4096, null=True, blank=True )
    VerifierName  = models.CharField(max_length=512, null=True, blank=True )
    VerifierCompany  = models.CharField(max_length=512, null=True, blank=True )
    VerifierPosition = models.CharField(max_length=512, null=True, blank=True )
    VerifierTelephone = models.CharField(max_length=512, null=True, blank=True )
    VerifierEmail = models.CharField(max_length=512, null=True, blank=True )
    VerifierDate = models.DateField( null=True, blank=True )
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

class NdtTechnique(models.Model):

    candidate = models.ForeignKey(TesCandidate, related_name="ndt_technice_candidate", on_delete=models.CASCADE)
    techniqueCode = models.CharField(max_length=2048, null=True, blank=True )
    employerComponent = models.CharField(max_length=2048, null=True, blank=True )
    ndtTask = models.CharField(max_length=2048, null=True, blank=True )
    experienceHours = models.CharField(max_length=2048, null=True, blank=True )
    experienceConfirmed  = models.CharField(max_length=2048, null=True, blank=True )


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.techniqueCode

class PSL30LogExp(models.Model):

    event = models.ForeignKey(Event, related_name="osl_event", on_delete=models.CASCADE)
    candidate = models.ForeignKey(TesCandidate,related_name="psl_candidate", on_delete=models.CASCADE)
    fullName = models.CharField(max_length=1024, null=True, blank=True )
    pslNumber = models.CharField(max_length=1024, null=True, blank=True )
    ndtMethod = models.CharField(max_length=1024, null=True, blank=True )
    employingOrganisation = models.CharField(max_length=1024, null=True, blank=True )
    reviewerName = models.CharField(max_length=1024, null=True, blank=True )
    finalEmployerDeclarationName = models.CharField(max_length=1024, null=True, blank=True )
    dateCandidateDeclaration = models.DateField( null=True, blank=True )
    reviewerDate = models.DateField( null=True, blank=True )
    dateFrom = models.DateField( null=True, blank=True )
    dateTo = models.DateField( null=True, blank=True )
    ndtTechnique = models.ManyToManyField('NdtTechnique', null=True, blank=True)
    confirmation = models.BooleanField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName


class PSL30InitialForm(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Femail')
        ]

    event = models.ForeignKey(Event, related_name="initial_event", on_delete=models.CASCADE)
    candidate = models.ForeignKey(TesCandidate,related_name="initial_candidate", on_delete=models.CASCADE)
    cerAddres = models.CharField(max_length=2048, null=True, blank=True )
    pslCerAddres = models.CharField(max_length=2048, null=True, blank=True )
    phone = models.CharField(max_length=256, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, null=True, blank=True)
    pslNumber = models.CharField(max_length=1024, null=True, blank=True )
    birthDay = models.DateField(null=True, blank=True)
    currentEmploymentDetails = models.CharField(max_length=2048, null=True, blank=True)
    currentEmploymentPosition = models.CharField(max_length=1024, null=True, blank=True)
    currentEmploymentStatus = models.CharField(max_length=512, null=True, blank=True)
    preCerTraining = models.CharField(max_length=2048, null=True, blank=True)
    preCerTrainingDate = models.CharField(max_length=512, null=True, blank=True)
    productInductory = models.CharField(max_length=512, null=True, blank=True)
    ndtMethod = models.CharField(max_length=512, null=True, blank=True)
    level = models.CharField(max_length=512, null=True, blank=True)
    level3State = models.CharField(max_length=512, null=True, blank=True)
    basicRadiationSafty = models.CharField(max_length=512, null=True, blank=True)
    radiationProtectionSupervisor = models.CharField( max_length=512,null=True, blank=True)
    cerCategory = models.CharField(max_length=512, null=True, blank=True)
    preferredExaminationDateVenue = models.CharField(max_length=1024, null=True, blank=True)
    ndtDuration = models.CharField(max_length=1024, null=True, blank=True)
    expVerifierDetails = models.CharField(max_length=1024, null=True, blank=True)
    candidateEligibilityName = models.CharField(max_length=512, null=True, blank=True)
    candidateEligibilityDate = models.DateField( null=True, blank=True)
    sponsorName = models.CharField(max_length=512, null=True, blank=True)
    sponsorCompany = models.CharField(max_length=512, null=True, blank=True)
    sponsorCompany = models.CharField(max_length=512, null=True, blank=True)
    sponsorTelephone = models.CharField(max_length=512, null=True, blank=True)
    examDate = models.DateField(null=True, blank=True)
    examinerName = models.CharField(max_length=512, null=True, blank=True)
    examinerVenue = models.CharField(max_length=512, null=True, blank=True)
    moderator = models.CharField(max_length=512, null=True, blank=True)
    paymentRecieved = models.CharField(max_length=512, null=True, blank=True)
    resultReference = models.CharField(max_length=512, null=True, blank=True)
    examCloseDate = models.DateField(null=True, blank=True)

    confirmation = models.BooleanField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class CurrentFormerCertification(models.Model):
    methodLevel = models.CharField(max_length=512, null=True, blank=True)
    SchemeCertifyingAuthority = models.CharField(max_length=512, null=True, blank=True)
    ExpiryDate = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.methodLevel

class ExperienceClaimed(models.Model):
    methodLevel = models.CharField(max_length=512, null=True, blank=True)
    ExperienceClaimedSince = models.CharField(max_length=512, null=True, blank=True)
    NumberOfNonths = models.IntegerField( null=True, blank=True)
    DateOfExamination = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.methodLevel

class NDT15AExperienceVerification(models.Model):
    event = models.ForeignKey(Event, related_name="event_ndt", on_delete=models.CASCADE)
    candidate = models.ForeignKey(TesCandidate, related_name="candidate_ndt", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="category_ndt", on_delete=models.CASCADE)
    guideline = models.ForeignKey(Guideline, related_name="guideline_ndt", on_delete=models.CASCADE)
    candidateID = models.CharField(max_length=512, null=True, blank=True)
    currentFormerCertification = models.ManyToManyField('CurrentFormerCertification', null=True, blank=True)
    experienceClaimed = models.ManyToManyField('ExperienceClaimed', null=True, blank=True)
    descriptionOfExperience = models.CharField(max_length=512, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    nameJobTitle =  models.CharField(max_length=512, null=True, blank=True)
    companyName =  models.CharField(max_length=512, null=True, blank=True)
    supervisionActivity =  models.CharField(max_length=512, null=True, blank=True)
    verEmail =  models.EmailField(null=True, blank=True)
    verDate = models.DateField(null=True, blank=True)

    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.last_name



class NDTCovid19(models.Model):
    event = models.ForeignKey(Event, related_name="event_ndt_covid19", on_delete=models.CASCADE)
    candidate = models.ForeignKey(TesCandidate, related_name="candidate_ndt_covid19", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="category_ndt_covid19", on_delete=models.CASCADE)
    guideline = models.ForeignKey(Guideline, related_name="guideline_ndt_covid19", on_delete=models.CASCADE)
    candidateID = models.CharField(max_length=512, null=True, blank=True)
    candidateAdress = models.CharField(max_length=512, null=True, blank=True)
    candidateHomePhone = models.CharField(max_length=512, null=True, blank=True)
    fillingDate = models.DateField(null=True, blank=True)

    confirmCase1 = models.BooleanField(null=True, blank=True)
    confirmCase2 = models.BooleanField(null=True, blank=True)
    confirmCase3 = models.BooleanField(null=True, blank=True)
    confirmCase4 = models.BooleanField(null=True, blank=True)
    confirmCase5 = models.BooleanField(null=True, blank=True)
    confirmCase6 = models.BooleanField(null=True, blank=True)

    medicalTravelCase1 = models.BooleanField(null=True, blank=True)
    medicalHistory =models.CharField(max_length=512, null=True, blank=True)
    medicalTravelCase2 = models.BooleanField(null=True, blank=True)
    temperature = models.CharField(max_length=512, null=True, blank=True)
    medicalTravelCase3 = models.BooleanField(null=True, blank=True)
    medicalTravelCase4 = models.BooleanField(null=True, blank=True)

    afterEventDate = models.DateField(null=True, blank=True)
    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.last_name


class PSL57B(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Femail')
        ]

    event = models.ForeignKey(Event, related_name="event_psl_57b", on_delete=models.CASCADE)
    candidate = models.ForeignKey(TesCandidate, related_name="candidate_psl_57b", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="category_psl_57b", on_delete=models.CASCADE)
    guideline = models.ForeignKey(Guideline, related_name="guideline_psl_57b", on_delete=models.CASCADE)
    contactMe = models.BooleanField(null=True, blank=True)
    cerAddress = models.CharField(max_length=2048, null=True, blank=True )
    pslCerAddress = models.CharField(max_length=2048, null=True, blank=True )
    phone = models.CharField(max_length=256, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, null=True, blank=True)
    pslNumber = models.CharField(max_length=1024, null=True, blank=True )
    birthDay = models.DateField(null=True, blank=True)


    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.last_name
