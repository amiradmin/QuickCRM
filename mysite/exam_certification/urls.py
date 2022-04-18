from django.urls import path,include
from exam_certification import views
from django.conf import settings



app_name ="exam_certification"
urlpatterns = [



    path('cerattendancelist', views.CertificateAttendanceView.as_view(), name='cerattendancelist_'),
    path('newcerattendance', views.NewCertificateAttendance.as_view(), name='newcerattendance_'),
    path('finalcertificate/<int:id>/<int:canID>/<int:eventID>', views.FinalCertificateAttendanceView.as_view(), name='finalcertificate_'),
    path('deletecerattendance/<int:pk>/delete/', views.DeleteCertificateAttendance.as_view(), name='deletecerattendance_'),
    path('cersummary', views.CertificateSummayView.as_view(), name='cersummary_'),
    path('swipcersummary', views.CSWIPCertificateSummayView.as_view(), name='swipcersummary_'),
    path('pcncersummary', views.PCNCertificateSummayView.as_view(), name='pcncersummary_'),
    path('newpcncer', views.NewPcnCertificateAttendance.as_view(), name='newpcncer_'),
    path('newcswipcer', views.NewCswipCertificateAttendance.as_view(), name='newcswipcer_'),
    path('pcndelete/<int:pk>/delete/', views.DeletePcnCertificate.as_view(), name='pcndelete_'),


    path('exampiwi/', views.ExamMaterialPiWi.as_view(), name='exampiwi_'),
    path('exampiwisummary/', views.ExamMaterialPiWiSummary.as_view(), name='exampiwisummary_'),
    path('newexampiwi/', views.NewExamMaterialPiWi.as_view(), name='newexampiwi_'),
    path('exampiwidelete/<int:pk>/delete/', views.DeleteExamPiWi.as_view(), name='exampiwidelete_'),

    # path('exampiwi/', views.ExamMaterialPiWi.as_view(), name='exampiwi_'),
    path('examtofdsummary/', views.ExamMaterialTofdSummary.as_view(), name='examtofdsummary_'),
    path('newexamtofd/', views.NewExamMaterialTofd.as_view(), name='newexamtofd_'),
    path('examtofddelete/<int:pk>/delete/', views.DeleteExamTofd.as_view(), name='examtofddelete_'),

    path('exampautl2summary/', views.ExamMaterialPAUTL2Summary.as_view(), name='exampautl2summary_'),
    path('newexamaputl2/', views.NewExamMaterialPautl2.as_view(), name='newexamaputl2_'),
    path('exampautl2delete/<int:pk>/delete/', views.DeleteExamPAUTL2.as_view(), name='exampautl2delete_'),

    path('examl3summary/', views.ExamMaterialL3Summary.as_view(), name='examl3summary_'),
    path('newexaml3/', views.NewExamMaterialL3.as_view(), name='newexaml3_'),
    path('l3ismform/<int:id>', views.ExamMaterialL3IMSForm.as_view(), name='l3ismform_'),
    path('examl3delete/<int:pk>/delete/', views.DeleteExamL3Material.as_view(), name='examl3delete_'),

    path('examtofdl3summary/', views.ExamMaterialTofdL3Summary.as_view(), name='examtofdl3summary_'),
    path('newexamtofdl3/', views.NewExamMaterialTofdL3.as_view(), name='newexamtofdl3_'),
    path('tofdl3ismform/<int:id>', views.ExamMaterialTofdL3IMSForm.as_view(), name='tofdl3ismform_'),
    path('examtofdl3delete/<int:pk>/delete/', views.DeleteExamTofdL3Material.as_view(), name='examtofdl3delete_'),

    path('examresultsummary/', views.ExamResultSummary.as_view(), name='examresultsummary_'),
    path('newexamresult/', views.NewExamResultPautL2.as_view(), name='newexamresult_'),
    path('newexamresultbyid/<int:id>', views.ExamResultSummaryByID.as_view(), name='newexamresultbyid_'),
    path('l3ismform/<int:id>', views.ExamCSWIP31ResultSummaryByID.as_view(), name='l3ismform_'),
    # path('examl3delete/<int:pk>/delete/', views.DeleteExamL3Material.as_view(), name='examl3delete_'),

    path('examscwip31summary/', views.CSWIPExamMaterial31Summary.as_view(), name='examscwip31summary_'),
    path('newexamrscwip31esultbyid/<int:id>', views.ExamCSWIP31ResultSummaryByID.as_view(), name='newexamrscwip31esultbyid_'),
    path('newcswipexam31/', views.NewCSWIPExamMaterial31.as_view(), name='newcswipexam31_'),
    path('examcswip31delete/<int:pk>/delete/', views.DeleteCSWIPExamMaterial31.as_view(), name='examcswip31delete_'),

    path('examscwip321summary/', views.CSWIPExamMaterial321Summary.as_view(), name='examscwip321summary_'),
    # path('newexamrscwip31esultbyid/<int:id>', views.ExamCSWIP31ResultSummaryByID.as_view(), name='newexamrscwip31esultbyid_'),
    path('newcswipexam321/', views.NewCSWIPExamMaterial321.as_view(), name='newcswipexam321_'),
    path('examcswip321delete/<int:pk>/delete/', views.DeleteCSWIPExamMaterial321.as_view(), name='examcswip321delete_'),

    path('examscwip322summary/', views.CSWIPExamMaterial322Summary.as_view(), name='examscwip322summary_'),
    # path('newexamrscwip31esultbyid/<int:id>', views.ExamCSWIP31ResultSummaryByID.as_view(), name='newexamrscwip31esultbyid_'),
    path('newcswipexam322/', views.NewCSWIPExamMaterial322.as_view(), name='newcswipexam322_'),
    path('examcswip322delete/<int:pk>/delete/', views.DeleteCSWIPExamMaterial322.as_view(), name='examcswip322delete_'),

    path('exampaintinginspectionsummary/', views.BGAS_CSWIP_PaintingInspectorSummary.as_view(), name='exampaintinginspectionsummary_'),
    # path('newexamrscwip31esultbyid/<int:id>', views.NewBGAS_CSWIP_PaintingInspector.as_view(), name='newexamrscwip31esultbyid_'),
    path('newpaintinginspectionexam/', views.NewBGAS_CSWIP_PaintingInspector.as_view(), name='newpaintinginspectionexam_'),
    path('paintinginspectiondelete/<int:pk>/delete/', views.DeletePaintingInspectionMaterial.as_view(), name='paintinginspectiondelete_'),


    path('examscwipphasedarraysummary/', views.CSWIPPhasedArrayUltrasonicSummary.as_view(), name='examscwipphasedarraysummary_'),
    path('newscwipphasedarray/', views.NewExamMaterialCSWIPPhasedArrayUltera.as_view(), name='newscwipphasedarray_'),
    path('scwipphasedarraydelete/<int:pk>/delete/', views.DeleteCSWIPPhasedAraayUltera.as_view(), name='scwipphasedarraydelete_'),

    path('examscwipultral3summary/', views.PhasedArrayUltrasonicTesting_PAUT_L3CSWIPSummary.as_view(), name='examscwipultral3summary_'),
    path('newsexamscwipultral3/', views.NewExamMaterialPAUTUltraL3.as_view(), name='newsexamscwipultral3_'),
    path('examscwipultral3delete/<int:pk>/delete/', views.DeletePhasedArrayUltrasonicTesting_PAUT_L3CSWIPMaterial.as_view(), name='examscwipultral3delete_'),

    path('exampcnl3summary/', views.PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material_Summary.as_view(), name='exampcnl3summary_'),
    path('newexampcnl3/', views.NewExamMaterialPAUTUltraL3PCN.as_view(), name='newexampcnl3_'),
    path('exampcnl3delete/<int:pk>/delete/', views.DeletePhasedArrayUltrasonicTesting_PAUT_L3_PCN_Material.as_view(), name='exampcnl3delete_'),

    path('examscwipultral3resultsummary/', views.PhasedArrayUltrasonicTesting_PAUT_L3CSWIP_Result_Summary.as_view(), name='examscwipultral3resultsummary_'),
    path('newsexamscwipultral3result/', views.NewExamResultPAUTUltraL3.as_view(), name='newsexamscwipultral3result_'),
    path('examscwipultral3resultdelete/<int:pk>/delete/', views.DeletePhasedArrayUltrasonicTesting_PAUT_L3CSWIPResult.as_view(), name='examscwipultral3resultdelete_'),

    path('exampcnphasedarraysummary/', views.PCNPhasedArrayUltrasonicMaterialSummary.as_view(), name='exampcnphasedarraysummary_'),
    path('newexampcnphasedarray/', views.NewExamMaterialPCNPhasedArrayUltera.as_view(), name='newexampcnphasedarray_'),
    path('pcnphasedarraydelete/<int:pk>/delete/', views.DeletePhasedArrayPCNMaterial.as_view(), name='pcnphasedarraydelete_'),

    path('exampcnphasedarrayresultsummary/', views.PCNPhasedArrayUltrasonicResultSummary.as_view(), name='exampcnphasedarrayresultsummary_'),
    path('newexampcnphasedarraypcn/', views.NewExamResultPCNPhasedArrayUltrasonic.as_view(), name='newexampcnphasedarraypcn_'),
    path('pcnphasedarrayresultdelete/<int:pk>/delete/', views.DeletePhasedArrayPCNResult.as_view(), name='pcnphasedarrayresultdelete_'),

    path('examscwip31resultsummary/', views.CSWIPExamResult31Summary.as_view(), name='examscwip31resultsummary_'),
    path('newcswipexam31result/', views.NewExamResultSwip31.as_view(), name='newcswipexam31result_'),
    path('examcswip31delete/<int:pk>/delete/', views.DeleteCSWIPExamMaterial31.as_view(), name='examcswip31delete_'),


    path('examscwip321resultsummary/', views.CSWIPExamResult321Summary.as_view(), name='examscwip321resultsummary_'),
    path('newcswipexam321result/', views.NewExamResultSwip321.as_view(), name='newcswipexam321result_'),
    path('examcswip321resultdelete/<int:pk>/delete/', views.DeleteCSWIPExamResult321.as_view(), name='examcswip321resultdelete_'),


    path('cswipphasedarrayresultsummary/', views.CSWIPPhasedArrayUltrasonic_Result_Summary.as_view(), name='cswipphasedarrayresultsummary_'),
    path('newcswipphasedarrayresult/', views.NewExamResultCSWIPPhasedArrayUltrasonic.as_view(), name='newcswipphasedarrayresult_'),
    path('examcswipphasedarraydelete/<int:pk>/delete/', views.DeletePhasedArrayResultL2.as_view(), name='examcswipphasedarraydelete_'),


    path('paintinginspectionresultsummary/', views.PaintingInspectionSummary.as_view(), name='paintinginspectionresultsummary_'),
    path('newcpaintinginspectionresult/', views.NewExamResultPaintingInspection.as_view(), name='newcpaintinginspectionresult_'),
    path('paintinginspectionresultdelete/<int:pk>/delete/', views.DeletePaintingInspectionResult2.as_view(), name='paintinginspectionresultdelete_'),


    path('examscwip322resultsummary/', views.CSWIPExamResult322Summary.as_view(), name='examscwip322resultsummary_'),
    path('newcswipexam322result/', views.NewExamResultSwip322.as_view(), name='newcswipexam322result_'),
    path('examcswip322resultdelete/<int:pk>/delete/', views.DeleteCSWIPExamResult322.as_view(), name='examcswip322resultdelete_'),

    path('exampcnultral3resultsummary/', views.PhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result_Summary.as_view(),
         name='exampcnultral3resultsummary_'),
    path('newsexampcnultral3result/', views.NewPhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result.as_view(), name='newsexampcnultral3result_'),
    path('exampcnultral3resultdelete/<int:pk>/delete/',
         views.DeletePhasedArrayUltrasonicTesting_PAUT_L3_PCN_Result.as_view(), name='exampcnultral3resultdelete_'),

    path('examcswiptofdl3summary/', views.TimeFlightDiffractionTOFDLevel3_CSWIP_Material_Summary.as_view(), name='examcswiptofdl3summary_'),
    path('newcexamcswiptofdl3material/', views.NewTimeFlightDiffractionTOFDLevel3_CSWIP_Material.as_view(), name='newcexamcswiptofdl3material_'),
    path('cexamcswiptofdl3delete/<int:pk>/delete/', views.DeleteTimeFlightDiffractionTOFDLevel3_CSWIP_Material.as_view(),
         name='cexamcswiptofdl3delete_'),

    path('examswiptofdresultsummary/', views.TimeFlightDiffractionTOFDLevel3_CSWIP_Result_Summary.as_view(),
         name='examswiptofdresultsummary_'),
    path('newsexamswiptofdresultresult/', views.TimeFlightDiffractionTOFDLevel3_CSWIP_Result_Result.as_view(),
         name='newsexamswiptofdresultresult_'),
    path('examswiptofdresultresultdelete/<int:pk>/delete/',
         views.DeleteTimeFlightDiffractionTOFDLevel3_CSWIP_Result.as_view(), name='examswiptofdresultresultdelete_'),

    path('exampcntofdl3summary/', views.TimeFlightDiffractionTOFDLevel3_PCN_Material_Summary.as_view(),
         name='exampcntofdl3summary_'),
    # path('newcexamcswiptofdl3material/', views.NewTimeFlightDiffractionTOFDLevel3_CSWIP_Material.as_view(),
    #      name='newcexamcswiptofdl3material_'),
    # path('cexamcswiptofdl3delete/<int:pk>/delete/',
    #      views.DeleteTimeFlightDiffractionTOFDLevel3_CSWIP_Material.as_view(),
    #      name='cexamcswiptofdl3delete_'),

]
