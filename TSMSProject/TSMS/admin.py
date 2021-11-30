from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *  # Imports all the models in models.py
from .adminModels import *  # Imports all the models in adminModels.py
from django.contrib.auth.models import User

# Customizations
admin.site.site_header = "TSMS BACKEND"
admin.site.site_title = "BACKEND"
admin.site.index_title = "TASHTECH | TSMS"

# Register the models so the backend can recognise them
admin.site.register(FrontPageCarousel)
admin.site.register(News)
admin.site.register(Head)
admin.site.register(UpcomingEvent)
admin.site.register(StudentReview)
admin.site.register(Scholarship)
admin.site.register(Facility)
admin.site.register(ClubsAndSociety)
admin.site.register(Course)
admin.site.register(Miscellaneous)

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(Event)
admin.site.register(Timetable)
admin.site.register(Assignment)
admin.site.register(Star_student)
admin.site.register(Course_material)
admin.site.register(Recieved_mail)
admin.site.register(LatestNews)
admin.site.register(About)
admin.site.register(HomepageDepartment)
