# Django 심화편

### Python

```python
from django.contrib.auth.forms import UserCreationForm
회원가입 할 때 쟝고에 있는 form을 사용한다는 것.

from django.contrib.auth import login as auth_login
로그인 메써드를 통해서 정보다 담겨있음.

form.get_user()
# 사용자의 정보를 우리에게 주는 함수

import login as auth_login, logout as auth_logout
# import를 할 때 이름을 바꿔주는 것. 중첩이 될 수 있기에!

next_page = request.GET.get('next')
            return redirect(next_page or 'articles:index')
next는 약간 내장에서 주어지는 느낌임.

@login_required
이렇게 쓰는거는 사용자가 url로 치고 들어오는 것을 막는 것.
로그인을 해야만 가능할 수 있게.

request.user.delete()
로그인이 되어있는 상태에서 삭제 가능함.

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]
이런식으로 static과 assets를 연결해줄 수 있다.

on_delete=models.CASCADE
# 연결되어있는 관계가 끊어지면 해당 article도 지워버리겠다!!
# 한명의 user가 계속 article을 낼 건데 그러기 때문에 속하는 것일 것!!!)
```

### HTML Django

```html
<p>Hello, {{ user.username }}</p>
이런식으로 아예 정보가 기입이 되나부당.
```

### Bash

```bash
In [1]: request.user
Out[1]: <SimpleLazyObject: <User: blueboy1593>>

In [2]: request.user.is_anonymous
Out[2]: False
유저가 익명인지 물어보는 것.

In [3]: request.user.is_superuser
Out[3]: False
```

## 쟝고 USER 모델 만들기

### python

```python
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# 세팅즈에서 user모델을 직접 가져오는 것이다!

article.user = request.user
# 이 부분은 자동으로 해주는 건지 자동함수같은 느낌인건지 정확하게 모르겠다
```

### html

```django
{% if article.user == request.user %}
항상 유저는 request로 들어오는 것이다.
아티클에는 user가 존재하고
```

Template에서 노출시키지 않기!

그리고 url로 직접 들어갔을때 수정하지 못하게 하기!

## Practice

```
# Comment 와 User 간 1:N 관계 정의

- Comment 모델에 user 필드를 추가하여 1:N 관계를 형성한다.
  - 기존 생성되어있던 comment 가 있을 경우 임의의 사용자 정보로 채운다.
- View 함수에서 comment 생성 시 User 정보를 함께 저장한다.
- Article 상세보기 화면에서 Comment 정보 표현 시 작성자 이름도 함께 보여준다.
- Article 상세보기 화면에서 내가 작성한 Comment 라면 삭제하기 버튼을 보여준다.
- View 함수에서 comment 를 생성한 유저와 요청을 보낸 유저가 같을 경우에만 삭제하기 기능을 수행한다.
```

# Doctor & Patient

## shell_plus

```bash
In [3]: doctor1 = Doctor.objects.create(name='scarlet')

In [4]: doctor1
Out[4]: <Doctor: 1번 의사 scarlet>

In [5]: doctor2 = Doctor.objects.create(name='metel')

In [6]: patient1 = Patient.objects.create(name='chulyi', doctor=doctor1)

In [7]: patient2 = Patient.objects.create(name='kijang', doctor=doctor2)

In [8]: patient3 = Patient.objects.create(name='pikachu', doctor=doctor1)

In [9]: doctor1
Out[9]: <Doctor: 1번 의사 scarlet>

In [10]: patient3
Out[10]: <Patient: 3번 환자 pikachu>
이런식으로
Reservation.objects.create(doctor=doctor1, patient=patient2)

doctor1 = Doctor.objects.get(pk=1)
```

migrations에 있는 initial 숫자 등을 지우면 데이터를 지울 수 있다.

```bash
mamytomany field로 구현한 것
doctors = models.ManyToManyField(Doctor, related_name='patients') # 역으로 접근할 수 있도록 이름을 지어주기.

In [4]: doctor1.patients.add(patient1)

In [5]: doctor1.patients.all()
Out[5]: <QuerySet [<Patient: 1번 환자 chulyi>]>

In [6]: patient1.doctors.all()
Out[6]: <QuerySet [<Doctor: 1번 의사 scarlet>]>

# 여기는 지워보기
In [7]: patient1.doctors.remove(doctor1)

In [8]: patient1.doctors.all()
Out[8]: <QuerySet []>

In [9]: doctor1.patients.all()
Out[9]: <QuerySet []>
```

## fontawesome에서 가져오기

```
https://fontawesome.com/
에서 로그인하고 스크립트 붙여넣기 하기.
base.html에 부트스트랩 css랑 타이틀 사이에 끼워넣기
```



# 1023 N 대 N 다시 하기

```python
from django.contrib.auth.models import AbstractUser
# 이런식으로 유저를 꺼내준다.../??
```

