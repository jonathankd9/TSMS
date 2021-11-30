# SITE LEVEL URLS
from django.urls import path
from . import views

urlpatterns = [
    # NOTE: Navigates to the Homepage of the site
    path('', views.homepage, name='homepage'),
    path('home/teachers', views.teachers, name='teachers'),




    # NOTE: Navigates to the Login page of the site
    #     path('register_alumni/', views.register_alumni, name='register_alumni'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('upload_mail', views.upload_mail, name='upload_mail'),

    # NOTE:Handles navigation on the admin dashboard
    path('admin_tsms/', views.admin_tsms, name='admin_tsms'),
    path('admin_tsms/create_user', views.create_user, name='create_user'),
    path('admin_tsms/process_create_user',
         views.process_create_user, name='process_create_user'),

    path('admin_tsms/admin_students', views.admin_students, name='admin_students'),
    path('admin_tsms/add_student', views.add_student, name='add_student'),

    path('admin_tsms/admin_departments',
         views.admin_departments, name='admin_departments'),
    path('admin_tsms/add_department', views.add_department, name='add_department'),

    path('admin_tsms/admin_subjects', views.admin_subjects, name='admin_subjects'),
    path('admin_tsms/add_subject', views.add_subject, name='add_subject'),

    path('admin_tsms/teachers', views.admin_teachers, name='admin_teachers'),
    path('admin_tsms/add_teachers', views.add_teachers, name='add_teachers'),

    path('admin_tsms/admin_exams', views.admin_exams, name='admin_exams'),
    path('admin_tsms/add_exam', views.add_exam, name='add_exam'),

    path('admin_tsms/admin_events', views.admin_events, name='admin_events'),
    path('admin_tsms/add_event', views.add_event, name='add_event'),

    path('admin_tsms/admin_timetable',
         views.admin_timetable, name='admin_timetable'),
    path('admin_tsms/add_timetable', views.add_timetable, name='add_timetable'),

    path('admin_tsms/admin_fees', views.admin_fees, name='admin_fees'),

    path('admin_tsms/add_star_std',
         views.add_star_std, name='add_star_std'),

    path('admin_tsms/star_students', views.star_students, name='star_students'),

    path('admin_tsms/upload_star_student',
         views.upload_star_student, name='upload_star_student'),

    # NOTE: HANDLES USER UPLOADS TO DATABASE
    path('admin_tsms/upload_student/',
         views.upload_student, name='upload_student'),
    path('admin_tsms/upload_teacher/',
         views.upload_teacher, name='upload_teacher'),
    path('admin_tsms/upload_department/',
         views.upload_department, name='upload_department'),
    path('admin_tsms/upload_event/', views.upload_event, name='upload_event'),
    path('admin_tsms/upload_exams/', views.upload_exams, name='upload_exams'),
    path('admin_tsms/upload_timetable/',
         views.upload_timetable, name='upload_timetable'),
    path('admin_tsms/upload_subject/',
         views.upload_subject, name='upload_subject'),


    # NOTE: Handles navigation on the teacher's dashboard
    path('teacherDashboard/', views.teacherDashboard, name='teacherDashboard'),
    path('teacher/teacher_assignments',
         views.teacher_assignments, name='teacher_assignments'),
    path('teacher/add_assignment', views.add_assignment, name='add_assignment'),
    path('teacher/upload_assignment',
         views.upload_assignment, name='upload_assignment'),

    path('teacher/teacher_course_material',
         views.teacher_course_material, name='teacher_course_material'),
    path('teacher/add_material', views.add_material, name='add_material'),
    path('teacher/internal_performance', views.teacher_internal_performance, name='teacher_internal_performance'
         ),
    path('teacher/wassce_performance', views.teacher_wassce_performance,
         name='teacher_wassce_performance'),
    path('teacher/teacher_exams', views.teacher_exams, name='teacher_exams'),
    path('teacher/teacher_timetable',
         views.teacher_timetable, name='teacher_timetable'),
    path('teacher/teacher_event', views.teacher_event, name='teacher_event'),
    path('teacher/teacher_add_event',
         views.teacher_add_event, name='teacher_add_event'),


    # NOTE: Handles navigation on the student's dashboard
    path('studentDashboard/', views.studentDashboard, name='studentDashboard'),
    path('student/student_exams', views.student_exams, name='student_exams'),
    path('student/student_event', views.student_event, name='student_event'),
    path('student/student_assignment',
         views.student_assignment, name='student_assignment'),
    path('student/student_timetable',
         views.student_timetable, name='student_timetable'),
    #path('student/student_depmtList',views.student_depmtList, name='student_depmtList'),



    # NOTE: Handles navigagions on the helpdesk dashboard
    path('helpDeskDashboard', views.helpDeskDashboard, name='helpDeskDashboard'),
    path('helpDeskDashboard/received_mails',
         views.helpDesk_received_mails, name='helpDesk_received_mails'),
    path('helpDeskDashboard/review_requests',
         views.helpDesk_review_requests, name='helpDesk_review_requests'),



    # NOTE: Handles navigation on the ACCOUNTS dashboard
    path('accountsDashboard', views.accountsDashboard, name='accountsDashboard'),
    path('accounts/fees', views.accounts_fees, name='accounts_fees'),

    # NOTE: Handles navigation on the content manager's dashboard
    path('cmanager/', views.cmanager, name='cmanager'),
    path('cmanager/carousel', views.cmanager_carousel, name='cmanager_carousel'),
    path('cmanager/courses', views.cmanager_courses, name='cmanager_courses'),
    path('cmanager/departments', views.cmanager_departments,
         name='cmanager_departments'),
    path('cmanager/experience_heads', views.cmanager_experience_heads,
         name='cmanager_experience_heads'),
    path('cmanager/latest_news', views.cmanager_latest_news,
         name='cmanager_latest_news'),
    path('cmanager/students_review', views.cmanager_students_review,
         name='cmanager_students_review'),


    # NOTE: Handles navigations on the alumin dashboard
    path('alumniDashboard', views.alumniDashboard, name='alumniDashboard'),
    path('alumni/dues', views.alumni_dues, name='alumni_dues'),
    path('alumni/event', views.alumni_event, name='alumni_event'),
    path('alumni/internal_assessment', views.alumni_internal_assessment,
         name='alumni_internal_assessment'),
    path('alumni/wassce_assessment', views.alumni_wassce_assessment,
         name='alumni_wassce_assessment'),

    path('parentDashboard', views.parentDashboard, name='parentDashboard'),
    path('parent/make_payment', views.parent_make_payment,
         name='parent_make_payment'),
    path('parent/parent_request_review', views.parent_request_review,
         name='parent_request_review'),
    path('parent/upload_request_review',
         views.upload_request_review, name='upload_request_review'),
    #
    path('export_student_list', views.export_student_list,
         name='export_student_list'),

    path('export_star_student_list', views.export_star_student_list,
         name='export_star_student_list'),
    path('export_teacher_list', views.export_teacher_list,
         name='export_teacher_list'),
    path('export_subject_list', views.export_subject_list,
         name='export_subject_list'),
    path('export_exam_list', views.export_exam_list, name='export_exam_list'),
    path('export_timetable_list', views.export_timetable_list,
         name='export_timetable_list'),
    path('export_request_review_list', views.export_request_review_list, name='export_request_review_list'),
    path('export_department_list', views.export_department_list, name='export_department_list'),







]
