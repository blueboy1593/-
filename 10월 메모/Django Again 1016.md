# Django Again 1016

```bash
python -m venv venv
venv라는 모듈을 가상환경 이름으로 정해주는것.

pip freeze > requirements.txt
저 텍스트 파일에 어떤 모듈들이 설치되어있는지 얼려준다. 디버깅 테스트 때에는 저게 제공이 될 것.
저기에 있는 명령어를 따라서 설치하면 된다고 하는 것 같음.

pip freeze | xargs pip uninstall -y
이거 하면 으으으으음..... 다 지워버리는 건가????
큼...

pip install -r requirements.txt
이거를 치면 requirements.txt 이거를 읽으면서 하나하나 설치하는 과정이다.

django-admin startproject review .
이거 이제 슬슬 외울 때 된거같다.

python manage.py startapp 이름은 복수형으로 만드는게 좋다.

pip install django-extensions ipython
이게 두개 다 설치하는 것인가봐
```

```python
USE_I18N = True
이거 두개가 국제와 현지값?
USE_L10N = True
```



```bash
In [1]: Article
Out[1]: articles.models.Article
In [2]: article = Article()
In [3]: article.title = '첫번째 타이을'
In [4]: article.save()
이렇게 입력.
```

```bash
$ python manage.py makemigrations
You are trying to add a non-nullable field 'content' to article without a default; we can't do that (the database needs something
to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> ''
Migrations for 'articles':
  articles\migrations\0003_article_content.py
    - Add field content to article
(venv)
이거는 content를 없다가 새로 넣어주면서 생긴 것이다.
python manage.py migrate
를 해주면 실제 반영이 되는 것!!
```

```json
"[django-html]": {
        "editor.tabSize": 2
    }
이거슨 세팅에서 탭사이즈를 2로 만들어 주는 것.

'APP_DIRS': True,
어플리케이션 폴더에 있는 것들은 자동으로 인식하게 되어있음.
다른곳에 하겠다면 등록을 해줘야하는 것이다.

class Meta:
        ordering = ('-pk', )
이거 하면 정렬이 pk 반대로 된다!!!!
재밌네 재밌어
```

```django
<a href="{% url 'articles:detail' article.pk %}">상세보기 고고</a>
이렇게 하는거 기억 나지??
```

```python
form = ArticleForm(instance=article)
이렇게 하면 instance에 원래 있던 article이 저장된다.
```

```python
class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(
        max_length=100,
        validators=[EmailValidator(message='이메일 형식에 맞지 않습니다.')]
        )
    age = models.ImageField(
        validators=[MinValueValidator(message="미성년자는 노노에요")]
    )
이렇게 해서 validator 쓰는 방법 알겠지?!
```

```bash
python manage.py dumpdata --format=json articles.article > articles.json
이걸로 뭐 데이타 추출하는 듯

python manage.py dumpdata --format=yaml articles.article > articles.yaml
yaml 모듈이 있어야 작동하는 것

pip install pyyaml
로 설치해주면 된당!

python manage.py loaddata articles.json
python manage.py loaddata articles.yaml
이거로 불러올 수 있는것!!! 엄청 신기함.

ctrl + shift + p 로 format document 누르면 개이득이다!!
```

## 1017 부터의 복습

### 과제 코멘트 만들기

```
# Comment 기능 구현

- Comment 모델을 만들어야 합니다.
  - content : 문자열
  - created_at : 시간
  - article : 참조키
- Comment 의 Create, Read, Delete 가 가능해야 합니다.
  - Comment 생성/삭제 동작의 경우 모두 POST 요청으로 동작합니다.
  - Comment 읽기(목록) 및 생성/삭제 동작은 Article 의 읽기(상세보기)에 있습니다.
  - Comment 생성 동작은 모두(View, Template 에서) ModelForm 으로 구현해야 합니다.
```





