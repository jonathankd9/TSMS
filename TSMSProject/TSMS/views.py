import csv
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.forms import ModelForm, inlineformset_factory
from django.core.mail import send_mail

from .adminForms import *
from .models import *
from .adminModels import *
from TSMSProject import settings

# import request for the api manipulation
# import requests

# NOTE: FIX THIS


def register_alumni(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('create_user')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('homepage')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email,)
                    user.groups.add(Group.objects.get(name='alumni'))
                    user.save()
                    # # Login after register
                    login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('alumniDashboard')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('create_user')

        alumni = AlumniForm(request.POST or None)
        # if alumni.is_valid():
        alumni.save()
        messages.success(request, 'Alumni added successfully')
        return redirect('admin_alumni')
    return render(request, 'admin/alumni.html')


def process_create_user(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        group = request.POST['group']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('create_user')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('create_user')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    print('Before User.save()')
                    user.save()
                    print('After User.save()')
                    user.groups.add(Group.objects.get(name=group))
                    print('After user.groups.add()')

                    messages.success(
                        request, 'User account created successfully')
                    return redirect('create_user')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('create_user')
    return render(request, 'admin/create_user.html', {})

# Logs in user


def loginPage(request):
    # user groups
    staff = 'teacher'
    student = 'student'
    parent = 'parent'
    alumni = 'alumni'
    admin_tsms = 'admin_tsms'
    accounts = 'accounts'
    helpdesk = 'helpdesk'
    # accounts = 'accounts'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            if user.groups.filter(name=staff).exists():
                return redirect('teacherDashboard')
            elif user.groups.filter(name=student).exists():
                return redirect('studentDashboard')

            elif user.groups.filter(name=parent).exists():
                return redirect('parentDashboard')

            elif user.groups.filter(name=alumni).exists():
                return redirect('alumniDashboard')

            elif user.groups.filter(name=admin_tsms).exists():
                return redirect('admin_tsms')

            elif user.groups.filter(name=helpdesk).exists():
                return redirect('helpDeskDashboard')

            elif user.groups.filter(name=accounts).exists():
                return redirect('accountsDashboard')

            else:
                return redirect('homepage')
        else:
            messages.error(request, 'Username or Password is incorrect')
            # return render(request, 'homepage/home.html', {})
            return redirect('homepage')

    context = {}

    return render(request, 'homepage/home.html', context)

# Log the user out


def logoutUser(request):
    logout(request)
    return redirect('homepage')

#  upload student into database


# def process_payment(request):

#     url = 'https://payhubghana.io/api/v1.0/debit_mobile_account/'

#     # request header
#     header = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Token ' + settings.PAYHUB_TOKEN,
#     }


#     if request.method == 'POST':
#         mobile_number = request.POST['mobile_number']
#         amount = request.POST['amount']
#         network_code = request.POST['network_code']
#         reference = request.POST['reference']
#         wallet_id = request.POST['wallet_id']
#         transaction_id = request.POST['transaction_id']

#         params = {
#             'mobile_number': mobile_number,
#             'amount': amount,
#             'network_code': network_code,
#             'reference': reference,
#             'wallet_id': wallet_id,
#             'transaction_id': transaction_id
#         }

#         response = requests.post(url, json=params, headers=header)
#         data = response.json()

#     return HttpResponse('<h1>Processing Payment<h1 />')


def upload_student(request):
    if request.method == "POST":
        student = StudentForm(request.POST or None)
        # if student.is_valid():
        student.save()
        messages.success(request, 'Student added successfully')
        return redirect('admin_students')
    return render(request, 'admin/add-student.html')

#  upload student into database


def upload_teacher(request):
    if request.method == "POST":
        teacher = TeacherForm(request.POST or None)
        # if teacher.is_valid():
        teacher.save()
        messages.success(request, 'Teacher added successfully')
        return redirect('admin_teachers')
    return render(request, 'admin/add-teacher.html')


def upload_department(request):
    if request.method == "POST":
        department = DepartmentForm(request.POST or None)
        # if department.is_valid():
        department.save()
        messages.success(request, 'Department added successfully')
        return redirect('admin_departments')
    return render(request, 'admin/departments.html')


def upload_event(request):
    if request.method == "POST":
        event = EventForm(request.POST or None)
        # if event.is_valid():
        event.save()
        messages.success(request, 'Event added successfully')
        return redirect('admin_events')
    return render(request, 'admin/event.html')


def upload_exams(request):
    if request.method == "POST":
        exam = ExamForm(request.POST or None)
        # if exam.is_valid() or not(exam.is_valid()):
        exam.save()
        messages.success(request, 'Exam added successfully')
        return redirect('admin_exams')
    return render(request, 'admin/exams.html')


def upload_timetable(request):
    if request.method == "POST":
        timetable = TimetableForm(request.POST or None)
        # if timetable.is_valid():
        timetable.save()
        messages.success(request, 'Schedule added to timetable successfully')
        return redirect('admin_timetable')
    return render(request, 'admin/timetables.html', {})


def upload_subject(request):
    if request.method == "POST":
        subject = SubjectForm(request.POST or None)
        # if subject.is_valid():
        subject.save()
        messages.success(request, 'subject added successfully')
        return redirect('admin_subjects')
    return render(request, 'admin/subjects.html')


def upload_event(request):
    if request.method == "POST":
        event = EventForm(request.POST or None)
        # if event.is_valid():
        event.save()
        messages.success(request, 'Event added successfully')
        return redirect('admin_events')
    return render(request, 'admin/add-event.html')


def upload_mail(request):
    if request.method == "POST":
        mail = Recieved_mailForm(request.POST or None)
        # if mail.is_valid():
        mail.save()
        messages.success(request, 'Mail sent successfully')
        return redirect('homepage')
    return render(request, 'homepage/home.html')


def upload_request_review(request):
    mail_recipients = [
        'pskyeremanteng@st.ug.edu.gh',
        'princesamuelpks@gmail.com',
        'princeofori723@gmail.com',
        'jkd6735@gmail.com',
    ]

    if request.method == "POST":
        phone = request.POST['review_number']
        subject = f'PARENT WITH {phone} REQUESTS A REVIEW'
        student = request.POST['review_student']
        std_class = request.POST['review_class']
        std_department = request.POST['review_department']
        body = f'I WISH TO REQUEST FOR A REVIEW ON MY WARD. Student: {student} \nClass: {std_class} \nDepartment: {std_department}'
        # mail = request.POST['review_mail']

        # to_be_sent = send_mail(
        #     subject,
        #     body,
        #     settings.EMAIL_HOST_USER,
        #     mail_recipients,
        # )

        # to_be_sent.fail_silently = False
        # to_be_sent.send()

        review = Reguest_reviewForm(request.POST or None)
        # if review.is_valid():
        review.save()
        messages.success(
            request, 'Request for review sent successfully. You will be replied to shortly.')
        return redirect('parentDashboard')
    return render(request, 'parent/request-review.html')


def homepage(request):

    carousels = FrontPageCarousel.objects.all()
    latest_news = LatestNews.objects.all().order_by('-id')[:4]
    abouts = About.objects.all().order_by('-id')[:1]
    courses = Course.objects.all().order_by('-id')
    departments = HomepageDepartment.objects.all().order_by('-id')
    heads = Head.objects.all().order_by('-id')
    reviews = StudentReview.objects.all().order_by('-id')[:5]
    upcoming_events = UpcomingEvent.objects.all().order_by('-id')[:6]
    newses = News.objects.all().order_by('-id')[:10]

    # day_of_date = upcoming_events.event_date.strftime("%A")

    context = {
        'carousels': carousels,
        'latest_news': latest_news,
        'abouts': abouts,
        'courses': courses,
        'departments': departments,
        'heads': heads,
        'reviews': reviews,
        'upcoming_events': upcoming_events,
        'newses': newses,

    }

    return render(request, 'homepage/home.html', context)
# NOTE: HOMEPAGE ENDS HERE


def teachers(request):
    return render(request, 'homepage/teachers.html', {})


def admin_tsms(request):
    num_of_students = Student.objects.all().count()
    num_of_departments = Department.objects.all().count()
    num_of_subjects = Subject.objects.all().count()
    num_of_teachers = Teacher.objects.all().count()

    students = Star_student.objects.all().order_by('-id')

    context = {
        'num_of_students': num_of_students,
        'num_of_departments': num_of_departments,
        'num_of_subjects': num_of_subjects,
        'num_of_teachers': num_of_teachers,
        'students': students
    }
    return render(request, 'admin/home.html', context)


def admin_students(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'admin/students.html', {'students': students})


def star_students(request):
    students = Star_student.objects.all().order_by('-id')
    return render(request, 'admin/star_students.html', {'students': students})


def add_star_std(request):
    return render(request, 'admin/add_star_student.html')


def upload_star_student(request):
    if request.method == "POST":
        student = Star_studentForm(request.POST or None)
        # if student.is_valid():
        student.save()
        messages.success(request, 'Star Student added successfully')
        return redirect('star_students')
    return render(request, 'admin/add_star_student.html')


def add_student(request):
    return render(request, 'admin/add-student.html', {})


def admin_teachers(request):
    teachers = Teacher.objects.all().order_by('-id')
    return render(request, 'admin/teachers.html', {'teachers': teachers})


def add_teachers(request):
    return render(request, 'admin/add-teacher.html', {})


def admin_departments(request):
    departments = Department.objects.all()
    return render(request, 'admin/departments.html', {'departments': departments})


def add_department(request):
    return render(request, 'admin/add-department.html', {})


def admin_exams(request):
    exams = Exam.objects.all()
    return render(request, 'admin/exam.html', {'exams': exams})


def add_exam(request):
    return render(request, 'admin/add-exam.html', {})


def admin_events(request):
    events = Event.objects.all().order_by('-id')
    return render(request, 'admin/event.html', {'events': events})


def add_event(request):
    return render(request, 'admin/add-event.html', {})


def admin_subjects(request):

    subjects = Subject.objects.all()

    return render(request, 'admin/subjects.html', {'subjects': subjects})


def add_subject(request):
    return render(request, 'admin/add-subject.html', {})


def admin_timetable(request):
    timetable = Timetable.objects.all().order_by('form', 'day', 'start_time')
    return render(request, 'admin/timetable.html', {'timetable': timetable})


def add_timetable(request):
    return render(request, 'admin/add-timetable.html', {})


def admin_fees(request):
    return render(request, 'admin/fees.html', {})


def create_user(request):
    # Pulls out the user creation form
    return render(request, 'admin/create_user.html', {})

# def add_timetable(request):
#     return render(request, 'admin/add-timetable.html', {})


# NOTE: ADMIN PANEL ENDS HERE

# teacher view
def teacherDashboard(request):
    # make database query here

    # database query ends here!

    return render(request, 'teacher/teacher.html', {})
# NOTE: TEACHER PANEL ENDS HERE


def teacher_assignments(request):
    assignments = Assignment.objects.all().order_by('-id')
    return render(request, 'teacher/assignments.html', {'assignments': assignments})


def add_assignment(request):
    return render(request, 'teacher/add-assignment.html', {})


def upload_assignment(request):
    if request.method == "POST":
        assignment = AssignmentForm(request.POST or None)
        # if assignment.is_valid():
        assignment.save()
        messages.success(request, 'Assignment added successfully')
        return redirect('teacher_assignments')
    return render(request, 'teacher/add-assignment.html', {})


def teacher_course_material(request):
    assignments = Assignment.objects.all().order_by('-id')
    return render(request, 'teacher/course_materials.html', {'assignments': assignments})


def add_material(request):
    return render(request, 'teacher/add-course_material.html', {})


def teacher_internal_performance(request):
    return render(request, 'teacher/internal-performance.html', {})


def teacher_wassce_performance(request):
    return render(request, 'teacher/teacher-wassce-performance.html', {})


def teacher_exams(request):
    exams = Exam.objects.all()
    return render(request, 'teacher/exam.html', {'exams': exams})


def teacher_timetable(request):
    timetable = Timetable.objects.all().order_by('form', 'day', 'start_time')
    return render(request, 'teacher/timetable.html', {'timetable': timetable})


def teacher_event(request):
    events = Event.objects.all().order_by('-id')
    return render(request, 'teacher/event.html', {'events': events})


def teacher_add_event(request):
    return render(request, 'teacher/add-event.html', {})


def studentDashboard(request):
    num_of_events = Event.objects.all().count()
    num_of_subjects = Subject.objects.all().count()
    num_of_schedules = Timetable.objects.all().count()
    num_of_assignments = Assignment.objects.all().count()
    current_assignments = Assignment.objects.all().order_by('-id')[:3]
    context = {
        'num_of_events': num_of_events,
        'num_of_subjects': num_of_subjects,
        'num_of_schedules': num_of_schedules,
        'num_of_assignments': num_of_assignments,
        'current_assignments': current_assignments,
    }
    return render(request, 'student/index.html', context)
# NOTE: student PANEL ENDS HERE


def student_exams(request):
    exams = Exam.objects.all()
    return render(request, 'student/exam.html', {'exams': exams})


def student_event(request):
    events = Event.objects.all().order_by('-id')
    return render(request, 'student/event.html', {'events': events})

# def student_department(request):
#     return render(request, 'student/department.html', {})


def student_timetable(request):
    timetable = Timetable.objects.all().order_by('form', 'day', 'start_time')
    return render(request, 'student/time-table.html', {'timetable': timetable})


def student_assignment(request):
    assignments = Assignment.objects.all().order_by('-id')
    return render(request, 'student/assignment.html', {'assignments': assignments})


def accountsDashboard(request):

    return render(request, 'accounts/index.html', {})
# NOTE: acounts PANEL ENDS HERE


def accounts_fees(request):
    return render(request, 'accounts/fees-collections.html', {})


def cmanager(request):
    # make database query here

    # database quesry ends here!
    return render(request, 'cmanager/index.html', {})


def cmanager_carousel(request):
    # make database query here

    # database quesry ends here!
    return render(request, 'cmanager/carousel.html', {})


def cmanager_courses(request):
    # make database query here

    # database quesry ends here!
    return render(request, 'cmanager/courses.html', {})


def cmanager_departments(request):
    # make database query here

    # database quesry ends here!
    return render(request, 'cmanager/departments.html', {})


def cmanager_experience_heads(request):
    # make database query here

    # database quesry ends here!
    return render(request, 'cmanager/experience-heads.html', {})


def cmanager_latest_news(request):
    # make database query here

    # database quesry ends here!
    return render(request, 'cmanager/latest-news.html', {})


def cmanager_students_review(request):
    # make database query here

    # database quesry ends here!
    return render(request, 'cmanager/students-review.html', {})


# NOTE: cmanager PANEL ENDS HERE


def parentDashboard(request):
    # make database query here

    # database query ends here!

    return render(request, 'parent/index.html', {})
# NOTE: parent PANEL ENDS HERE


def parent_request_review(request):
    # make database query here

    # database query ends here!
    return render(request, 'parent/request-review.html', {})


def parent_make_payment(request):
    # make database query here

    # database query ends here!

    return render(request, 'parent/make-payment.html', {})


def alumniDashboard(request):
    # make database query here

    # database quesry ends here!
    star_students = Star_student.objects.all().order_by('-id')
    num_of_department = Department.objects.all().count()
    num_of_teachers = Teacher.objects.all().count()
    num_of_students = Student.objects.all().count()

    context = {
        'star_students': star_students,
        'num_of_department': num_of_department,
        'num_of_teachers': num_of_teachers,
        'num_of_students': num_of_students,
    }

    return render(request, 'alumni/index.html', context)
# NOTE: alumni PANEL ENDS HERE


def alumni_dues(request):
    return render(request, 'alumni/dues.html', {})


def alumni_event(request):
    events = Event.objects.all().order_by('-id')
    return render(request, 'alumni/event.html', {'events': events})


def alumni_internal_assessment(request):
    return render(request, 'alumni/internal-assessment.html', {})


def alumni_wassce_assessment(request):
    return render(request, 'alumni/wassce-assessment.html', {})


def helpDeskDashboard(request):

    mails = Recieved_mail.objects.all().order_by('-id')
    reviews = Reguest_review.objects.all().order_by('-id')

    num_of_mails = Recieved_mail.objects.all().count()
    num_of_reviews = Reguest_review.objects.all().count()

    context = {
        'mails': mails, 'reviews': reviews,
        'num_of_mails': num_of_mails,
        'num_of_reviews': num_of_reviews
    }

    return render(request, 'help_desk/index.html', context)


def helpDesk_received_mails(request):

    mails = Recieved_mail.objects.all().order_by('-id')
    context = {
        'mails': mails,
    }
    return render(request, 'help_desk/received_mails.html', context)


def helpDesk_review_requests(request):
    review_requests = Reguest_review.objects.all().order_by('-id')

    context = {
        'review_requests': review_requests,
    }

    return render(request, 'help_desk/review_requests.html', context)


# NOTE: helpdesk PANEL ENDS HERE


def export_student_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_list.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'NAME', 'GENDER', 'CLASS',
                    'D_O_B', 'HOUSE', 'DEPARTMENT', ])

    students = Student.objects.all().order_by('-id')

    for student in students:
        writer.writerow(
            [
                student.std_id,
                student.fname + student.lname,
                student.gender,
                student.std_class,
                student.d_o_b,
                student.house,
                student.department,
            ]
        )

    return response


