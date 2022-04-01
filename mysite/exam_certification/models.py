from django.db import models
from django.contrib.auth.models import User
from training.models import Country,Location,TesCandidate,Product,Event
# Create your models here.





class ExamMaterialPiWiModel(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_pi_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_pi_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    exam_revision = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class Invigilator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    passport_id = models.CharField(max_length=30, null=True, blank=True )
    email = models.EmailField( null=True, blank=True )
    city = models.CharField(max_length=30,  null=True, blank=True  )
    country = models.CharField(max_length=30,  null=True, blank=True  )
    contact_number = models.CharField(max_length=30,  null=True, blank=True  )
    photo = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_1 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_2 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_3 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_4 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_5 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_6 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_7 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_8 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    document_9 = models.FileField(upload_to='lecturer_document',null=True,blank=True)
    avatar = models.FileField(upload_to='avatar',null=True,blank=True)
    note = models.TextField(max_length=2000,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + ' '+ self.user.last_name




class CertificateType(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True )
    expriation = models.IntegerField( null=True, blank=True )
    file = models.FileField(upload_to='exam_file',null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CertificateAttendance(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    authorized_signatory = models.CharField(max_length=256, null=True, blank=True )
    cer_number = models.CharField(max_length=256, null=True, blank=True )
    certiﬁcate_number = models.CharField(max_length=256, null=True, blank=True )
    course_duration = models.IntegerField( null=True, blank=True )
    event = models.ForeignKey(Event,related_name="exam_event",  null=True, blank=True , on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    type = models.ForeignKey(CertificateType,related_name="exam_type",  null=True, blank=True , on_delete=models.DO_NOTHING)
    invigilator = models.ForeignKey(Invigilator,related_name="invigilator_exam",  null=True, blank=True , on_delete=models.DO_NOTHING)
    issue_date = models.DateTimeField(null=True,blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class PcnCertificateProduct(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PcnCertificateAttendance(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    candidate = models.ForeignKey(TesCandidate,related_name="pcn_exam_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    product = models.ForeignKey(PcnCertificateProduct,related_name="pcn_exam_product",  null=True, blank=True , on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class CswipCertificateProduct(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CSWIPCertificateAttendance(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    candidate = models.ForeignKey(TesCandidate,related_name="cswip_exam_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    product = models.ForeignKey(CswipCertificateProduct,related_name="cswip_exam_product",  null=True, blank=True , on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
