from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    age = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        self.users = kwargs.pop('users', [])  # Получаем список пользователей из kwargs
        super().__init__(*args, **kwargs)  # Инициализация родительского конструктора

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username in self.users:  # Проверка на уникальность
            raise forms.ValidationError("Пользователь с таким именем уже существует.")
        return username

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("Возраст должен быть не менее 18 лет.")
        return age

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Проверка на совпадение паролей
        if password != confirm_password:
            self.add_error('confirm_password', 'Пароли не совпадают.')  # Добавляем ошибку в поле confirm_password

        return cleaned_data
