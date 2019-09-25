# 09/19,20 목요일 금요일 메모

# Django

path 뒤에 include를 넣어줘야 한다.

/pages/greeting/<str:name>/경로로 name을 변수로 받아서 greeting.html에서 name값을 출력하는 페이지를 만드세요.

django에서는 template namespace를 공유한다.

 method="GET"

 method="POST"

두 종류의 method 가 있다.!

```bash
python manage.py makemigrations
python manage.py migrate
```



쟝고는 모든 템플레이츠 폴더를 어플리케이션들이 공유를 하지.

```bash
pip install faker
python manage.py shell
python manage.py makemigration
python manage.py migrate
# 데이터베이스를 어플리케이션마다 만들어줘야 한다.
```

```bash
from faker import Faker
fake = Faker()
fake.name()
fake.name()
fake.name()
fake.address()
fake = Faker('ko_kr')
fake.job()
```

# 전생 직업 찾기

## 페이지

### 이름 입력 페이지

- 해당 페이지에 접근하는 URL 은 `/jobs/` 입니다.
- `name` 을 입력할 수 있는 `form` 이 있으며 `form` 의 method 는 `POST` 입니다. `form` 은 `/jobs/past_job/` 으로 제출됩니다.

### 전생 직업 결과 페이지

- 해당 페이지에 접근하는 URL 은 `/jobs/past_job/` 입니다.
- `/jobs/` 에서 제출된 form 의 `name` 으로 저장된 직업을 데이터 베이스에서 찾아서 `past_job.html` 페이지에 표시합니다.
  - 단, `name` 으로 저장된 직업이 없을 시 `faker` 라이브러리를 통해 랜덤으로 직업 데이터를 생성하여 데이터베이스에 저장합니다.

# 프로젝트 두번째

https://developers.giphy.com/docs/api

- 회원가입 하여 API Key 를 발급받는다.

https://developers.giphy.com/docs/api/endpoint

- 위 API 를 사용하여 past_job 에 맞는 gif 파일을 검색하여 화면에 함께 보여준다.
- 사용 라이브러리 : `requests`
  - `pip install requests`

GIPHY에서 gif를 받아서 한다.

api.giphy.com/v1/gifs/search?

api_key=4i1aScgdTDrEGFZuIltFlaHACRS0QWA6&

q=cheeze&

limit=1

# 오후 수업 데이더 다루기

on_delete 

```bash
pip install django_extensions
python manage.py shell_plus


>>> article = Article()
>>> article.title = '새로운 데이터'
>>> article.content = '새로운 내용'
>>> article.save()
>>> article
<Article: Article object (5)>
>>> comment = Comment()
>>> comment.content = 'First comment'
>>> comment.article = article
>>> comment.article_id = article.pk
>>> comment.save()
comment.article
comment.article_id
comment.article_pk
comment.article.content
comment.article.title
comment.pk
comment = Comment(article=article, content = 'Second comment')
comment.save()
comment.content
comment.article
dir(article)
dir(article.comment_set)
# 여러가지 코멘트에 관한 것들을 실행할 수 있다.!

pip install ipython
# 이것을 해주면 in 과 out으로 ㅇ나온다!!!


```

```bash
In [7]: article.comment_set.get(pk=1)
Out[7]: <Comment: First comment>

In [8]: article.comment_set.filter(content='Second comment')
Out[8]: <QuerySet [<Comment: Second comment>]>

In [9]: article.comment_set.filter(content='Second comment').first()
Out[9]: <Comment: Second comment>
```

```bash
python manage.py makemigrations
python manage.py migrate
article = Article.objects.get(pk=7)
# 이런식으로 7번에 속해있는 article을 가져온다.
In [4]: article.comments.all()
Out[4]: <QuerySet [<Comment: Second comment>, <Comment: First comment>]>

```

```python
comments = article.comments.all()
이렇게 바꿔서 접근한다.
```

