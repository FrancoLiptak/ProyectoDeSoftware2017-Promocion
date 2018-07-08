from django.urls import include, path
from apps.users.views import * 
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.decorators import login_required

app_name = 'users'
urlpatterns = [
    path('register/', login_required(RegisterUser.as_view()), name='users_register'),
    path('login/', login, {'template_name':'users/login.html'}, name='users_login'),
    path('logedin/', login_required(logued_user), name='users_logedin'),
    path('logout/', login_required(logout_then_login), name='users_logout'),
    path('reset/password_reset/', password_reset, {'template_name':'users/password_reset_form.html',
        'email_template_name':'users/password_reset_email.html',
        'post_reset_redirect':'users:users_password_reset_done',}, name='users_password_reset'),
    path('reset/password_reset_done/', password_reset_done, {'template_name':'users/password_reset_done.html',},
        name='users_password_reset_done'),
    path("reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/",
        password_reset_confirm, {'template_name':'users/password_reset_confirm.html',
        'post_reset_redirect':'users:users_password_reset_complete',},
        name='users_password_reset_confirm'),
    path('reset/password_reset_complete/', password_reset_complete, {'template_name':'users/password_reset_complete.html',},
        name='users_password_reset_complete'),
    path('list/', login_required(UsersList.as_view()), name='users_list'),
    path('update/<pk>/', login_required(UsersUpdate.as_view()), name='users_update'),
    path('delete/<pk>/', login_required(UsersDelete.as_view()), name='users_delete'),
    path('show/<pk>/', login_required(UsersShow.as_view()), name='users_show'),
]