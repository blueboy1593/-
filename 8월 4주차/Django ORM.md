# Django ORM

## 기초설정

```
$ python manage.py makemigrations
$ python manage.py migrate

위에 이것들을 해줘야 한다.
아마 SQLite에서 쓰는 기능들이 여기에 담겨있는게 아닌가 싶은데. 뭐하는 것들인지는 이따 다시 확인.
```

- Shell

  ```bash
  python manage.py shell
  ```

- import model

  ```python
  from articles.models import Article
  ```

  데이터베이스에서 명령을 내리게 하는 객체가 objects이다.

  article은 뭐지....

### 데이터를 저장하는 3가지 방법

title과 content가 있는 상태에서만 저장을 할 수 있다.

1. 첫번째 방식

   ```bash
   article = Article()
   article
   article.title = 'First article'
   article.content = 'Hello, article?'
   article.save()
   article # <Article: Article object (1)>
   위와 같은 결과값이 나옴.
   Article.objects.all() # 아티클에서 모든 오브젝트??? 를 가져오라는 명령어.
   ```

2. 두 번째 방식

   - 함수에서 keyword 인자 넘기기와 비슷한 방식

     ```python
     article = Article(title='Second', content='hihi')
     # 이번에는 생성하면서 넘겨준다.
     article.save() # 저장
     ```

3. 세번째 방식

   - create를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번의 스텝

     ```python
     Article.objects.create(title='third', content='Django! Good')
     # <Article: Article object (3)> 이런식의 반응이 나온다.
     ```

4. title과 content가 모두 있어야 저장을 할 수 있다. 검증 과정.

   ```python
   article=Article()
   article.title='Python is good'
   article.full_clean() # 저장하기 전 데이터 검증을 할 수 있다.
   # raise ValidationError(errors)
   # {'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
   ```

# READ

## 모든 객체

```python
>>> Article.objects.all()
<QuerySet [<Article: 1번 글 - First article : Hello, article?>, <Article: 2번 글 - title : hihi>, <Article: 3번 글 - third : Django! Good>]>
# 전부 다 가지고 오라는 것
```

### Filter를 통해서 타이틀에 맞게 분류하기

```python
>>> Article.objects.filter(title='third')
<QuerySet [<Article: 3번 글 - third : Django! Good>, <Article: 4번 글 - third : Django? Django!>]>
# 복수형으로 가지고 온다.
```

### DB에 저장된 글 중 title이 같은 글 중에서 첫번째만 가지고 오기

```python
>>> querySet = Article.objects.filter(title="third")
>>> querySet
<QuerySet [<Article: 3번 글 - third : Django! Good>, <Article: 4번 글 - third : Django? Django!>]>
>>> querySet.first()
<Article: 3번 글 - third : Django! Good>
# querySet으로 타이틀 필터된 것들을 모아주고 그 중 몇번째를 골라본다.
>>> Article.objects.filter(title="third").last()
<Article: 4번 글 - third : Django? Django!>
# first 말고 last도 사용할 수 있음.
```

### DB에 저장된 글 중에서 pk가 1인 글만 가지고 오기

PK만 `get()` 으로 가지고 올 수 있다.

```python
# PK = Primary Key = 고유 식별자 가장 유니크하고 이거 말고는 잘 사용하지 않기에.
Article.objects.get(pk=1)
>>> Article.objects.get(pk=10)
articles.models.Article.DoesNotExist: Article matching query does not exist.
# 이렇게 하면 오류가 난다.
>>> Article.objects.get(title='third')
articles.models.Article.MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
# filter로 하면 출력이 되지 않지만 오류는 안난다.
>>> Article.objects.filter(pk=10)
<QuerySet []>
```

### 오름차순 내림차순

```python
# 이렇게 하면 오름차순으로 가져온다
>>> articles = Article.objects.order_by('pk')
>>> articles
<QuerySet [<Article: 1번 글 - First article : Hello, article?>, <Article: 2번 글 - title : hihi>, <Article: 3번 글 - third : Django! Good>, <Article: 4번 글 - third : Django? Django!>]>
# 이렇게 하면 내림차순??
>>> articles = Article.objects.order_by('-pk')
>>> articles
<QuerySet [<Article: 4번 글 - third : Django? Django!>, <Article: 3번 글 - third : Django! Good>, <Article: 2번 글 - title : hihi>, <Article: 1번 글 - First article : Hello, article?>]>
```

### 인덱스 접근이 가능하다!

```python
# 단편적인 인덱스 접근
>>> article = articles[2]
>>> article
<Article: 2번 글 - title : hihi>
# 심지어 슬라이싱도 가능. 오브젝트와 올로 하기.
>>> articles = Article.objects.all()[1:3]
>>> articles
<QuerySet [<Article: 2번 글 - title : hihi>, <Article: 3번 글 - third : Django! Good>]>
```

### 단어의 부분값을 입력해도 가능

- startswith
- endswith

```python
>>> articles = Article.objects.filter(title__contains='th')
>>> articles
<QuerySet [<Article: 3번 글 - third : Django! Good>, <Article: 4번 글 - third : Django? Django!>]>
# 이런식으로 __를 사용해서...! 특이한 방식이니깐 잘 알아놓는게 좋을 것 같다.
>>> articles = Article.objects.filter(title__startswith="firs")
>>> articles
<QuerySet [<Article: 1번 글 - First article : Hello, article?>]>
# 여기는 왜인지는 모르겠는데 대소문자 그냥 된다. 
>>> articles = Article.objects.filter(content__endswith='Good')
>>> articles
<QuerySet [<Article: 3번 글 - third : Django! Good>]>
# startswith과 endswith
```

## Delete

article 인스턴스 생성 후 `.delete()` 함수를 실행한다.

```python
>>> article = Article.objects.get(pk=2)
>>> article.delete()
(1, {'articles.Article': 1})
위와 같이 지워줄 수가 있음.
```

## Update

article 인스턴스 호출 후 값 변경하여 `.save()` 함수 실행

```python
>>> Article.objects.create(title='Good')
<Article: 5번 글 - Good : >
>>> article = Article.objects.get(pk=5)
>>> article.content
''
>>> article.content = 'new contents'
>>> article.save()
# 이런 식으로 update를 해주는 것.
```

# admin.py

```python
from django.contrib import admin
from .models import Article
# 동일한 모델에 있는 아티클을 등록. admin이라는 미리 주어진 객체를 활용
# Register your models here.
admin.site.register(Article)
```

```bash
$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'student'): KangHyun
이메일 주소:
Password:
Password (again):
Error: Your passwords didn't match.
Password:
Password (again):
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

신기하다.... 이런식으로 하면 다 되는구나. 어드민 페이지 되고

### [![img](https://wayhome25.github.io/assets/images/monkey.jpg) 초보몽키의 개발공부로그](https://wayhome25.github.io/)

```bash
$ pip install django-extensions
이것으로 쟝고 익스텐션스를 깔아주고,
INSTALLED_APPS = [
    # third parties
    'django_extensions',
    ]
    여기에 저장해준다.
```

```bash
$ python manage.py shell_plus
# Shell Plus Model Imports
위 명령어로 켜준다.
```

# 점심 먹고 다시!

## 이게 바로 MTV 모델이다!

```python
'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],
templates에 이렇게 넣어주면 됨.
```

1. base.html 만들고 그거 변경하면서 이리저리 할 것.

2. 경로를 여러가지로 막 할 수 있음.

   ```python
   from .models import Article
   이런 식으로 같은 폴더 안에 파일이나 폴더 등등
   ```

3.  new, index, views, create 등등 url.py crux를 왜 거치는 거지.