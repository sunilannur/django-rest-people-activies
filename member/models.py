from django.db import models
import random
import string

def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class User(models.Model):
    id = models.CharField(primary_key=True, default=id_generator, editable=False, max_length=100)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table = "user"

    def __str__(self):
        return self.real_name


class class UserSerializer(serializers.ModelSerializer):

    activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE,related_name='activity_periods')
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
 
    class Meta:
        verbose_name = "activity_period"
        verbose_name_plural = "activity_periods"
        db_table = "activity_period"
    
    def __str__(self):
        return self.member.real_name


