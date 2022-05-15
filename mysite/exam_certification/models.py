from django.db import models
from django.contrib.auth.models import User
from training.models import Country,Location,TesCandidate,Product,Event
# Create your models here.



class Samples(models.Model):
    serial_no = models.CharField(max_length=256, null=True, blank=True )
    asset_code = models.CharField(max_length=256, null=True, blank=True)
    size = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial_no


class ExamMaterialPhasedArrayUltrasonicTesting_TOFD_Level2PCN(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_ultra_event_tofd_pcn", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_ultra_candidate_tofd_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample = models.ForeignKey(Samples,related_name="exam_material_ultra_sample_tofd_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)

    sample1_collection = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample1_collection_tofd_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample2_collection = models.ForeignKey(Samples, related_name="exam_material_ultera_sample_gsample2_collection_tofd_pcn",
                                           null=True, blank=True, on_delete=models.DO_NOTHING)
    sample1_analysis = models.CharField(max_length=256, null=True, blank=True)
    sample2_analysis = models.CharField(max_length=256, null=True, blank=True)
    sample3_analysis = models.CharField(max_length=256, null=True, blank=True)
    sample4_analysis = models.CharField(max_length=256, null=True, blank=True)
    sample5_analysis = models.CharField(max_length=256, null=True, blank=True)
    written_instruction = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_written_tofd_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)


    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class Exam_Result_PhasedArrayUltrasonicTesting_TOFD_Level2PCN(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_result_ultra_event_tofd_pcn", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_result_ultra_candidate_tofd_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample = models.ForeignKey(Samples,related_name="exam_result_ultra_sample_tofd_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)

    sample1_collection =  models.CharField(max_length=256, null=True, blank=True)
    sample2_collection = models.CharField(max_length=256, null=True, blank=True)

    sample1_analysis = models.CharField(max_length=256, null=True, blank=True)
    sample2_analysis = models.CharField(max_length=256, null=True, blank=True)

    sample3_analysis = models.CharField(max_length=256, null=True, blank=True)
    sample4_analysis = models.CharField(max_length=256, null=True, blank=True)
    sample5_analysis = models.CharField(max_length=256, null=True, blank=True)
    written_instruction = models.CharField(max_length=256, null=True, blank=True)


    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name

