from django.contrib import admin
from .models import Payment
# Register your models here.

class PaymnetToAdmin(admin.ModelAdmin):
    list_display = [ 'Photogarpher','month', 'year', 'expiration_date'  ]


admin.site.register(Payment,PaymnetToAdmin)
    