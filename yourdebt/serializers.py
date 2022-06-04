from email.headerregistry import Group
from rest_framework import serializers, HyperlinkedModelSerializer
from .models import OpenDebt, CloseDebt, Mortgage
from django.contrib.auth.models import User, Group


class OpenDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenDebt
        fields = ('id', 'debt_name', 'amount_owed', 'int_rate','min_payment', 'extra_principal', 'time_topay')
class CloseDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloseDebt
        fields = ('id', 'debt_name', 'amount_owed', 'int_rate','min_payment', 'extra_principal', 'time_topay', 'term')
class MortgageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortgage
        fields = ('id', 'mortgage_name', 'purchase_price', 'down_payment', 'mortgage_term','int_rate', 'property_tax', 'property_insurance', 'PMI', 'first_month','first_year')

class UserSerializer(HyperlinkedModelSerializer):
   class Meta:
    model = User
    fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(HyperlinkedModelSerializer):
   class Meta:
    model = Group
    fields = ('url', 'name')