from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('user_login/', user_login, name='user_login'),
    path('login_admin/', login_admin, name= 'login_admin'),
    path('user_signup/', user_signup , name='user_signup'),
    path('admin_home/', admin_home, name = 'admin_home'),
    path('admin_logout/', admin_logout, name = 'admin_logout'),
    path('profile/', profile , name ='profile'),
    path('change_password/', change_password, name = 'change_password'),
    path('upload_notes/', upload_notes, name = 'upload_notes'),
    path('viewmy_notes/', viewmy_notes, name = 'viewmy_notes'),
    path('viewall_notes/', viewall_notes, name= 'viewall_notes'),
    path('view_users/', view_users , name = 'view_users'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
    path('deletemy_notes(?P<int:pid>)', deletemy_notes, name='deletemy_notes'),
    path('pending_notes/', pending_notes, name = 'pending_notes'),
    path('rejected_notes/', rejected_notes, name = 'rejected_notes'),
    path('accepted_notes/', accepted_notes, name= 'accepted_notes'),
    path('allnotes_admin', allnotes_admin, name = 'allnotes_admin'),
    path('delete_users(?P<int:pid>)', delete_users, name= 'delete_users'),
    path('deletenotes_admin(?P<int:pid>)', deletenotes_admin, name = 'deletenotes_admin'),
    path('status/<int:pid>', status , name = 'status')
]
