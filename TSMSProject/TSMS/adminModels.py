from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, TextField

# from TSMSVirtual.TSMSProject.TSMS.models import ClubsAndSociety


'''NOTE: THE ADMIN WILL USE THIS MODELS TO MANAGE THE SYSTEM'''
'''NOTE: THE ADMIN WILL USE THIS MODELS TO MANAGE THE SYSTEM'''


class Teacher(models.Model):
    '''Model to add teacher'''
    teacher_id = models.CharField(
        max_length=20, default='TSM-ID-001', primary_key=False)
    teacher_name = models.CharField(max_length=100)
    teacher_gender = models.CharField(max_length=15)
    teacher_d_o_b = models.DateField()
    teacher_mobile = models.CharField(max_length=15, null=True)
    teacher_join_date = models.DateField()
    teacher_qualification = models.CharField(max_length=20, null=True)
    teacher_experience = models.CharField(max_length=100, null=True)
    teacher_address = models.CharField(
        max_length=200, null=True)
    teacher_city = models.CharField(max_length=50, null=True)
    teacher_region = models.CharField(max_length=50, null=True)
    teacher_digital_address = models.CharField(blank=True, max_length=50)
    teacher_country = models.CharField(blank=True, max_length=50, )
    teacher_class = models.CharField(max_length=50, null=True)
    teacher_subject = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
# NOTE: TEACHER MODEL ENDS HERE


class Student(models.Model):
    '''Model to add the student'''
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    # std_id = models.UUIDField(editable=False)
    std_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    d_o_b = models.DateField()
    std_class = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    join_date = models.DateField()
    mobile = models.CharField(max_length=15)
    admision_num = models.CharField(max_length=50)
    house = models.CharField(max_length=100)
    department = models.CharField(max_length=100, null=True)
    # Parent information (father)
    father_name = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=15)
    father_email = models.CharField(max_length=100)
    father_address = models.CharField(max_length=200)
    # Parent information (mother)
    mother_name = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=15)
    mother_email = models.CharField(max_length=100)
    mother_address = models.CharField(max_length=200)

    def __str__(self):
        return self.fname + ' ' + self.lname
# NOTE: STUDENT MODEL ENDS HERE!


class Star_student(models.Model):
    '''Model to add the star student'''
    full_name = models.CharField(max_length=150)
    index = models.CharField(max_length=30)
    best_six = models.IntegerField()
    overall_eight = models.IntegerField()
    year = models.DateField()
    # std_id = models.UUIDField(editable=False)


class Subject(models.Model):
    '''Model to add suject'''
    name = models.CharField(max_length=20)
    subj_id = models.CharField(max_length=20)
    std_class = models.CharField(max_length=20)

    def __str__(self):
        return self.name
# NOTE: SUBJECT MODEL ENDS HERE!


class Assignment(models.Model):
    '''Model to enable teachers give assignment and students to access the assignment'''
    teacher = models.CharField(max_length=100)
    assignment_name = models.CharField(max_length=150)
    assignment_description = models.CharField(max_length=2000)
    assignment_start_date = models.DateField()
    assignment_end_date = models.DateField()
    assignment_grade = models.CharField(max_length=20, null=True)
    assignment_class = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.assignment_name + ' - ' + self.teacher


class Department(models.Model):
    '''Model to add the department'''
    # dep_Id = models.UUIDField(editable=False)
    dep_Id = models.CharField(max_length=20)
    dep_name = models.CharField(max_length=50)
    h_o_d = models.CharField(max_length=50)
    date_started = models.DateField()
    num_of_stud = models.IntegerField()

    def __str__(self):
        return self.dep_name
#   NOTE: MODEL FOR DEPARTMENT ENDS HERE!


class Exam(models.Model):
    '''Model to add exam'''
    exam_name = models.CharField(max_length=20)
    exam_class = models.CharField(max_length=50)
    exam_subject = models.CharField(max_length=100)
    exam_start_time = models.TimeField()
    exam_end_time = models.TimeField()
    exam_date = models.DateField()

    def __str__(self):
        return self.exam_name


class Event(models.Model):
    '''Model to add event'''
    event_heading = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_content = models.TextField()

    def __str__(self):
        return self.event_heading


class Timetable(models.Model):
    '''Model to add timetable'''
    form = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    day = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.day


class Reguest_review(models.Model):
    '''Model to add review'''
    review_student = models.CharField(max_length=200)
    review_department = models.CharField(max_length=200)
    review_class = models.CharField(max_length=100)
    review_mail = models.CharField(max_length=100)
    review_number = models.CharField(max_length=20)

    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.review_subject + " on " + self.review_student


class Recieved_mail(models.Model):
    '''Model to add recieved mails'''
    # mail_name = models.CharField(max_length=100, null=True)
    mail_subject = models.CharField(max_length=200)
    sender_mail = models.CharField(max_length=100, null=True)
    mail_phone = models.CharField(max_length=100)
    mail_body = models.TextField()
    mail_date = models.DateField()

    def __str__(self):
        return self.mail_subject


class Course_material(models.Model):
    '''Model to add course material'''
    material_heading = models.CharField(max_length=300)
    material_file = models.FileField(upload_to='course_material/')
    material_class = models.CharField(max_length=100)
    material_teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.content_heading
