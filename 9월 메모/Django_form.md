# Django_form 2

### .gitignore에 가상환경 폴더와 .vscode 폴더 관련

```
venv/
.vscode/
```

```bash
django-admin startproject myform .
프로젝트 만들기
```

```python
class Meta:
        ordering = ('-pk')
마지막으로 꺼낸 친구가 표현? 될 수 있도록?
```

### 관리자 아이디 만들기

```bash
python manage.py createsuperuser
관리자? 아이디를 만드는 것 같음.
```

### 은근히 놓치기 쉬운 views.py의 import 들

```python
from django.shortcuts import render, redirect,get_object_or_404
다 해줘야해 이런거.
from django import forms
이걸로 이제 forms에 있는 것들을 사용할 수 있는거지.
```

### html에서 form의 역할

```django
{{ form.as_p }}
이게 아래를 대체한다구?! 더 좋은 기능으로다가 대체해준다.
{% comment %} <label for="title">타이틀: </label><br>
  <input type="text" name="title" id="title"><br>
  <label for="content">내용: </label><br>
  <textarea name="content" id="content" cols="30" rows="10"></textarea> {% endcomment %}
```

### form 좀 꾸며보기

```python
class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the title...'
            }
        ),
    )
위젯으로 form을 어떻게 할지 보여줄 수 있다. 여러가지 기능 추가
```













