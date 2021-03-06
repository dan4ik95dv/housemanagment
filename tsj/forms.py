# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *
from .streets import STREET_CHOICES


class CompanyForm(ModelForm):
    username = forms.CharField(label=u"Имя пользователя", required=True)
    password = forms.CharField(label=u"Пароль", widget=forms.PasswordInput(), required=True)

    class Meta:
        model = Company
        exclude = ('user', 'services')


class AddHouseForm(ModelForm):
    #house = forms.ChoiceField(label=u"Дома", choices=STREET_CHOICES,#((house.id, house) for house in House.objects.all()),
    #    widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = House



class AddResidentForm(forms.Form):
    resident = forms.ChoiceField(label=u"Жилец", choices=((resident.id, resident) for resident in Resident.objects.all()),
        widget=forms.Select(attrs={'class': 'form-control'}))


class AddServiceCompanyForm(forms.Form):
    service = forms.ChoiceField(label=u"Подрядчик", choices=((service.id, service) for service in ServiceCompany.objects.all()),
        widget=forms.Select(attrs={'class': 'form-control'}))


class EmployerForm(ModelForm):
    class Meta:
        exclude = ["company"]
        model = Employer


class AddServiceEmployerForm(forms.Form):
    employer = forms.ChoiceField(label=u"Сотрудник", choices=((employer.id, employer) for employer in Employer.objects.all()),
        widget=forms.Select(attrs={'class': 'form-control'}))


class AddNotificationForm(forms.Form):
    notify = forms.IntegerField()


class NotifyForm(ModelForm):
    class Meta:
        exclude = ["pub_date"]
        model = Notification


class ResidentForm(ModelForm):
    username = forms.CharField(label='Имя пользователя', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label=u'Пароль', required=True)

    class Meta:
        model = Resident
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'middle_name',
            'phone',
            'house',
            'flat',
            'bill_numb',
            'passport',
            'registration')

class MeterForm(forms.ModelForm):
    meter_type = forms.ChoiceField(label=u"Тип счетчика", choices=((types.id, types) for types in MeterType.objects.all()),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = MeterReadingHistory
        fields = ('value',)
        exclude = ('meter_type', )
    
class HouseAccountForm(forms.ModelForm):

    class Meta:
        model = HouseAccount
        fields = ('account_change',)

class EmployerRequestForm(forms.ModelForm):
    employer = forms.ChoiceField(label=u"Работник", choices=((emp.id, emp) for emp in Employer.objects.all()),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = EmployerRequest
        fields = ('reason', )
