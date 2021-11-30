from django.db.models import fields
from django.forms import ModelForm

from .models import *
from .adminModels import *


class StudentForm(ModelForm):
    class Meta():
        model = Student
        fields = [
            'fname',
            'lname',
            'std_id',
            'gender',
            'd_o_b',
            'std_class',
            'religion',
            'join_date',
            'mobile',
            'admision_num',
            'house',
            'department',
            'father_name',
            'father_occupation',
            'father_mobile',
            'father_email',
            'father_address',
            'mother_name',
            'mother_occupation',
            'mother_mobile',
            'mother_email',
            'mother_address',
        ]
# NOTE: STUDENT FORM ENDS HERE


class Star_studentForm(ModelForm):
    class Meta():
        model = Star_student
        fields = [

            'full_name',
            'index',
            'best_six',
            'overall_eight',
            'year',
        ]


class TeacherForm(ModelForm):
    class Meta():
        model = Teacher
        fields = [
            'teacher_id',
            'teacher_name',
            'teacher_gender',
            'teacher_d_o_b',
            'teacher_mobile',
            'teacher_join_date',
            'teacher_qualification',
            'teacher_experience',
            'teacher_address',
            'teacher_city',
            'teacher_region',
            'teacher_digital_address',
            'teacher_country',
            'teacher_class',
            'teacher_subject',
        ]
# NOTE: TEACHERFORM ENDS HERE!


class SubjectForm(ModelForm):
    class Meta():
        model = Subject
        fields = [
            'name',
            'subj_id',
            'std_class',
        ]
# NOTE: SUBJECTFORM ENDS HERE!


class TimetableForm(ModelForm):
    class Meta():
        model = Timetable
        fields = [
            'form',
            'subject',
            'teacher',
            'day',
            'start_time',
            'end_time',
        ]


class AssignmentForm(ModelForm):
    class Meta():
        model = Assignment
        fields = [
            'teacher',
            'assignment_name',
            'assignment_description',
            'assignment_start_date',
            'assignment_end_date',
            'assignment_grade',
            'assignment_class',

        ]


class DepartmentForm(ModelForm):
    class Meta():
        model = Department
        fields = [
            'dep_Id',
            'dep_name',
            'h_o_d',
            'date_started',
            'num_of_stud',
        ]
# NOTE: DEPARTMENTFORM ENDS HERE!


class EventForm(ModelForm):

    class Meta():
        model = Event
        fields = [
            'event_heading',
            'event_date',
            'event_time',
            'event_content',
        ]


class ExamForm(ModelForm):
    class Meta():
        model = Exam
        fields = [
            'exam_name',
            'exam_class',
            'exam_subject',
            'exam_start_time',
            'exam_end_time',
            'exam_date',
        ]


class Reguest_reviewForm(ModelForm):
    class Meta():
        model = Reguest_review
        fields = [
            'review_student',
            'review_department',
            'review_class',
            'review_mail',
            'review_number',
        ]


class Recieved_mailForm(ModelForm):
    class Meta():
        model = Recieved_mail
        fields = [
            'sender_mail',
            'mail_phone',
            'mail_body',
            'mail_date'
        ]


class Course_materialForm(ModelForm):
    class Meta():
        model = Course_material
        fields = [
            'material_heading',
            'material_file',
            'material_class',
            'material_teacher',
        ]