def export_star_student_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="star_student_list.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            'NAME',
            'INDEX NUMBER',
            'BEST 6',
            'OVERALL 8',
            'YEAR',
        ]

    )

    students = Star_student.objects.all().order_by('-id')
    for student in students:
        writer.writerow(
            [
                student.full_name,
                student.index,
                student.best_six,
                student.overall_eight,
                student.year,
            ]
        )

    return response


def export_teacher_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="teacher_list.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            'ID',
            'NAME',
            'CLASS',
            'GENDER',
            'SUBJECT',
            'MOBILE',
        ]
    )
    teachers = Teacher.objects.all().order_by('-id')
    for teacher in teachers:
        writer.writerow(
            [
                teacher.teacher_id,
                teacher.teacher_name,
                teacher.teacher_class,
                teacher.teacher_gender,
                teacher.teacher_subject,
                teacher.teacher_mobile,
            ]
        )
    return response


def export_department_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="department_list.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            'ID',
            'NAME',
            'H_O_D',
            'DATE STARTED',
            'TOTAL STUDENTS',
        ]
    )
    departments = Department.objects.all().order_by('-id')
    for department in departments:
        writer.writerow(
            [
                department.dep_Id,
                department.dep_name,
                department.h_o_d,
                department.date_started,
                department.num_of_stud,
            ]
        )
    return response


