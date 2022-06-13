from rest_framework import serializers
# ============================================================================ #
from .models import Enquiry


# ============================ ENQUIRY SERIALIZER ============================ #


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = "__all__"