```html
{% load static %}
스태틱 폴더를 가져옵니다!
<img src="{% static 'articles/images/gazua.jpeg' %}" alt="gazua">
폴더를 이런식으로!
스태틱은 그러면 원래 지정된 값일까? 아니면 다른 폴더로 이름을 지어도 되는 것?
templates 처럼 이름이 있는 그 자체로 작동을 하는건지
```

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
원하는 곳에 static을 세팅하는 방법에 해당
```

https://docs.djangoproject.com/ko/2.2/howto/static-files/

에서 나온 정보들.

static을 많이 세팅해주고 불러온다. static은 그냥 좀.... 음... 뭐랄까 편하게 불러오기 위한 것인거같음.

지금부터 할 것은 이미지 저장.

```python
image = models.ImageField(blank=True)
아무런 값이 넘어오지 않아도 저장할 수 있다.
데이터는 숫자값 비어있는 것 null 등등 저장할 수 있다.
```

```bash
$ python manage.py makemigrations
SystemCheckError: System check identified some issues:

ERRORS:
articles.Article.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "pip install Pillow".
(venv)
쟝고에서는 img를 그냥 저장할 수 없기 때문에 그지같은 pillow라는 pip를 깔아야 한다.
```

```bash
$ sqlite3 db.sqlite3
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
sqlite> .schema articles_article
CREATE TABLE IF NOT EXISTS "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(20) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "image" varchar(100) NOT NULL)
# varchar는 string이라는 뜻이다.
# NOT NULL
```

```html
accept="image/*"
세상에서 가장 믿을 수 없는 것이 사용자이기에 이렇게 지정해준다.
```

```python
image = request.FILES.get('image')
POST로 하는게 아니라 FILES에서 꺼낸다고 생각하면 된다. image를 get 하는거지.

from IPython import embed
embed()

In [3]: image.name
Out[3]: '튜브1.jpg'

In [4]: image.size
Out[4]: 45409

In [5]: article.image
Out[5]: <ImageFieldFile: 튜브1_RJlLhX0.jpg>
       
In [7]: article.image.url
Out[7]: '%ED%8A%9C%EB%B8%8C1_RJlLhX0.jpg'

In [8]: article.image.path
Out[8]: 'C:\\Users\\student\\django\\django_crud\\튜브1_RJlLhX0.jpg'
# 이런식으로 확인을 해볼 수 있다.
```

### Settings.py

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media Files
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# static과 media에 대한 setting이다.
```

# Media 파일 올리기 위한 작업

1. Article Model 에 `ImageField` 추가

2. Form 으로 파일 타입 받을 수 있도록 enctype 속성을 multipart/form-data 로 줬음.

3. Form 안에서 File type의 input 생성, accept="image/*" 속성을 줬음

   - accept : 특정 파일 타입만 받을 수 있게 하기 위한 속성

4. `create` 함수에서 파일을 `request.FILES` 에서 꺼내서 article에 넣고 저장.

5. media 파일들을 저장하기 위한 폴더 설정

   ```python
   # settings.py
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # 프로젝트/media/
   ```

6. Client 가 media 파일들로 접근할 수 있는 URL 이름 설정

   ```python
   # setting.py
   MEDIA_URL = '/media/'
   ```

7. Client 가 실제 파일들로 접근할 수 있는 URL 생성

   ```python
   # crud/urls.py
   from django.conf import settings
   from django.conf.urls.static import static
   ...
   # MEDIA_URL 로 들어오면 MEDIA_ROOT 에 저장한 파일들로 접근할 수 있습니다.
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

8. Detail 페이지에서 이미지 보여주기

   `detail.html`

   ```django
   <img src="{{ article.image.url }}" alt="{{ article.image }}">
   ```

## Mini Project

```
## Jobs Application 에 Media 파일 업로드 로직 구현

1. **Model**
   - `Job` model 에  `profile_image` 이름으로 이미지 필드를 생성한다.
   - 새롭게 수정한 모델을 데이터베이스 테이블에 반영시킨다.
2. **Pages**
   - 이름을 입력하는 페이지에서 사진 파일을 함께 업로드 할 수 있게 한다.
   - 결과페이지에서 저장한 이미지를 출력하여 보여준다.

3. **View**
   - Job 데이터를 저장할 때 업로드한 사진 파일을 함께 저장한다.
```

## 아이콘을 등록하는 것 해보자!

```html
favicon generator를 돌려서 일단 favicon을 만든다.
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
link파비콘으로!
<link rel="shortcut icon" href="{% static 'favicon-96x96.png' %} " type="image/x-icon">
요런식으루다가
```

```bash
pip install pilkit
pip install django-imagekit
로 이미지킷 다운받기
```

```python
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField
이렇게 활용하는 것
```