class DigitalRadiographicInterpretationDRI_Level2_Material(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="dri_event1", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="dri_candidate1",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    general_practical = models.ForeignKey(Samples,related_name="exam_general_practical_dri",  null=True, blank=True , on_delete=models.DO_NOTHING)
    data_analysis1 = models.ForeignKey(Samples,related_name="exam_material_data_analysis1",  null=True, blank=True , on_delete=models.DO_NOTHING)
    data_analysis2 = models.ForeignKey(Samples,related_name="exam_material_data_analysis2",  null=True, blank=True , on_delete=models.DO_NOTHING)
    data_analysis3 = models.ForeignKey(Samples,related_name="exam_material_data_analysis3",  null=True, blank=True , on_delete=models.DO_NOTHING)
    data_analysis4 = models.ForeignKey(Samples,related_name="exam_material_data_analysis4",  null=True, blank=True , on_delete=models.DO_NOTHING)
    data_analysis5 = models.ForeignKey(Samples,related_name="exam_material_data_analysis5",  null=True, blank=True , on_delete=models.DO_NOTHING)
    data_analysis6 = models.ForeignKey(Samples,related_name="exam_material_data_analysis6",  null=True, blank=True , on_delete=models.DO_NOTHING)
    general_theory = models.ForeignKey(Samples,related_name="exam_material_dri",  null=True, blank=True , on_delete=models.DO_NOTHING)
    specific_theory = models.ForeignKey(Samples,related_name="exam_material_specific_dri",  null=True, blank=True , on_delete=models.DO_NOTHING)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class DigitalRadiographicInterpretationDRI_Level2_Material3(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="dri_event13", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="dri_candidate13",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    general_practical = models.CharField(max_length=256, null=True, blank=True)
    data_analysis1 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis2 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis3 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis4 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis5 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis6 = models.CharField(max_length=256, null=True, blank=True)
    general_theory = models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class DigitalRadiographicInterpretationDRI_Level2_Result(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="dri_event1_result", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="dri_candidate1_result",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    general_practical = models.CharField(max_length=256, null=True, blank=True)
    data_analysis1 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis2 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis3 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis4 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis5 = models.CharField(max_length=256, null=True, blank=True)
    data_analysis6 = models.CharField(max_length=256, null=True, blank=True)
    general_theory = models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name

class TimeFlightDiffractionTOFDLevel3_PCN_Material(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="pcn_material_phased_Array_l3_event1", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="pcn_material_phased_Array_l3_candidate1",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    basic_a1 = models.CharField(max_length=256, null=True, blank=True)
    basic_a2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256, null=True, blank=True)
    main_d = models.CharField(max_length=256, null=True, blank=True)
    main_e = models.CharField(max_length=256, null=True, blank=True)
    main_f = models.CharField(max_length=256, null=True, blank=True)
    practical_tofd_l2 = models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class TimeFlightDiffractionTOFDLevel3_PCN_Material2(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="pcn_material_phased_Array_l3_event2", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="pcn_material_phased_Array_l3_candidate2",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    basic_a1 = models.CharField(max_length=256, null=True, blank=True)
    basic_a2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256, null=True, blank=True)
    main_d = models.CharField(max_length=256, null=True, blank=True)
    main_e = models.CharField(max_length=256, null=True, blank=True)
    main_f = models.CharField(max_length=256, null=True, blank=True)
    practical_tofd_l2 = models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class RadiographicInterpretationWeldsRIMaterial(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="ri_event1", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="ri_candidate1",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    general_theory = models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)
    practical = models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name

class RadiographicInterpretationWeldsRIResult(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="ri_event1_result", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="ri_candidate1_result",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    general_theory = models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)
    practical = models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name
#
#
# class TimeFlightDiffractionTOFDLevel3_PCN_Result(models.Model):
#     name = models.CharField(max_length=256, null=True, blank=True )
#     event = models.ForeignKey(Event, related_name="exam_material_flight_l3_pcn_event_result1", null=True, blank=True, on_delete=models.DO_NOTHING)
#     candidate = models.ForeignKey(TesCandidate,related_name="exam_material_flight_l3_pcn_candidate_result1",  null=True, blank=True , on_delete=models.DO_NOTHING)
#     customerID = models.CharField(max_length=256, null=True, blank=True)
#     scheme = models.CharField(max_length=256, null=True, blank=True)
#     exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
#     basic_a1 = models.CharField(max_length=256,null=True, blank=True)
#     basic_a2 = models.CharField(max_length=256,null=True, blank=True)
#     basic_b_part_1 = models.CharField(max_length=256,null=True, blank=True)
#     basic_b_part_2 = models.CharField(max_length=256,null=True, blank=True)
#     basic_b_part_3 = models.CharField(max_length=256,null=True, blank=True)
#     basic_b_part_4 = models.CharField(max_length=256,null=True, blank=True)
#     main_d =models.CharField(max_length=256,null=True, blank=True)
#     main_e = models.CharField(max_length=256,null=True, blank=True)
#     main_f = models.CharField(max_length=256,null=True, blank=True)
#     practical_tofd_l2 = models.CharField(max_length=256,null=True, blank=True)
#     delivery_method = models.CharField(max_length=256,null=True, blank=True)
#     lecturer = models.CharField(max_length=256, null=True, blank=True)
#     invigilator = models.CharField(max_length=256, null=True, blank=True)
#     venue = models.CharField(max_length=256, null=True, blank=True)
#     file = models.FileField(upload_to='exam_file', null=True, blank=True)
#     remark = models.CharField(max_length=2048, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.event.name


class TimeFlightDiffractionTOFDLevel3_PCN_Result2(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_flight_l3_pcn_event_result2", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_flight_l3_pcn_candidate_result2",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    basic_a1 = models.CharField(max_length=256,null=True, blank=True)
    basic_a2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256,null=True, blank=True)
    main_d =models.CharField(max_length=256,null=True, blank=True)
    main_e = models.CharField(max_length=256,null=True, blank=True)
    main_f = models.CharField(max_length=256,null=True, blank=True)
    practical_tofd_l2 = models.CharField(max_length=256,null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class TimeFlightDiffractionTOFDLevel3_PCN_Result3(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_flight_l3_pcn_event_result3", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_flight_l3_pcn_candidate_result3",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    basic_a1 = models.CharField(max_length=256,null=True, blank=True)
    basic_a2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256,null=True, blank=True)
    main_d =models.CharField(max_length=256,null=True, blank=True)
    main_e = models.CharField(max_length=256,null=True, blank=True)
    main_f = models.CharField(max_length=256,null=True, blank=True)
    practical_tofd_l2 = models.CharField(max_length=256,null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class TimeFlightDiffractionTOFDLevel3_CSWIP_Material2(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="cswip_material_phased_Array_l3_event2", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="cswip_material_phased_Array_l3_candidate2",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField( null=True, blank=True)
    basic_a1 = models.CharField(max_length=256, null=True, blank=True)
    basic_a2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256, null=True, blank=True)
    main_c_1 =models.CharField(max_length=256, null=True, blank=True)
    main_c_2 = models.CharField(max_length=256, null=True, blank=True)
    main_c_3 = models.CharField(max_length=256, null=True, blank=True)
    practical_tofd_l2 =models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name

class TimeFlightDiffractionTOFDLevel3_CSWIP_Material(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="cswip_material_phased_Array_l3_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="cswip_material_phased_Array_l3_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField( null=True, blank=True)
    basic_a1 = models.CharField(max_length=256, null=True, blank=True)
    basic_a2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256, null=True, blank=True)
    main_c_1 =models.CharField(max_length=256, null=True, blank=True)
    main_c_2 = models.CharField(max_length=256, null=True, blank=True)
    main_c_3 = models.CharField(max_length=256, null=True, blank=True)
    practical_tofd_l2 =models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class TimeFlightDiffractionTOFDLevel3_CSWIP_Result(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_flight_l3_event_result", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_flight_l3_candidate_result",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    basic_a1 = models.CharField(max_length=256,null=True, blank=True)
    basic_a2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256,null=True, blank=True)
    main_c_1 =models.CharField(max_length=256,null=True, blank=True)
    main_c_2 = models.CharField(max_length=256,null=True, blank=True)
    main_c_3 = models.CharField(max_length=256,null=True, blank=True)
    practical_tofd_l2 = models.CharField(max_length=256,null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name




class PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_phased_Array_l3_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_phased_Array_l3_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    basic_a1 = models.CharField(max_length=256, null=True, blank=True)
    basic_a2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256, null=True, blank=True)
    main_d = models.CharField(max_length=256, null=True, blank=True)
    main_e = models.CharField(max_length=256, null=True, blank=True)
    main_f = models.CharField(max_length=256, null=True, blank=True)
    practical_paut_l2 = models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="pcn_material_phased_Array_l3_event_result", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="pcn_material_phased_Array_l3_candidate_result",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    basic_a1 = models.CharField(max_length=256,null=True, blank=True)
    basic_a2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256,null=True, blank=True)
    main_d =models.CharField(max_length=256,null=True, blank=True)
    main_e = models.CharField(max_length=256,null=True, blank=True)
    main_f = models.CharField(max_length=256,null=True, blank=True)
    practical_paut_l2 = models.CharField(max_length=256,null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name




class PhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="pcn_material_phased_Array_l3_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="pcn_material_phased_Array_l3_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    basic_a1 =  models.CharField(max_length=256, null=True, blank=True)
    basic_a2 =  models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_1 =  models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_2 =  models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_3 =  models.CharField(max_length=256, null=True, blank=True)
    basic_b_part_4 =  models.CharField(max_length=256, null=True, blank=True)
    main_c_1 =  models.CharField(max_length=256, null=True, blank=True)
    main_c_2 =  models.CharField(max_length=256, null=True, blank=True)
    main_c_3 =  models.CharField(max_length=256, null=True, blank=True)
    practical_paut_l2 = models.CharField(max_length=256, null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class PhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_phased_Array_l3_event_result", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_phased_Array_l3_candidate_result",  null=True, blank=True , on_delete=models.DO_NOTHING)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    basic_a1 = models.CharField(max_length=256,null=True, blank=True)
    basic_a2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_1 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_2 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_3 = models.CharField(max_length=256,null=True, blank=True)
    basic_b_part_4 = models.CharField(max_length=256,null=True, blank=True)
    main_c_1 =models.CharField(max_length=256,null=True, blank=True)
    main_c_2 = models.CharField(max_length=256,null=True, blank=True)
    main_c_3 = models.CharField(max_length=256,null=True, blank=True)
    practical_paut_l2 = models.CharField(max_length=256,null=True, blank=True)
    delivery_method = models.CharField(max_length=256,null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    venue = models.CharField(max_length=256, null=True, blank=True)
    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2PCN(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_ultra_event_pcn", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_ultra_candidate_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample = models.ForeignKey(Samples,related_name="exam_material_ultra_sample_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)
    sample1_analysis = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample1_analysis_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample1_collection = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample1_collection_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample2_analysis = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample2_analysis_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample2_collection = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_gsample2_collection_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample3_analysis = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample3_analysis_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample3_collection = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample3_collection_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    written_instruction = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_written_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)


    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2PCN(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_ultra_result_event_pcn", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_ultra_result_candidate_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample = models.ForeignKey(Samples,related_name="exam_material_ultra_result_sample_pcn",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    specific_theory =models.CharField(max_length=128, null=True, blank=True)
    sample1_analysis = models.CharField(max_length=128, null=True, blank=True)
    sample1_collection = models.CharField(max_length=128, null=True, blank=True)
    sample2_analysis = models.CharField(max_length=128, null=True, blank=True)
    sample2_collection = models.CharField(max_length=128, null=True, blank=True)
    sample3_analysis = models.CharField(max_length=128, null=True, blank=True)
    sample3_collection =models.CharField(max_length=128, null=True, blank=True)
    written_instruction =models.CharField(max_length=128, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)

    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name





class ExamMaterialPhasedArrayUltrasonicTesting_PAUT_Level2CSWIP(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_ultra_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_ultra_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample = models.ForeignKey(Samples,related_name="exam_material_ultra_sample",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    general_theory =  models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)
    sample1_analysis = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample1_analysis",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample1_collection = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample1_collection",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample2_analysis = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample2_analysis",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample2_collection = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_gsample2_collection",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample3_analysis = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample3_analysis",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample3_collection = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_sample3_collection",  null=True, blank=True , on_delete=models.DO_NOTHING)
    written_instruction = models.ForeignKey(Samples,related_name="exam_material_ultera_sample_written",  null=True, blank=True , on_delete=models.DO_NOTHING)


    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class Exam_Result_PhasedArrayUltrasonicTesting_PAUT_Level2CSWIP(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_ultra_result_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_ultra_result_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample = models.ForeignKey(Samples,related_name="exam_material_ultra_result_sample",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    general_theory =models.CharField(max_length=128, null=True, blank=True)
    specific_theory = models.CharField(max_length=128, null=True, blank=True)
    sample1_analysis = models.CharField(max_length=128, null=True, blank=True)
    sample1_collection = models.CharField(max_length=128, null=True, blank=True)
    sample2_analysis = models.CharField(max_length=128, null=True, blank=True)
    sample2_collection = models.CharField(max_length=128, null=True, blank=True)
    sample3_analysis = models.CharField(max_length=128, null=True, blank=True)
    sample3_collection =models.CharField(max_length=128, null=True, blank=True)
    written_instruction =models.CharField(max_length=128, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)

    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class BGAS_CSWIP_PaintingInspectorMaterial(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_result_event_painting_exam_material", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_result_candidate_painting_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    # exam = models.ForeignKey(ExamMaterialPAUTL2,related_name="exam_result_31_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=128,null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.CharField(max_length=4096,null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file',null=True,blank=True)
    general_theory = models.CharField(max_length=256, null=True, blank=True)
    practical = models.CharField(max_length=256, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class BGAS_CSWIP_PaintingInspectorResult(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_result_event_painting_exam_result", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_result_candidate_painting_exam_result",  null=True, blank=True , on_delete=models.DO_NOTHING)
    # exam = models.ForeignKey(ExamMaterialPAUTL2,related_name="exam_result_31_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=128,null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.CharField(max_length=4096,null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file',null=True,blank=True)
    general_theory = models.CharField(max_length=128,null=True, blank=True)
    practical = models.CharField(max_length=128,null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class CSWIPWeldingInspector3_2_2ExamMaterial(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_result_event_322_exam_material", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_result_candidate_322_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    # exam = models.ForeignKey(ExamMaterialPAUTL2,related_name="exam_result_31_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=128,null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.CharField(max_length=4096,null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file',null=True,blank=True)
    general_theory_s = models.CharField(max_length=256, null=True, blank=True)
    ndt_s = models.CharField(max_length=256, null=True, blank=True)
    symbols_s = models.CharField(max_length=256, null=True, blank=True)
    scenario_s = models.CharField(max_length=256, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class CSWIPWeldingInspector3_2_2_Result(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    event = models.ForeignKey(Event, related_name="exam_result_event_322_result", null=True, blank=True,
                              on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate, related_name="exam_result_candidate_322_result", null=True,
                                  blank=True, on_delete=models.DO_NOTHING)
    # exam = models.ForeignKey(ExamMaterialPAUTL2,related_name="exam_result_31_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=128, null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.CharField(max_length=4096, null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file', null=True, blank=True)
    general_theory_s = models.CharField(max_length=256, null=True, blank=True)
    ndt_s = models.CharField(max_length=256, null=True, blank=True)
    symbols_s = models.CharField(max_length=256, null=True, blank=True)
    scenario_s = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class CSWIPWeldingInspector3_2_1ExamMaterial2(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_result_event_321_exam_material2", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_result_candidate_321_exam_material2",  null=True, blank=True , on_delete=models.DO_NOTHING)
    # exam = models.ForeignKey(ExamMaterialPAUTL2,related_name="exam_result_31_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=128,null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.CharField(max_length=4096,null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file',null=True,blank=True)
    general_theory_s = models.CharField(max_length=256, null=True, blank=True)
    ndt_s = models.CharField(max_length=256, null=True, blank=True)
    symbols_s = models.CharField(max_length=256, null=True, blank=True)
    scenario_s = models.CharField(max_length=256, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class CSWIPWeldingInspector3_2_1ExamMaterial(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_result_event_321_exam_material", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_result_candidate_321_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    # exam = models.ForeignKey(ExamMaterialPAUTL2,related_name="exam_result_31_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=128,null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.CharField(max_length=4096,null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file',null=True,blank=True)
    general_theory_s = models.CharField(max_length=256, null=True, blank=True)
    ndt_s = models.CharField(max_length=256, null=True, blank=True)
    symbols_s = models.CharField(max_length=256, null=True, blank=True)
    scenario_s = models.CharField(max_length=256, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class CSWIPWeldingInspector3_2_1_Result(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    event = models.ForeignKey(Event, related_name="exam_result_event_321_result", null=True, blank=True,
                              on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate, related_name="exam_result_candidate_321_result", null=True,
                                  blank=True, on_delete=models.DO_NOTHING)
    # exam = models.ForeignKey(ExamMaterialPAUTL2,related_name="exam_result_31_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=128, null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.CharField(max_length=4096, null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file', null=True, blank=True)
    general_theory_s = models.CharField(max_length=256, null=True, blank=True)
    ndt_s = models.CharField(max_length=256, null=True, blank=True)
    symbols_s = models.CharField(max_length=256, null=True, blank=True)
    scenario_s = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='exam_file', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class ExamMaterialTofdL3(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_tofd_l3_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_tofd_l3_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)



    tofd_scheme = models.CharField(max_length=256, null=True, blank=True)
    tofd_exam_date = models.DateTimeField(null=True, blank=True)
    tofd_ndtl3 = models.CharField(max_length=256,null=True, blank=True)
    tofd_pautl2 = models.CharField(max_length=256,null=True, blank=True)
    tofd_practical_exam = models.CharField(max_length=256,null=True, blank=True)
    tofd_basic_a1 = models.CharField(max_length=256,null=True, blank=True)
    tofd_basic_a2 = models.CharField(max_length=256,null=True, blank=True)
    tofd_basic_b_part_1 = models.CharField(max_length=256,null=True, blank=True)
    tofd_basic_b_part_2 = models.CharField(max_length=256,null=True, blank=True)
    tofd_basic_b_part_3 = models.CharField(max_length=256,null=True, blank=True)
    tofd_basic_b_part_4 = models.CharField(max_length=256,null=True, blank=True)
    tofd_main_c_1 = models.CharField(max_length=256,null=True, blank=True)
    tofd_main_c_2 = models.CharField(max_length=256,null=True, blank=True)
    tofd_main_c_3 = models.CharField(max_length=256,null=True, blank=True)
    tofd_delivery_method = models.CharField(max_length=256, null=True, blank=True)
    tofd_lecturer = models.CharField(max_length=256, null=True, blank=True)
    tofd_invigilator = models.CharField(max_length=256, null=True, blank=True)
    tofd_venue = models.CharField(max_length=256, null=True, blank=True)
    tofd_remark = models.CharField(max_length=2048, null=True, blank=True)



    pcn_tofd_l3_scheme = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_exam_date = models.DateTimeField(null=True, blank=True)
    pcn_tofd_l3_ndtl3 = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_pautl2 = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_practical_exam = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_basic_a1 = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_basic_a2 = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_basic_b_part_1 = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_basic_b_part_2 = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_basic_b_part_3 = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_basic_b_part_4 = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_main_d = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_main_e = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_main_f = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_delivery_method = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_lecturer = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_invigilator = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_venue = models.CharField(max_length=256, null=True, blank=True)
    pcn_tofd_l3_remark = models.CharField(max_length=2048, null=True, blank=True)


    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name

class ExamMaterialL3(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_l3_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_l3_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)

    paut_scheme = models.CharField(max_length=256, null=True, blank=True)
    paut_exam_date = models.DateTimeField(max_length=256,null=True, blank=True)
    paut_ndtl3 = models.CharField(max_length=256,null=True, blank=True)
    paut_pautl2 = models.CharField(max_length=256,null=True, blank=True)
    paut_practical_exam = models.CharField(max_length=256,null=True, blank=True)
    paut_basic_a1 = models.CharField(max_length=256,null=True, blank=True)
    paut_basic_a2 = models.CharField(max_length=256,null=True, blank=True)
    paut_basic_b_part_1 = models.CharField(max_length=256,null=True, blank=True)
    paut_basic_b_part_2 = models.CharField(max_length=256,null=True, blank=True)
    paut_basic_b_part_3 = models.CharField(max_length=256,null=True, blank=True)
    paut_basic_b_part_4 = models.CharField(max_length=256,null=True, blank=True)
    paut_main_c_1 = models.CharField(max_length=256,null=True, blank=True)
    paut_main_c_2 = models.CharField(max_length=256,null=True, blank=True)
    paut_main_c_3 = models.CharField(max_length=256,null=True, blank=True)
    paut_delivery_method = models.CharField(max_length=256,null=True, blank=True)
    paut_lecturer = models.CharField(max_length=256, null=True, blank=True)
    paut_invigilator = models.CharField(max_length=256, null=True, blank=True)
    paut_venue = models.CharField(max_length=256, null=True, blank=True)
    paut_remark = models.CharField(max_length=2048, null=True, blank=True)


    pcn_paut_l3_scheme = models.CharField(max_length=256, null=True, blank=True)
    pcn_paut_l3_exam_date = models.DateTimeField(null=True, blank=True)
    pcn_paut_l3_ndtl3 = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_pautl2 = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_practical_exam = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_basic_a1 = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_basic_a2 = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_basic_b_part_1 = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_basic_b_part_2 = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_basic_b_part_3 = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_basic_b_part_4 = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_main_d = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_main_e = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_main_f = models.CharField(max_length=256,null=True, blank=True)
    pcn_paut_l3_delivery_method = models.CharField(max_length=256, null=True, blank=True)
    pcn_paut_l3_lecturer = models.CharField(max_length=256, null=True, blank=True)
    pcn_paut_l3_invigilator = models.CharField(max_length=256, null=True, blank=True)
    pcn_paut_l3_venue = models.CharField(max_length=256, null=True, blank=True)
    pcn_paut_l3_remark = models.CharField(max_length=2048, null=True, blank=True)



    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name

class ExamMaterialPAUTL2(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_pautl_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_pautl_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample = models.ForeignKey(Samples,related_name="exam_material_pautl_sample",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    general_theory = models.ForeignKey(Samples,related_name="exam_material_pautl_sample_general_theory",  null=True, blank=True , on_delete=models.DO_NOTHING)
    specific_theory = models.ForeignKey(Samples,related_name="exam_material_pautl_sample_specific_theory",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample1_analysis = models.ForeignKey(Samples,related_name="exam_material_pautl_sample_sample1_analysis",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample1_collection = models.ForeignKey(Samples,related_name="exam_material_pautl_sample_sample1_collection",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample2_analysis = models.ForeignKey(Samples,related_name="exam_material_pautl_sample_sample2_analysis",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample2_collection = models.ForeignKey(Samples,related_name="exam_material_pautl_sample_gsample2_collection",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample3_analysis = models.ForeignKey(Samples,related_name="exam_material_pautl_sample_sample3_analysis",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample3_collection = models.ForeignKey(Samples,related_name="exam_material_pautl_sample_sample3_collection",  null=True, blank=True , on_delete=models.DO_NOTHING)
    written_instruction = models.ForeignKey(Samples,related_name="exam_material_pautl_sample_written",  null=True, blank=True , on_delete=models.DO_NOTHING)


    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class ExamResultPautL2(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_result_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_result_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam = models.ForeignKey(ExamMaterialPAUTL2,related_name="exam_result",  null=True, blank=True , on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=128,null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    explanation = models.CharField(max_length=4096,null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file',null=True,blank=True)
    general_theory = models.CharField(max_length=128,null=True, blank=True)
    specific_theory = models.CharField(max_length=128, null=True, blank=True)
    sample1_analysis = models.CharField(max_length=128,null=True, blank=True)
    sample1_collection = models.CharField(max_length=128, null=True, blank=True)
    sample2_analysis = models.CharField(max_length=128, null=True, blank=True)
    sample2_collection = models.CharField(max_length=128, null=True, blank=True)
    sample3_analysis = models.CharField(max_length=128, null=True, blank=True)
    sample3_collection = models.CharField(max_length=128,null=True, blank=True)
    written_instruction = models.CharField(max_length=128,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class CSWIPWeldingInspector3_1ExamMaterial(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_result_event_31_exam_material", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_result_candidate_31_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    # exam = models.ForeignKey(ExamMaterialPAUTL2,related_name="exam_result_31_exam_material",  null=True, blank=True , on_delete=models.DO_NOTHING)
    result = models.CharField(max_length=128,null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.CharField(max_length=4096,null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file',null=True,blank=True)
    general_paper = models.CharField(max_length=256, null=True, blank=True)
    technology_paper = models.CharField(max_length=256, null=True, blank=True)
    plate_paper = models.CharField(max_length=256, null=True, blank=True)
    pipe_paper = models.CharField(max_length=256, null=True, blank=True)
    macro_paper = models.CharField(max_length=256, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name





class CSWIPWeldingInspector3_1Result(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_result_event_31", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_result_candidate_31",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam = models.ForeignKey(CSWIPWeldingInspector3_1ExamMaterial,related_name="exam_result_31",  null=True, blank=True , on_delete=models.CASCADE)
    invigilator = models.CharField(max_length=128,null=True, blank=True)
    exam_title = models.CharField(max_length=128,null=True, blank=True)
    scheme = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.CharField(max_length=4096,null=True, blank=True)
    file = models.FileField(upload_to='exam_result_file',null=True,blank=True)
    general_paper = models.CharField(max_length=128,null=True, blank=True)
    technology_paper = models.CharField(max_length=128, null=True, blank=True)
    plate_paper = models.CharField(max_length=128, null=True, blank=True)
    pipe_paper = models.CharField(max_length=128, null=True, blank=True)
    macro_paper = models.CharField(max_length=128, null=True, blank=True)
    exam_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name


class CSWIPWeldingInspector3_1ResultIntermadiate(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    candidate = models.ForeignKey(TesCandidate, related_name="exam_material_result_intermadiate_candidate", null=True, blank=True,
                                  on_delete=models.DO_NOTHING)
    primary = models.ForeignKey(CSWIPWeldingInspector3_1Result,related_name="exam_result_31_intermediate",  null=True, blank=True , on_delete=models.CASCADE)
    secondry = models.ForeignKey(CSWIPWeldingInspector3_1Result,related_name="exam_result_31_intermediate_result1",  null=True, blank=True , on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name



class ExamMaterialTOFDModel1(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_tofd_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_tofd_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    general_theory = models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)
    sample1 = models.ForeignKey(Samples,related_name="exam_material_pautl2_sample1",  null=True, blank=True , on_delete=models.DO_NOTHING)
    sample2 = models.ForeignKey(Samples,related_name="exam_material_pautl2_sample2",  null=True, blank=True , on_delete=models.DO_NOTHING)
    data_file_1 = models.CharField(max_length=256, null=True, blank=True)
    data_file_2 = models.CharField(max_length=256, null=True, blank=True)
    data_file_3 = models.CharField(max_length=256, null=True, blank=True)
    data_file_4 = models.CharField(max_length=256, null=True, blank=True)
    data_file_5 = models.CharField(max_length=256, null=True, blank=True)
    written_instruction = models.ForeignKey(Samples, related_name="exam_material_written_instruction_l2", null=True,
                                            blank=True, on_delete=models.DO_NOTHING)


    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name



class ExamMaterialTOFD_CSWIP(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True )
    event = models.ForeignKey(Event, related_name="exam_material_tofd_l2_event", null=True, blank=True, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(TesCandidate,related_name="exam_material_tofd_l2_candidate",  null=True, blank=True , on_delete=models.DO_NOTHING)
    exam_date = models.DateTimeField(null=True, blank=True)
    cswip_pcn = models.CharField(max_length=256, null=True, blank=True)
    exam_title = models.CharField(max_length=256, null=True, blank=True)
    customerID = models.CharField(max_length=256, null=True, blank=True)
    lecturer = models.CharField(max_length=256, null=True, blank=True)
    invigilator = models.CharField(max_length=256, null=True, blank=True)
    general_theory = models.CharField(max_length=256, null=True, blank=True)
    specific_theory = models.CharField(max_length=256, null=True, blank=True)
    sample1 = models.CharField(max_length=256, null=True, blank=True)
    sample2 = models.CharField(max_length=256, null=True, blank=True)
    data_file_1 = models.CharField(max_length=256, null=True, blank=True)
    data_file_2 = models.CharField(max_length=256, null=True, blank=True)
    data_file_3 = models.CharField(max_length=256, null=True, blank=True)
    data_file_4 = models.CharField(max_length=256, null=True, blank=True)
    data_file_5 = models.CharField(max_length=256, null=True, blank=True)
    written_instruction = models.CharField(max_length=256, null=True, blank=True)


    remark = models.CharField(max_length=2048, null=True, blank=True)
    file = models.FileField(upload_to='exam_file',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name
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


