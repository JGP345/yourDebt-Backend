from django.contrib import admin
from .models import CloseDebt, OpenDebt, Mortgage
# Register your models here.
class OpenDebtAdmin(admin.ModelAdmin):
    list_display = ('debt_name', 'amount_owed', 'int_rate')
class CloseDebtAdmin(admin.ModelAdmin):
    list_display = ('debt_name', 'amount_owed', 'int_rate')
class MortgageAdmin(admin.ModelAdmin):
    list_display = ('mortgage_name', 'purchase_price')

admin.site.register(OpenDebt, OpenDebtAdmin)
admin.site.register(CloseDebt,CloseDebtAdmin)
admin.site.register(Mortgage,MortgageAdmin)