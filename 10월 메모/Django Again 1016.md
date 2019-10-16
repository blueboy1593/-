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





``` bash
In [1]: 1+1
Out[1]: 2
​
In [2]: form
Out[2]: <ArticleForm bound=True, valid=Unknown, fields=(title;content)>
​
In [3]: dir(form)
Out[3]:
['Meta',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__html__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_bound_fields_cache',
 '_clean_fields',
 '_clean_form',
 '_errors',
 '_get_validation_exclusions',
 '_html_output',
 '_meta',
 '_post_clean',
 '_save_m2m',
 '_update_errors',
 '_validate_unique',
 'add_error',
 'add_initial_prefix',
 'add_prefix',
 'as_p',
 'as_table',
 'as_ul',
 'auto_id',
 'base_fields',
 'changed_data',
 'clean',
 'data',
 'declared_fields',
 'default_renderer',
 'empty_permitted',
 'error_class',
 'errors',
 'field_order',
 'fields',
 'files',
 'full_clean',
 'get_initial_for_field',
 'has_changed',
 'has_error',
 'hidden_fields',
 'initial',
 'instance',
 'is_bound',
 'is_multipart',
 'is_valid',
 'label_suffix',
 'media',
 'non_field_errors',
 'order_fields',
 'prefix',
 'renderer',
 'save',
 'use_required_attribute',
 'validate_unique',
 'visible_fields']
​
In [4]: form.as_p
Out[4]: <bound method BaseForm.as_p of <ArticleForm bound=True, valid=Unknown, fields=(title;content)>>
​
In [5]: form.as_p()
Out[5]: '<p><label for="id_title">Title:</label> <input type="text" name="title" value="4번째 게시글" maxlength="20" required id="id_title"></p>\n<p><label for="id_content">Content:</label> <textarea name="content" cols="40" rows="10" required id="id_content">\n배고파</textarea></p>'
​
In [6]: form.is_valid()
Out[6]: True
```

