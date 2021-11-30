from django.db import models
from django.db.models.fields import CharField, DateField, TextField


# NOTE: MODELS FOR SITE CONTENTS START HERE!!!!!!!
# NOTE: MODELS FOR SITE CONTENTS START HERE!!!!!!!
class FrontPageCarousel(models.Model):
    '''Model for the frontpage carousel'''
    heading = models.CharField(max_length=200)
    briefIntro = models.TextField()
    picture = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return self.heading
# frontpage model ends here


class News(models.Model):
    '''model for updating news on the site'''
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    overview = models.TextField()
    picture = models.ImageField(upload_to='uploaded_images')
    pub_date = models.DateField()

    def __str__(self):
        return self.title
# news model ends here


class Head(models.Model):
    '''models for updating info on heads of school'''
    name = models.CharField(max_length=200)
    portfolio = models.CharField(max_length=200)
    briefInfo = models.TextField()
    tel = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return self.portfolio + ' - ' + self.name
# heads models ends here


class UpcomingEvent(models.Model):
    '''Model for upcoming events'''
    title = models.CharField(max_length=500)
    briefInfo = models.TextField()
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    picture = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return self.title
# model for upcoming events end here


class Upcoming_courses(models.Model):
    '''Model for upcoming courses'''
    title = models.CharField(max_length=500)
    briefInfo = models.TextField()
    course_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    picture = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return self.title

class StudentReview(models.Model):
    '''Model for students review'''
    name = CharField(max_length=100)
    course = CharField(max_length=100)
    year_batch = DateField()
    # portfolio = TextField()
    message = TextField()
    picture = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return self.name + ' ' + self.course
# students review ends here


class Scholarship(models.Model):
    '''Model for scholarship opportunities'''
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return self.name
# model for scholarship opportunities ends here


class Facility(models.Model):
    '''model for updating the facilities of the school'''
    name = models.CharField(max_length=100)
    briefInfo = models.TextField()
    picture = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return self.name
# Facility model ends here


class ClubsAndSociety(models.Model):
    '''model for updating clubs and societies in the school'''
    name = models.CharField(max_length=100)
    briefInfo = models.TextField()
    patron = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return self.name
# Clubs and Scociety model ends here


class Course(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.TextField(null=True)
    description = models.TextField()
    picture = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return self.name


class Miscellaneous(models.Model):
    number = models.CharField(max_length=10)
    footerDescription = models.TextField()
    emailAddress = models.EmailField()

    def __str__(self):
        return 'Miscellaneous items: ' + str(self.id)

# NOTE: MODELS FOR SITE CONTENTS ENDS HERE!!!!!!!
# NOTE: MODELS FOR SITE CONTENTS ENDS HERE!!!!!!!


class LatestNews(models.Model):
    headline = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.headline


class About(models.Model):
    main_heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.main_heading


class HomepageDepartment(models.Model):
    name = models.CharField(max_length=200)
    num_of_courses = models.IntegerField()
    picture = models.ImageField(upload_to='uploaded_images')
    h_o_d = models.CharField(max_length=200)

    def __str__(self):
        return self.name
