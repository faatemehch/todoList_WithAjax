from django.urls import path
from django.contrib.auth import views as forgotPasswordView

urlpatterns = [
    path( 'password-reset/', forgotPasswordView.PasswordResetView.as_view(
        template_name='forgot_password/password_reset_form.html',
        email_template_name='forgot_password/password_reset_email.html',
        subject_template_name='forgot_password/password_reset_subject.txt'
    ),
          name='password_reset' ),

    path( 'password-reset/done/', forgotPasswordView.PasswordResetDoneView.as_view(
        template_name='forgot_password/password_reset_done.html'
    ),
          name='password_reset_done' ),

    path( 'password-reset-confirm/<uidb64>/<token>/',
          forgotPasswordView.PasswordResetConfirmView.as_view(
              template_name='forgot_password/password_reset_confirm.html'
          ),
          name='password_reset_confirm' ),

    path( 'password-reset-complete/',
          forgotPasswordView.PasswordResetCompleteView.as_view(
              template_name='forgot_password/password_reset_complete.html'
          ),
          name='password_reset_complete' ),

]