def export_subject_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="subject_list.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            'ID',
            'NAME',
            'CLASS',
        ]
    )

    subjects = Subject.objects.all().order_by('-id')
    for subject in subjects:
        writer.writerow(
            [
                subject.subj_id,
                subject.name,
                subject.std_class,
            ]
        )

    return response


def export_exam_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exam_list.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            'NAME',
            'CLASS',
            'SUBJECT',
            'START TIME',
            'END TIME',
            'DATE',
        ]
    )

    exams = Exam.objects.all().order_by('-id')
    for exam in exams:
        writer.writerow(
            [
                exam.exam_name,
                exam.exam_class,
                exam.exam_subject,
                exam.exam_start_time,
                exam.exam_end_time,
                exam.exam_date,
            ]
        )

    return response


def export_timetable_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="timetable_list.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            'FORM',
            'SUBJECT',
            'TEACHER',
            'DAY',
            'START TIME',
            'END TIME',
        ]
    )

    timetables = Timetable.objects.all().order_by('-id')
    for timetable in timetables:
        writer.writerow(
            [
                timetable.form,
                timetable.subject,
                timetable.teacher,
                timetable.day,
                timetable.start_time,
                timetable.end_time,
            ]
        )

    return response


def export_request_review_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="review_request_list.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            'STUDENT NAME',
            'STUDENT DEPARTMENT',
            'STUDENT CLASS',
            'PARENT MAIL',
            'PARENT NUMBER',
        ]
    )

    request_reviews = Reguest_review.objects.all().order_by('-id')
    for request_review in request_reviews:
        writer.writerow(
            [
                request_review.review_student,
                request_review.review_department,
                request_review.review_class,
                request_review.review_mail,
                request_review.review_number,
            ]
        )

    return response


# def export_department_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="department_list.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            'ID',
            'NAME',
            'H_O_D',
            'DATE STARTED',
            'TOTAL STUDENTS',
        ]
    )
    departments = Department.objects.all().order_by('-id')
    for department in departments:
        writer.writerow(
            [
                department.dep_Id,
                department.dep_name,
                department.h_o_d,
                department.date_started,
                department.num_of_stud,
            ]
        )
    return response
