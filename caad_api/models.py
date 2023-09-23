# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccomodationProforma(models.Model):
    ac_id = models.AutoField(primary_key=True)
    internship = models.ForeignKey('Internships', models.DO_NOTHING)
    identity= models.ForeignKey('IdentitycardProforma', models.DO_NOTHING)
    date_of_application = models.DateField()
    security_and_police_proforma = models.BooleanField()
    application_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    accomodation_start_date = models.DateField(blank=True, null=True)
    accomodation_end_date = models.DateField(blank=True, null=True)
    institute_type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pdf_form = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accomodation_proforma'


class AccomodationType(models.Model):
    accomodation_id = models.AutoField(primary_key=True)
    accm_description = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accomodation_type'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CaadAccomodationVerification(models.Model):
    caad_hr3_id = models.AutoField(primary_key=True)
    accom_type = models.ForeignKey(AccomodationType, models.DO_NOTHING, blank=True, null=True)
    accomodation_form = models.ForeignKey(AccomodationProforma, models.DO_NOTHING, blank=True, null=True)
    registration_entries = models.BooleanField(blank=True, null=True)
    police_verification = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caad_accomodation_verification'


class CaadClearanceVerification(models.Model):
    caad_clearance_id = models.AutoField(primary_key=True)
    clearance = models.ForeignKey('ClearancePerforma', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caad_clearance_verification'


class CaadEvaluationVerification(models.Model):
    caad_evaluation_id = models.AutoField(primary_key=True)
    evaluation = models.ForeignKey('EvaluationProforma', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caad_evaluation_verification'


class CaadExtensionVerification(models.Model):
    caad_extension_id = models.AutoField(primary_key=True)
    extension_form = models.ForeignKey('ExtensionProforma', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'caad_extension_verification'


class CaadIdentityVerification(models.Model):
    caad_identity_id = models.AutoField(db_column='CAAD_identity_id', primary_key=True)  # Field name made lowercase.
    university_type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    security_particular_proforma = models.BooleanField(blank=True, null=True)
    police_verification_proforma = models.BooleanField(blank=True, null=True)
    identity = models.ForeignKey('IdentitycardProforma', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'caad_identity_verification'


class CaadLatesittingVerification(models.Model):
    caad_latesitting_id = models.AutoField(primary_key=True)
    latesit = models.ForeignKey('LateSittingProforma', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'caad_latesitting_verification'


class CaadRegistrationVerification(models.Model):
    caad_registration_verification = models.AutoField(primary_key=True)
    internship = models.ForeignKey('Internships', models.DO_NOTHING, blank=True, null=True)
    academic_record_acceptable = models.BooleanField(blank=True, null=True)
    financial_matter_involve = models.BooleanField(blank=True, null=True)
    applicant_applicable = models.BooleanField(blank=True, null=True)
    funds_available = models.BooleanField(blank=True, null=True)
    applicant_considered = models.BooleanField(blank=True, null=True)
    tors_issue_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caad_registration_verification'


class CaadTransportVerification(models.Model):
    transport_confirmation_id = models.AutoField(primary_key=True)
    transport_availability = models.BooleanField(blank=True, null=True)
    vehicle_reg_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    confirmation_date = models.DateField(blank=True, null=True)
    transport_form = models.ForeignKey('TransportMemberProforma', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'caad_transport_verification'


class ClearancePerforma(models.Model):
    clearance_id = models.AutoField(primary_key=True)
    internship = models.ForeignKey('Internships', models.DO_NOTHING, blank=True, null=True)
    reason_to_leave = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    application_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    identity = models.ForeignKey('IdentitycardProforma', models.DO_NOTHING)
    apply_date = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pdf_form = models.BinaryField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'clearance_performa'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documents(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    required = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class DocumentsUpload(models.Model):
    uploaddoc_id = models.AutoField(db_column='uploadDoc_id', primary_key=True)  # Field name made lowercase.
    image = models.BinaryField(blank=True, null=True)
    std_cnic = models.ForeignKey('Student', models.DO_NOTHING, db_column='std_cnic')
    doc = models.ForeignKey(Documents, models.DO_NOTHING)
    img_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_upload'


class EvaluationProforma(models.Model):
    evaluation_id = models.AutoField(primary_key=True)
    date_of_submission = models.DateField(blank=True, null=True)
    internship = models.ForeignKey('Internships', models.DO_NOTHING)
    research_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    research_title = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    research_summary = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pdf_form = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation_proforma'


class ExtensionProforma(models.Model):
    extension_form_id = models.AutoField(primary_key=True)
    apply_date = models.DateField(blank=True, null=True)
    internship = models.ForeignKey('Internships', models.DO_NOTHING)
    reason_for_extension = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    reqperiod_ex_startdate = models.DateField()
    reqperiod_ex_enddate = models.DateField()
    accomodation = models.BooleanField()
    transport = models.BooleanField()
    application_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pdf_form = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extension_proforma'


class HostedresearcherCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostedresearcher_category'


class IdentitycardProforma(models.Model):
    identity_id = models.AutoField(primary_key=True)
    identity_apply_date = models.DateField(blank=True, null=True)
    internship = models.ForeignKey('Internships', models.DO_NOTHING)
    registration_date = models.DateField(blank=True, null=True)
    registration_receipt_number = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    blood_group = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    identification_mark = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    application_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'identitycard_proforma'


class Internships(models.Model):
    internship_id = models.AutoField(primary_key=True)
    proposed_research_area = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    proposed_research_start_time = models.DateField(blank=True, null=True)
    proposed_research_end_time = models.DateField(blank=True, null=True)
    accomodation_required = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    accomodation_start_time = models.DateField(blank=True, null=True)
    accomodation_end_time = models.DateField(blank=True, null=True)
    application_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ncp_employee_id = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    category = models.ForeignKey(HostedresearcherCategory, models.DO_NOTHING, blank=True, null=True)
    registration_no = models.ForeignKey('StudentRegistration', models.DO_NOTHING, db_column='registration_no',null=True)
    ncp_assigned_regno = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    university_supervisor = models.ForeignKey('UniversitySupervisor', models.DO_NOTHING, blank=True, null=True)
    proposed_research_department = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    is_supervisor_from_ncp = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    is_cosupervisor_from_ncp = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    consulted_date_of_ncp_supervisor = models.DateField(blank=True, null=True)
    apply_date = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pdf_form = models.BinaryField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'internships'


class ItDeptLogin(models.Model):
    user_id = models.AutoField(primary_key=True)
    login_form = models.ForeignKey('LoginProforma', models.DO_NOTHING)
    email_acc = models.BooleanField(blank=True, null=True)
    window_login_acc = models.BooleanField(blank=True, null=True)
    all_user_mailing_list = models.BooleanField(blank=True, null=True)
    linux_acc = models.BooleanField(blank=True, null=True)
    print_quota = models.BooleanField(blank=True, null=True)
    department_mailing_list = models.BooleanField(blank=True, null=True)
    vpn_account = models.BooleanField(blank=True, null=True)
    record_update = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it_dept_login'


class LateSittingProforma(models.Model):
    latesit_id = models.AutoField(primary_key=True)
    late_performa_submitdate = models.DateField(blank=True, null=True)
    internship = models.ForeignKey(Internships, models.DO_NOTHING)
    latesitting_reason = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    workarea_during_latework = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lab_contact_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    latesitting_startdate = models.DateField(blank=True, null=True)
    latesitting_enddate = models.DateField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emergency_contact_landline = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    attendant_during_latework = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    recommended_by_supervisor = models.BooleanField(blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pdf_form = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'late_sitting_proforma'


class LoginProforma(models.Model):
    login_form_id = models.AutoField(primary_key=True)
    internship = models.ForeignKey(Internships, models.DO_NOTHING)
    building = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    floor = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    room_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    window_login_account = models.BooleanField(blank=True, null=True)
    email_account = models.BooleanField(blank=True, null=True)
    print_quota = models.BooleanField()
    linux_account = models.BooleanField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    mac_address = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    purpose_it_account = models.CharField(db_column='purpose_IT_account', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    application_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    apply_date = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pdf_form = models.BinaryField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'login_proforma'


class NcpAccomodationApproval(models.Model):
    ncp_allotted_id = models.AutoField(primary_key=True)
    ncp_chk = models.ForeignKey('NcpAccomodationCheck', models.DO_NOTHING)
    room_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    allotment_startdate = models.DateField(blank=True, null=True)
    allotment_enddate = models.DateField(blank=True, null=True)
    priority_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ncp_accomodation_approval'


class NcpAccomodationCheck(models.Model):
    ncp_chk_id = models.AutoField(primary_key=True)
    caad_hr3 = models.ForeignKey(CaadAccomodationVerification, models.DO_NOTHING)
    no_room_allotted_sop = models.IntegerField(blank=True, null=True)
    total_room_allotted = models.IntegerField(blank=True, null=True)
    space_available_room = models.IntegerField(blank=True, null=True)
    space_for_total_student = models.IntegerField(blank=True, null=True)
    availability = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ncp_accomodation_check'


class NcpDues(models.Model):
    dues_id = models.AutoField(primary_key=True)
    it_branch = models.BooleanField(blank=True, null=True)
    ncpemployee_id = models.IntegerField(blank=True, null=True)
    mehanical_workshop = models.BooleanField(blank=True, null=True)
    finance_branch = models.BooleanField(blank=True, null=True)
    security_branch = models.BooleanField(blank=True, null=True)
    hr_branch = models.BooleanField(blank=True, null=True)
    transport_section = models.BooleanField(blank=True, null=True)
    telephone_exchange = models.BooleanField(blank=True, null=True)
    store_branch = models.BooleanField(blank=True, null=True)
    estate_branch = models.BooleanField(blank=True, null=True)
    ncp_libaray = models.BooleanField(blank=True, null=True)
    a_ai_branch = models.BooleanField(db_column='A_AI_branch', blank=True, null=True)  # Field name made lowercase.
    clearance = models.ForeignKey(ClearancePerforma, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ncp_dues'


class NcpPublications(models.Model):
    ncppublications_id = models.AutoField(primary_key=True)
    no_papers_published = models.IntegerField(blank=True, null=True)
    no_papers_accepted = models.IntegerField(blank=True, null=True)
    no_papers_submitted = models.IntegerField(blank=True, null=True)
    no_papers_presented = models.IntegerField(blank=True, null=True)
    no_patents_submitted = models.IntegerField(blank=True, null=True)
    evaluation = models.ForeignKey(EvaluationProforma, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ncp_publications'


class PublicationsList(models.Model):
    publications_id = models.AutoField(primary_key=True)
    publications_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    publications_document = models.BinaryField(blank=True, null=True)
    std_cnic = models.ForeignKey('Student', models.DO_NOTHING, db_column='std_cnic')

    class Meta:
        managed = False
        db_table = 'publications_list'


class Student(models.Model):
    std_cnic = models.CharField(primary_key=True, max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    std_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    std_email = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    std_phone_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    std_password = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    verification_code = models.IntegerField(blank=True, null=True)
    verification_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentPictures(models.Model):
    std_pic_id = models.AutoField(primary_key=True)
    std_cnic = models.ForeignKey(Student, models.DO_NOTHING, db_column='std_cnic')
    image = models.BinaryField(blank=True, null=True)
    img_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_pictures'


class StudentRegistration(models.Model):
    reg_form_id = models.AutoField(primary_key=True)
    std_cnic = models.ForeignKey(Student, models.DO_NOTHING, db_column='std_cnic')
    dob = models.DateField(blank=True, null=True)
    highest_qualification = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    academic_record = models.CharField(db_column='academic_Record', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    present_status = models.CharField(max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    designation = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    university_reg_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    present_university_name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    permanent_address = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    mailing_address = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    landline_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_registration'


class TransportMemberProforma(models.Model):
    transport_form_id = models.AutoField(primary_key=True)
    transport_application_date = models.DateField(blank=True, null=True)
    internship = models.ForeignKey(Internships, models.DO_NOTHING)
    identity = models.ForeignKey(IdentitycardProforma, models.DO_NOTHING, blank=True, null=True)
    transport_req_start_date = models.DateField(blank=True, null=True)
    transport_req_end_date = models.DateField(blank=True, null=True)
    pick_drop_point = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lab_contact_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    application_status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    remarks = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    pdf_form = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transport_member_proforma'


class UniversitySupervisor(models.Model):
    supervisor_id = models.AutoField(primary_key=True)
    supervisor_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    supervisor_designation = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    supervisor_phone_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    supervisor_fax_no = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    supervisor_email = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    supervisor_department = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'university_supervisor'