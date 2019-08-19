# Start Django Project

```bash
source venv/Scripts/activate
(venv)
$ pip install django
```

- Django를 설치한 순간부터 django-admin이라는 command를 사용할 수 있게 한다.
- 이 command 를 통해 django project 에 여러가지 명령을 할 수 있다.

```ba
$ django-admin startproject django_intro .
왼쪽에 manage.py가 생기면 된다.

$ python manage.py runserver
를 눌러서 서버 오픈
```

### Start project

```bash
(venv)
$ django-admin startproject django_intro.
```

- 현재 디렉토리에서 django_intro 라는 이름으로 프로젝트를 시작하겠다.

- Django project naming

  - -캐릭터는 사용할 수 없다.

  - python 과 django 에서 이미 사용되는 이름은 사용하지 않는다.

    (django 라는 이름은 django 그 자체와 충돌이 발생하며, test 라는 이름도 django 내부적으로 사용하는 모듈이름)

### Run server

```bash
$ python manage.py runserver
```

- `Ctrl + c` 커맨드로 끌 수 있음.
- 기본적으로 `localhost:8000` 에서 실행이 된다.

## django_intro 폴더의 파일들

pycache 폴더에 있는 내용들은 신경쓰지 않아도 된다. 그냥 파이썬 관련 캐시들일 것.

init.py 파일은 파이썬 패키지로써 쟝고 인트로를 파이썬 패키지로 해줄 수 있게 해주는 파일.

settings.py는 세팅이 일어나는 곳이다. 여기서 여러가지 세팅을 할 것.

```python
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

urls.py는 우리 페이지에서 어디 페이지로 갈 건지 기입하는 곳이다. 우리가 웹 어플리케이션 제작에 있어서 경로들/ 쟝고 프로젝트의 목차를 작성하는 곳

```python
# www.ssafy.com/admin/ => 성공
# www.ssafy.com/login/ => '로그인 페이지 관련 함수' 페이지 없음
path('login/', 로그인 페이지 관련 함수)
```

wsgi.py 지금은 만질 필요가 없구, 어떤 건지만 알고 있어라. 베포할 때만 사용하는 파일이다.

settings와 urls정도만 지금은 할 줄 알면 됨. 여기서만 작성하는거 기억하면 됨.

### manage.py 

는 매니저라고 생각하면 된다. 쟝고할때 이거를 통해서 하면 된다. 알아서 명령을 받아서 상호작용을 해줄 것.

db.sqlite3는 데이터베이스가 저장되는 곳. 데이터 관련 로직들 명령어 입력하면 이상한 것들 나옴.

뭐 근데 아무튼 만질 필요는 없음.

```
프로젝트 대 앱

프로젝트와 앱은 무엇이 다를까요? 앱은 특정한 기능(블로그나 공공 기록물을 위한 데이터베이스나, 간단한 설문조사 앱)을 수행하는 웹 어플리케이션을 말합니다. 프로젝트는 이런 특정 웹 사이트를 위한 앱들과 각 설정들을 한데 묶어놓은 것입니다. 프로젝트는 다수의 앱을 포함할 수 있고, 앱은 다수의 프로젝트에 포함될 수 있습니다.
```

## pages 폴더 만들기 & 폴더 안에 내용들

```bash
$ python manage.py startapp pages
```

이렇게 하면 왼쪽에 pages 폴더에 이것저것 생긴다.

### admin.py

너의 모델을 이곳에 등록해줘. 관리자 페이지를 커스터마이징 하는 곳. 여기는 조금씩 만질 일이 생길 것.

### apps.py

pages라는 어플리케이션에서 앱에 대한 정보가 입력되는 곳. 건드릴 일은 거의 없음.

### models.py

pages라는 어플리케이션에서 사용할 모델을 정의하는 곳. 유저라는 모델이 있어서 유저라는 정보를 저장. 저장할 데이터들을 정의하는 곳.

삼대장 중 첫번째 대장.

### tests.py

테스트 코드들이 저장이 되는 곳. 따로 다루지 않기에 우리가 만질 일이 없다.

### views.py

가장 중요한 point.

```
파이썬 쟝고의 삼대장 model template view
```

함수같은 것들을 views 안에 저장을 할 것. 무슨 css 같은 비슷한 건가...?

플라스크 할때 따로 함수들 저장해놓는 그런 공간??

두번째 대장.

### 쟝고 intro의 urls

이게 세번째 대장...?

## Settings.py에서

```python
# Application definition

INSTALLED_APPS = [
    # Local apps
    'pages',

    # Third party apps

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Local apps

우리가 직접 손보는 웹

### Third party apps

기본적으로 제공되지 않고 다른 사람이 만들어놓은 것은 이것이다. pip install로 하는 것??

따로 설치한 것들

### Django apps

쟝고에서 지정해둔 앱들이다. 기본 제공? 그런 느낌.

# After Lunch

### view.py

template_name: 어떤 페이지를 사용자에게 보여줄 건지 이름

templates라는 폴더를 만들면 view에서 함수가 알아서 저기로 찾아간다.

## 막간의 problem 실습

url : image/

template : `image.html` // 전달받은 image url 을 img 태그 src 속성에 담아서 랜덤 이미지를 보여준다.

view : 

```python
def image(request):
    # image url 을 context 에 담아서 image.html 에 전달한다..
```

```html
<img src="{{ url }}" alt="200따리이미지">
이런식으로 띄어쓰기 유의.
양 옆에 "" 로 감싸주기 해줘야 한다.
```

```django
path('greeting/IU/',)
url을 할 때 맨 끝에 /를 꼭 붙여줘야 한다. 붙이지 않으면 안된다.
```

### practice 실습

url : times/

- Variable routing 으로 숫자 2개를 각 각 `int` 타입으로 `num1, num2` 이름으로 받는다.

view : 

```python
def times(request, num1, num2):
    # 두 숫자를 곱한 result 변수와, num1, num2 를 context 에 담아서 times.html에 전달한다.
```

- template : `times.html`
  - 전달받은 context 의 값들을 알맞게 표시한다.


