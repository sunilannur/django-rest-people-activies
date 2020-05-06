from rest_framework import serializers
from .models import * as member_models



class ActivityPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = member_models.ActivityPeriod
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    # activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = member_models.User
        fields = '__all__'

    def get_activity_periods(self, user_obj):
        return ActivityPeriod(user_obj.activity_periods.all()).data