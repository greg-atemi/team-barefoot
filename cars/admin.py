from django.contrib import admin
from cars.models import Car, Review


class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TIME INFORMATION', {'fields': ['year']}),
        ('CAR INFORMATION', {'fields': ['brand']})
    ]


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('IDENTITY', {'fields': ['first_name', 'surname']}),
        ('RATING', {'fields': ['rating']})
    ]


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
