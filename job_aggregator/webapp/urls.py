from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signin/", views.signin, name="signin"),
    path("login/", views.login_view, name="login"),
    path("confirmation_sent/", views.confirmation_sent, name="confirmation_sent"),
    path("account_activated/", views.account_activated, name="account_activated"),
    path("activation_failed/", views.activation_failed, name="activation_failed_no_id"),
    path(
        "activation_failed/<int:user_id>/",
        views.activation_failed,
        name="activation_failed",
    ),
    path("job_board/", views.job_board, name="job_board"),
    path("activate/<uuid:token>/", views.account_activation, name="account_activation"),
    path(
        "resend_activation_email/<int:user_id>/",
        views.resend_activation_email,
        name="resend_activation_email",
    ),
]
