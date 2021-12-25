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
    candidate = models.ForeignKey(TesCandidate, related_name="candidate_form", on_delete=models.CASCADE, null=True, blank=True)
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
    candidate = models.ForeignKey(TesCandidate,related_name="candidate", on_delete=models.CASCADE, null=True, blank=True )
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
    sponsorCcmpany = models.CharField(max_length=512, null=True, blank=True)
    sponsorName = models.CharField(max_length=512, null=True, blank=True)
    sponsorAddress = models.CharField(max_length=512, null=True, blank=True)
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
    totalHours = models.IntegerField(max_length=1024, null=True, blank=True )
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

    # def __str__(self):
    #     return self.candidate.first_name


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
    employeer = models.CharField(max_length=512, null=True, blank=True)
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
    outsideCountry = models.CharField(max_length=1024, null=True, blank=True)
    medicalTravelCase4 = models.BooleanField(null=True, blank=True)

    afterEventDate = models.DateField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.last_name


class empHistory(models.Model):
    organisation = models.CharField(max_length=512, null=True, blank=True)
    period = models.CharField(max_length=512, null=True, blank=True)
    contactNamePhone = models.CharField(max_length=512, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.organisation


class PSL57A(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
        ]

    event = models.ForeignKey(Event, related_name="event_psl_57a", on_delete=models.CASCADE)
    candidate = models.ForeignKey(TesCandidate, related_name="candidate_psl_57a", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="category_psl_57a", on_delete=models.CASCADE, null=True, blank=True )
    guideline = models.ForeignKey(Guideline, related_name="guideline_psl_57a", on_delete=models.CASCADE, null=True, blank=True )
    contactMe = models.BooleanField(null=True, blank=True)
    cerAddress = models.CharField(max_length=2048, null=True, blank=True )
    pslCerAddress = models.CharField(max_length=2048, null=True, blank=True )
    phone = models.CharField(max_length=256, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, null=True, blank=True)
    pclNumber = models.CharField(max_length=1024, null=True, blank=True )
    birthDay = models.DateField(null=True, blank=True)
    emphistory = models.ManyToManyField(empHistory, null=True, blank=True)
    currentEmploymentDetails = models.CharField(max_length=1024, null=True, blank=True)
    candidatePosition = models.CharField(max_length=512, null=True, blank=True)
    employmentStatus  = models.CharField(max_length=512, null=True, blank=True)
    examinationType   = models.CharField(max_length=512, null=True, blank=True)
    trainingOrg   = models.CharField(max_length=512, null=True, blank=True)
    dateOfCourse = models.DateField(null=True, blank=True)
    iroductsIndustrySector = models.CharField(max_length=1024, null=True, blank=True)
    NDTMethod    = models.CharField(max_length=256, null=True, blank=True)
    NDTLevel    = models.CharField(max_length=256, null=True, blank=True)
    ifLevel3    = models.CharField(max_length=256, null=True, blank=True)
    radiationSafety    = models.CharField(max_length=256, null=True, blank=True)
    radiationProtectionSup    = models.CharField(max_length=256, null=True, blank=True)
    categoriesOfCertification = models.CharField(max_length=256, null=True, blank=True)
    preferredExaminationDateVenu = models.CharField(max_length=1024, null=True, blank=True)
    claimDuration = models.CharField(max_length=256, null=True, blank=True)
    verClaimAddress = models.CharField(max_length=1024, null=True, blank=True)
    dateOfSign = models.DateField(null=True, blank=True)
    sponsorName = models.CharField(max_length=256, null=True, blank=True)
    sponsorCompany = models.CharField(max_length=256, null=True, blank=True)
    sponsorPhone = models.CharField(max_length=256, null=True, blank=True)
    sponsorSign = models.CharField(max_length=256, null=True, blank=True)
    testCenterExamDate = models.DateField(null=True, blank=True)
    testCenterVenue = models.CharField(max_length=256, null=True, blank=True)
    testCenterExaminer = models.CharField(max_length=256, null=True, blank=True)
    testCenterModerator = models.CharField(max_length=256, null=True, blank=True)
    testCenterPaymentReceived = models.CharField(max_length=256, null=True, blank=True)
    testCenterResultRef = models.CharField(max_length=256, null=True, blank=True)
    testCenterExamCompleteColsed = models.CharField(max_length=256, null=True, blank=True)
    nameAddressInvoice = models.CharField(max_length=1024, null=True, blank=True)
    accommodation = models.CharField(max_length=1024, null=True, blank=True)
    paymentMethod = models.CharField(max_length=1024, null=True, blank=True)
    cheque = models.BooleanField(null=True, blank=True)
    nameResponsible = models.CharField(max_length=256, null=True, blank=True)
    companyOrderReference = models.CharField(max_length=1024, null=True, blank=True)
    creditCardPayment = models.CharField(max_length=256, null=True, blank=True)
    issueExpiryDates = models.DateField(null=True, blank=True)
    NameOnCard = models.CharField(max_length=256, null=True, blank=True)
    cardNumber = models.CharField(max_length=256, null=True, blank=True)
    securityCode  = models.CharField(max_length=256, null=True, blank=True)
    addressCreditCardHolder = models.CharField(max_length=256, null=True, blank=True)
    debit = models.CharField(max_length=256, null=True, blank=True)





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
    pclNumber = models.CharField(max_length=1024, null=True, blank=True )
    birthDay = models.DateField(null=True, blank=True)
    emphistory = models.ManyToManyField(empHistory, null=True, blank=True)
    currentEmploymentDetails = models.CharField(max_length=1024, null=True, blank=True)
    candidatePosition = models.CharField(max_length=512, null=True, blank=True)
    employmentStatus  = models.CharField(max_length=512, null=True, blank=True)
    examinationType   = models.CharField(max_length=512, null=True, blank=True)
    iroductsIndustrySector    = models.CharField(max_length=1024, null=True, blank=True)
    NDTMethod    = models.CharField(max_length=256, null=True, blank=True)
    NDTLevel    = models.CharField(max_length=256, null=True, blank=True)
    ifLevel3    = models.CharField(max_length=256, null=True, blank=True)
    categoriesOfCertification = models.CharField(max_length=256, null=True, blank=True)
    recertification = models.CharField(max_length=1024, null=True, blank=True)
    preferredExaminationDateVenu = models.CharField(max_length=1024, null=True, blank=True)
    nameAddressInvoice = models.CharField(max_length=1024, null=True, blank=True)
    accommodation = models.CharField(max_length=1024, null=True, blank=True)
    paymentMethod = models.CharField(max_length=1024, null=True, blank=True)
    cheque = models.BooleanField(null=True, blank=True)
    nameResponsible = models.CharField(max_length=256, null=True, blank=True)
    companyOrderReference = models.CharField(max_length=1024, null=True, blank=True)
    creditCardPayment = models.CharField(max_length=256, null=True, blank=True)
    issueExpiryDates = models.DateField(null=True, blank=True)
    NameOnCard = models.CharField(max_length=256, null=True, blank=True)
    cardNumber = models.CharField(max_length=256, null=True, blank=True)
    securityCode  = models.CharField(max_length=256, null=True, blank=True)
    addressCreditCardHolder = models.CharField(max_length=256, null=True, blank=True)
    debit = models.CharField(max_length=256, null=True, blank=True)


    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.last_name



class VisionTest(models.Model):

    event = models.ForeignKey(Event, related_name="event_vision_test", on_delete=models.CASCADE)
    candidate = models.ForeignKey(TesCandidate, related_name="candidate_vision_test", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="category_vision_test", on_delete=models.CASCADE)
    guideline = models.ForeignKey(Guideline, related_name="guideline_vision_test", on_delete=models.CASCADE)
    address = models.CharField(max_length=2048, null=True, blank=True )
    address = models.CharField(max_length=2048, null=True, blank=True )
    phone = models.CharField(max_length=256, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    birthDay = models.DateField(null=True, blank=True)
    employer = models.CharField(max_length=2048, null=True, blank=True)
    nearVisionAcuity = models.CharField(max_length=2048, null=True, blank=True)
    colourPerception = models.CharField(max_length=2048, null=True, blank=True)
    shadesOfGrey = models.CharField(max_length=2048, null=True, blank=True)
    tumbling = models.CharField(max_length=2048, null=True, blank=True)
    recognisedOrganisation = models.CharField(max_length=2048, null=True, blank=True)
    recognisedName = models.CharField(max_length=2048, null=True, blank=True)
    recognisedPhone = models.CharField(max_length=2048, null=True, blank=True)
    recognisedLicenceNumber = models.CharField(max_length=2048, null=True, blank=True)
    recognisedDate = models.DateField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)


    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.last_name


class TesFrmCandidate(models.Model):

    candidate = models.ForeignKey(TesCandidate, related_name="tes_frm_candidate", on_delete=models.CASCADE)
    testSequence= models.CharField(max_length=1024, null=True, blank=True)
    scheme= models.CharField(max_length=1024, null=True, blank=True)
    methodOfExam= models.CharField(max_length=1024, null=True, blank=True)
    # methodOfExam= models.CharField(max_length=1024, null=True, blank=True)
    remark= models.CharField(max_length=1024, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.last_name




class TesFrmExaminationAttendance(models.Model):
    examTitleCode= models.CharField(max_length=2048, null=True, blank=True)
    venue= models.CharField(max_length=2048, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    invigilatorName = models.CharField(max_length=2048, null=True, blank=True)
    tesFrmCandidate = models.ManyToManyField(TesFrmCandidate, null=True, blank=True)


    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.examTitleCode


class TesLecFeedbackFrom(models.Model):
    courseName= models.ForeignKey(Event, related_name="feed_form_event", on_delete=models.CASCADE)
    lecturerName= models.CharField(max_length=512, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=512, null=True, blank=True)
    candidate = models.ForeignKey(TesCandidate, related_name="feed_form_candidate", on_delete=models.CASCADE)

    knowledge = models.IntegerField( null=True, blank=True)
    knowledgeComment = models.CharField(max_length=2048, null=True, blank=True)

    teachingMethod  = models.IntegerField( null=True, blank=True)
    teachingMethodComment = models.CharField(max_length=2048, null=True, blank=True)


    abilityToAnswer   = models.IntegerField( null=True, blank=True)
    abilityToAnswerComment = models.CharField(max_length=2048, null=True, blank=True)

    usefulExample   = models.IntegerField( null=True, blank=True)
    usefulExampleComment = models.CharField(max_length=2048, null=True, blank=True)

    industrialExperience   = models.IntegerField( null=True, blank=True)
    industrialExperienceComment = models.CharField(max_length=2048, null=True, blank=True)

    appropriateAids   = models.IntegerField( null=True, blank=True)
    appropriateAidsComment = models.CharField(max_length=2048, null=True, blank=True)

    transposition   = models.IntegerField( null=True, blank=True)
    transpositionComment = models.CharField(max_length=2048, null=True, blank=True)

    participantsAttraction   = models.IntegerField( null=True, blank=True)
    participantsAttractionComment = models.CharField(max_length=2048, null=True, blank=True)

    ControllingTheClass   = models.IntegerField( null=True, blank=True)
    ControllingTheClassComment = models.CharField(max_length=2048, null=True, blank=True)

    punctuality   = models.IntegerField( null=True, blank=True)
    punctualityComment = models.CharField(max_length=2048, null=True, blank=True)

    generalBehaviour   = models.IntegerField( null=True, blank=True)
    generalBehaviourComment = models.CharField(max_length=2048, null=True, blank=True)

    anyComments = models.CharField(max_length=4092, null=True, blank=True)



    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.courseName.name



class TesAttCandidate(models.Model):

    candidate = models.ForeignKey(TesCandidate, related_name="tes_att_candidate", on_delete=models.CASCADE)
    testSequence= models.CharField(max_length=1024, null=True, blank=True)

    dayOneSec1= models.BooleanField( null=True, blank=True)
    dayOneSec2= models.BooleanField( null=True, blank=True)
    dayOneSec3= models.BooleanField( null=True, blank=True)
    dayOneSec4= models.BooleanField( null=True, blank=True)


    dayTwoSec1= models.BooleanField( null=True, blank=True)
    dayTwoSec2= models.BooleanField( null=True, blank=True)
    dayTwoSec3= models.BooleanField( null=True, blank=True)
    dayTwoSec4= models.BooleanField( null=True, blank=True)

    dayThreeSec1= models.BooleanField( null=True, blank=True)
    dayThreeSec2= models.BooleanField( null=True, blank=True)
    dayThreeSec3= models.BooleanField( null=True, blank=True)
    dayThreeSec4= models.BooleanField( null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.last_name



class TrainingAttendance(models.Model):
    event = models.ForeignKey(Event, related_name="event_att_train", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="category_att_train", on_delete=models.CASCADE)
    guideline = models.ForeignKey(Guideline, related_name="guideline_att_train", on_delete=models.CASCADE)
    examTitleCode= models.CharField(max_length=2048, null=True, blank=True)
    venue= models.CharField(max_length=2048, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    lecturerName = models.CharField(max_length=2048, null=True, blank=True)
    attCandidate = models.ManyToManyField(TesAttCandidate, null=True, blank=True)

    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.examTitleCode


class TwiTrainingFeedback(models.Model):
    candidate = models.ForeignKey(TesCandidate, related_name="twi_training_candidate", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="twi_training_event", on_delete=models.CASCADE)
    region= models.CharField(max_length=2048, null=True, blank=True)
    venue= models.CharField(max_length=2048, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    lecturerName = models.CharField(max_length=2048, null=True, blank=True)
    programme = models.CharField(max_length=2048, null=True, blank=True)

    bookingProcess = models.CharField(max_length=2048, null=True, blank=True)
    joiningInstructions = models.CharField(max_length=2048, null=True, blank=True)
    trainingEnvironment = models.CharField(max_length=2048, null=True, blank=True)
    objectivesCourse = models.CharField(max_length=2048, null=True, blank=True)
    tutorLecturer  = models.CharField(max_length=2048, null=True, blank=True)
    principlesExplained  = models.CharField(max_length=2048, null=True, blank=True)
    questionsAnswered  = models.CharField(max_length=2048, null=True, blank=True)
    audience  = models.CharField(max_length=2048, null=True, blank=True)
    atmosphere  = models.CharField(max_length=2048, null=True, blank=True)
    practicalSessions  = models.CharField(max_length=2048, null=True, blank=True)
    notes  = models.CharField(max_length=2048, null=True, blank=True)
    equipment  = models.CharField(max_length=2048, null=True, blank=True)
    overallQuality  = models.CharField(max_length=2048, null=True, blank=True)
    expectations  = models.CharField(max_length=2048, null=True, blank=True)

    howWeDid  = models.CharField(max_length=9042, null=True, blank=True)
    email  = models.EmailField( null=True, blank=True)
    penetrantTesting = models.BooleanField(null=True, blank=True)
    magneticTesting = models.BooleanField(null=True, blank=True)
    radioTesting = models.BooleanField(null=True, blank=True)
    radioIntro = models.BooleanField(null=True, blank=True)
    ultrasonicTesting = models.BooleanField(null=True, blank=True)
    eddyCurrentTesting = models.BooleanField(null=True, blank=True)
    timeFlightDiffraction = models.BooleanField(null=True, blank=True)
    phasedArrayUltrasonic = models.BooleanField(null=True, blank=True)
    ACFM = models.BooleanField(null=True, blank=True)
    digitalComputedRadiography = models.BooleanField(null=True, blank=True)
    automatedUltrasonicTesting  = models.BooleanField(null=True, blank=True)
    pulsedEddyCurrent  = models.BooleanField(null=True, blank=True)
    appreciationBasicNDTMethod  = models.BooleanField(null=True, blank=True)
    appreciationAdvancedNDTmethods  = models.BooleanField(null=True, blank=True)
    cathodicProtection  = models.BooleanField(null=True, blank=True)

    introNDT  = models.BooleanField(null=True, blank=True)
    visualWeldingInspection  = models.BooleanField(null=True, blank=True)
    weldingInspection  = models.BooleanField(null=True, blank=True)
    seniorWeldingInspection  = models.BooleanField(null=True, blank=True)
    weldingQuality  = models.BooleanField(null=True, blank=True)
    partialWelder  = models.BooleanField(null=True, blank=True)
    introASME  = models.BooleanField(null=True, blank=True)
    introErupeanStandard  = models.BooleanField(null=True, blank=True)
    reviewAsmeXI  = models.BooleanField(null=True, blank=True)
    siteCoating  = models.BooleanField(null=True, blank=True)
    paitingInspector  = models.BooleanField(null=True, blank=True)
    weldingInspector  = models.BooleanField(null=True, blank=True)
    IIWDiploma  = models.BooleanField(null=True, blank=True)
    plantInspector  = models.BooleanField(null=True, blank=True)
    underWater  = models.BooleanField(null=True, blank=True)


    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.first_name




class TwiExamFeedback(models.Model):
    candidate = models.ForeignKey(TesCandidate, related_name="twi_examg_candidate", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="twi_texam_event", on_delete=models.CASCADE)
    region= models.CharField(max_length=2048, null=True, blank=True)
    venue= models.CharField(max_length=2048, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    invigilator = models.CharField(max_length=2048, null=True, blank=True)
    programme = models.CharField(max_length=2048, null=True, blank=True)

    administrativeStaff = models.CharField(max_length=2048, null=True, blank=True)
    examinationRoom = models.CharField(max_length=2048, null=True, blank=True)
    feltComfortable = models.CharField(max_length=2048, null=True, blank=True)
    explanationInvigilator = models.CharField(max_length=2048, null=True, blank=True)
    writtenExamination  = models.CharField(max_length=2048, null=True, blank=True)
    courseContent  = models.CharField(max_length=2048, null=True, blank=True)
    equipment  = models.CharField(max_length=2048, null=True, blank=True)
    samples  = models.CharField(max_length=2048, null=True, blank=True)
    reflection  = models.CharField(max_length=2048, null=True, blank=True)
    practicalSamples  = models.CharField(max_length=2048, null=True, blank=True)
    recommend  = models.CharField(max_length=2048, null=True, blank=True)
    comparisonTo  = models.CharField(max_length=2048, null=True, blank=True)
    afterYourExperience  = models.CharField(max_length=2048, null=True, blank=True)
    catering  = models.CharField(max_length=2048, null=True, blank=True)
    howWeDid  = models.CharField(max_length=4092, null=True, blank=True)
    candidateOpinion  = models.CharField(max_length=4092, null=True, blank=True)


    confirmation = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidate.first_name