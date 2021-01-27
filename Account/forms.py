from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label='نام کاربری'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}),
        label='گذرواژه'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exista_user = User.objects.filter(username=user_name).exists()
        if not is_exista_user:
            raise forms.ValidationError('کاربری با این مشخصات ثبت نام نکرده است')
        return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "نام کاربری"}),
        label=' نام کاربری'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "ایمیل"}),
        label='ایمیل',
        validators=[validators.EmailValidator('ایمیل معتبر نمی باشد')],
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "گذرواژه"}),
        label='گذرواژه'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "تایید گذرواژه"}),
        label=' تکرار گذرواژه',
        # چک کردن داده دریافتی و شخصی سازی کردنش،مثلا حداقل چند کارکتر باشه
        validators=[validators.MinLengthValidator(6,'گذرواژه باید حداقل 6 کارکتر باشد')]
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError("این کاربر قبلا قبت نام کرده است.")

        return user_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_exists_email = User.objects.filter(email=email).exists()

        if is_exists_email:
            raise forms.ValidationError("کاربری با این ایمیل قبلا ثبت نام کرده است")
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if password != re_password:
            raise forms.ValidationError('گذواژه مغایرت دارد')
        return password
