from rest_framework import serializers
from .models import *
from binascii import unhexlify

class HexBinaryField(serializers.Field):
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        try:
            return unhexlify(data)
        except Exception as e:
            raise serializers.ValidationError(str(e))


class AccomodationProformaSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccomodationProforma
        fields = '__all__'
        # depth=2


class AccomodationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccomodationType
        fields = '__all__'


class CaadAccomodationVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadAccomodationVerification
        fields = '__all__'


class CaadExtensionVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadExtensionVerification
        fields = '__all__'


class CaadIdentityVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadIdentityVerification
        fields = '__all__'

class CaadEvaluationVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadEvaluationVerification
        fields = '__all__'

class CaadClearanceVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadClearanceVerification
        fields = '__all__'
class CaadLatesittingVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadLatesittingVerification
        fields = '__all__'
class CaadRegistrationVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadRegistrationVerification
        fields = '__all__'
class CaadTransportVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaadTransportVerification
        fields = '__all__'


class ClearancePerformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClearancePerforma
        fields = '__all__'




class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class DocumentsUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentsUpload
        fields = '__all__'

class NcpPublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcpPublications
        fields = '__all__'

class EvaluationProformaSerializer(serializers.ModelSerializer):
     publications = NcpPublicationsSerializer(many=True, read_only=True)
     class Meta:
        model = EvaluationProforma
        fields = '__all__'
        #depth=2

class ExtensionProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionProforma
        fields = '__all__'


class HostedresearcherCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HostedresearcherCategory
        fields = '__all__'


class IdentitycardProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentitycardProforma
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'


class StudentPicturesSerializer(serializers.ModelSerializer):
    # image = HexBinaryField(required=False)
    class Meta:
        model = StudentPictures
        #fields = ('image',)
        fields = '__all__'
 
   

class StudentRegistrationSerializer(serializers.ModelSerializer):
    #student = StudentSerializer()
    class Meta:
        model = StudentRegistration
        fields = '__all__'
        depth =2


class InternshipsSerializer(serializers.ModelSerializer):
    #registration = StudentRegistrationSerializer(read_only= True)
    class Meta:
        model = Internships
        fields = '__all__'
        depth=2



class ItDeptLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItDeptLogin
        fields = '__all__'



class LateSittingProformaSerializer(serializers.ModelSerializer):
    # internship = InternshipsSerializer(read_only= True)
    class Meta:
        model = LateSittingProforma
        fields = '__all__'
        depth = 2


class LoginProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginProforma
        fields = '__all__'
class NcpAccomodationApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcpAccomodationApproval
        fields = '__all__'


class NcpAccomodationCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcpAccomodationCheck
        fields = '__all__'


class NcpDuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NcpDues
        fields = '__all__'





class PublicationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationsList
        fields = '__all__'
    





class TransportMemberProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportMemberProforma
        fields = '__all__'


class UniversitySupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversitySupervisor
        fields = '__all__'