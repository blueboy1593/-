# Django Rest Framework

```bash
pip install djangorestframework
쟝고로 레스트를 도와주는 프레임워크

$ python manage.py dumpdata --indent 2 musics > dummy.json
이 코드로 dummy.json 에다가 덤프데이타를 저장하구

$ python manage.py loaddata dummy.json
이 코드로는 불러올 수가 있다.

$ pip install drf-yasg
이걸로 새로운 tool 받기
```

```
http://127.0.0.1:8000/api/v1/musics/?artist_pk=1
Domain + endpoint + query parameters
```

