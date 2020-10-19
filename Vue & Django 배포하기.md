# Vue & Django 배포하기

# VUE part

1. 우리는 구글에 배포할 것.

2. Firebase 사용.

3. Google 로그인하고 Firebase console 검색

4. 프로젝트 만들기

5. 체크박스는 다 클릭하고 프로젝트 만들기 누르기.

6. 개발 탭 -> 호스팅 -> 시작

7. ```
   npm install -g firebase-tools
   firebase를 사용하는 툴을 설치.
   ```

8. ```bash
   $ firebase login
   $ firebase init
   ```

9. Hosting 에 체크 후 엔터.

10. Use an existing project

11. ? What do you want to use as your public directory? dist

12. ? Configure as a single-page app (rewrite all urls to /index.html)? (y/N) y

    여기서 해주는 것은 일단 index 페이지로 보내고

13. ```bash
    ? What do you want to use as your public directory? dist
    ? Configure as a single-page app (rewrite all urls to /index.html)? Yes
    ? File dist/index.html already exists. Overwrite? Yes
    +  Wrote dist/index.html
    
    i  Writing configuration info to firebase.json...
    i  Writing project information to .firebaserc...
    i  Writing gitignore file to .gitignore...
    
    +  Firebase initialization complete!
    ```

14. firebase.json

    ```json
    "hosting": {
        사용하고자 하는 서비스의 이름이다.
        "public": "dist",
        다이스트 라는 폴더에 배포하고싶은 모든 파일을 넣어놓겠다.
        "ignore": [
          "firebase.json",
          "**/.*",
          "**/node_modules/**"
        ],
    	여기에 있는 파일들은 추적하지 않겠다.
    	"rewrites": [
            이부분이 싱글 페이지 어플리케이션 Yes라고 해서 적용되는 부분이다.
          {
            "source": "**",
            어디로 들어오던간에 일단은 index.html로 보내라! vue-router를 통해서 component로 보내준다.
            "destination": "/index.html"
          }
        ]
    ```

15. "build": "vue-cli-service build",

    이 명령어로 하나로 묶는다. 여기서 잘 되어야 프로젝트가 되는 것이다.

16. ```bash
    $ firebase deploy
    이 명령어를 통해서 호스팅 뭐시기가 될 것.
    ```

17. 여기까지 하면 Vue 배포 끝!

18. 이쪽 URL로 가면 우리가 만든 VUE 를 볼 수 있따.



# Django part

1. 쟝고 배포는 2가지 방법으로 해볼 생각이다.

2. AWS와 헤로폰? 의 2가지 방법으로.

3. AWS는 카드 등록을 해야 할 수 있다.

4. ```bash
   $ python manage.py dumpdata accounts.User > users.json
   나의 database에 있는 덤프유저를 
   ```

5. accounts 폴더의 fixtures에 정보를 넣어준다.

6. 서버는 DB가 없는 상태에서 시작한다.

7. 그리고 서버는 시작할때 migrate를 할 것이다.

8. users.json 을 데이터 시팅으로 얹어준다.

9. ```
   $ python manage.py loaddata users.json
   얘는 application 의 fixtures 폴더에서 찾는 것이다.
   이러면 저장해두었던 데이터가 db.sqlite3에 저장이 될 것이다.
   ```

10. ```python
    ALLOWED_HOSTS = ['*']
    ```

    어떤 친구들이 들어올 수 있는지에 대해 허용해주는 것.

11. .env 만들어서

    ```python
    SCRETE_KEY='$bm*_f=$#auyrr=j3(a_@j7r5mp7(pp3%k(v4!%$%ke+sf--@)'
    DEBUG=True
    ```

12. ```bash
    pip install python-decouple
    ```

    환경변수에 있는 파일을 읽어오겠따! 라는 것.

13. settings.py

    ```python
    from decouple import config
    SECRET_KEY = config('SCRETE_KEY')
    DEBUG = config('DEBUG')
    ```

14. aws 검색해서 들어가기.

15. aws 서비스 찾기에서 IAM 검색.

16. 사용자 추가.

17. 액세스 유형 선택에서는 둘 다 선택.

    ```
    비밀번호: qwer1234
    ```

18. 기존 정책 직접 연결.

19. ElasticBeans 검색

20.  [AWSElasticBeanstalkFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAWSElasticBeanstalkFullAccess)  이거 체크해서 하나 만들기

21. 태그는 무시하고 다음으로 넘어간다.

22. csv 다운로드 받아서, 중요한 저장

23. Console Login Link로 갈 수 있는 것이다.

24. 링크로 가서

    ```
    계정: 숫자
    사용자 이름: 프로젝트 이름
    비밀번호: qwer1234
    ```

25. ```bash
    $ pip freeze > requirements.txt
    이걸 통해서 가상환경들 백업
    ```

26. ```bash
    $ mkdir .ebextensions
    ```

27. 위 폴더에 django.config 파일 만들기.

28. ```json
    "**/*.config": "yaml",
    settings.json에 추가.
    ```

29. ```yaml
    option_settings:
      aws:elasticbeanstalk:container:python:
        WSGIPath: JunesMovie/wsgi.py
        
        쟝고 프로젝트를 시작하겠다. 기본 세팅
    ```

30. db-migrate.config 파일

    ```yaml
    container_commands:
      01_migrate:
        command: "python manage.py migrate"
        leader_only: true
      02_chown_sqlitedb:
        command: "sudo chown wsgi db.sqlite3"
        leader_only: true
      03_seed:
        command: "python manage.py loaddata users.json"
    
    options_settings:
      aws:elasticbeanstalk:application:environment:
        DJANGO_SETTINGS_MODULE: JunesMovie/settings
    ```

31. ```python
    04_collectstatic:
      command: "python manage.py collectstatic"
      leader_only: true
      이거 해줘야함.
    
    STATIC_ROOT = 'static'
    으로 설정하면 스태틱 할거다.
    ```

32. ```bash
    $ pip install awsebcli
    ```

33. ```bash
    $ eb --version
    EB CLI 3.16.0 (Python 3.7.4)
    버전 확인.
    ```

34. ```bash
    $ eb init
    
    Select a default region
    1) us-east-1 : US East (N. Virginia)
    2) us-west-1 : US West (N. California)
    3) us-west-2 : US West (Oregon)
    4) eu-west-1 : EU (Ireland)
    5) eu-central-1 : EU (Frankfurt)
    6) ap-south-1 : Asia Pacific (Mumbai)
    7) ap-southeast-1 : Asia Pacific (Singapore)
    8) ap-southeast-2 : Asia Pacific (Sydney)
    9) ap-northeast-1 : Asia Pacific (Tokyo)
    10) ap-northeast-2 : Asia Pacific (Seoul)
    11) sa-east-1 : South America (Sao Paulo)
    12) cn-north-1 : China (Beijing)
    13) cn-northwest-1 : China (Ningxia)
    14) us-east-2 : US East (Ohio)
    15) ca-central-1 : Canada (Central)
    16) eu-west-2 : EU (London)
    17) eu-west-3 : EU (Paris)
    18) eu-north-1 : EU (Stockholm)
    19) ap-east-1 : Asia Pacific (Hong Kong)
    20) me-south-1 : Middle East (Bahrain)
    
    You have not yet set up your credentials or your credentials are incorrect
    You must provide your credentials.
    (aws-access-id): AKIAR2Q6T5TALYVDYH64
    (aws-secret-key): hs6WyvlQnjhFKgF/sH1iIlH35N3z1pwqp0UQSOPF
    
    Enter Application Name
    (default is "movie-back"): mooving
    Application mooving has been created.
    
    It appears you are using Python. Is this correct?
    (Y/n): Y
    
    Select a platform version.
    1) Python 3.6
    2) Python 3.4
    3) Python 3.4 (Preconfigured - Docker)
    4) Python 2.7
    5) Python
    (default is 1): 1
    Cannot setup CodeCommit because there is no Source Control setup, continuing with initialization
    Do you want to set up SSH for your instances?
    (Y/n): n
    
    ```


## 여기서 부터는 heroku!

1. Google 에 Heroku 검색해서 가입만 해놓기.

2. ```
   Heroku ID
   snb0303@naver.com
   ```

3. ```
   $ git checkout -b heroku
   ```

4. ```bash
   아예 쟝고 폴더로 만들어버리기
   $ pip install django-heroku
   환경을 설정해주는 라이브러리
   설치만 해주면 끝!!!
   ```

5. ```bash
   $ vi Procfile
   web: gunicorn JunesMovie.wsgi --log-file -
   이렇게 내용 기입해준다.
   ```

6. ```bash
   $ pip install gunicorn
   ```

7. ```bash
   $ pip freeze > requirements.txt
   pypiwin32
   pywin32 는 지워버려야한다!
   ```

8. runtime.txt 만들어서

   ```txt
   python-3.7.4
   ```

   입력!

9. $ pip install python-decouple 도 깔아줘야함

10. ```python
    from decouple import config
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG')
    ALLOWED_HOSTS = ['*']
    STATIC_ROOT = 'static'
    ```

11. heroku.com 으로 들어가서 heroku cli 검색. 그리고 64bit짜리 설치. 설치하구 bash 들어가서

    ```bash
    $ heroku
    치면 아래에 정보들 쭉 나옴.
    ```

12. ```bash
    $ heroku login
    heroku: Press any key to open up the browser to login or q to exit:
    Opening browser to https://cli-auth.heroku.com/auth/browser/06168d45-69f6-42c5-92ae-eef147a8d983
    Logging in... done
    Logged in as snb0303@naver.com
    ```

13. ```bash
    $ heroku create mooving-api-django-server
    Creating ⬢ mooving-api-django-server... done
    https://mooving-api-django-server.herokuapp.com/ | https://git.heroku.com/mooving-api-django-server.git
    ```

14. $ git remote -v 이거 하면 헤로쿠 등록된게 보인다.

15. 헤로쿠에 환경변수 세팅

    ```bash
    $ heroku config:set SCRETE_KEY='$bm*_f=$#auyrr=j3(a_@j7r5mp7(pp3%k(v4!%$%ke+sf--@)'
    
    ```

    이 방법말고 사이트에 가서 직접 해주자.!!!

    해주고 나서 git add 랑 git commit 까지 해주고

16. ```bash
    $ git push heroku heroku:master
    ```

17. 



```bash
$ git push heroku heroku:master
Enumerating objects: 63, done.
Counting objects: 100% (63/63), done.
Delta compression using up to 8 threads
Compressing objects: 100% (59/59), done.
Writing objects: 100% (63/63), 405.12 KiB | 5.26 MiB/s, done.
Total 63 (delta 16), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote:  !     Python has released a security update! Please consider upgrading to python-3.7.6
remote:        Learn More: https://devcenter.heroku.com/articles/python-runtimes
remote: -----> Installing python-3.7.4
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: Sqlite3 successfully installed.
remote: -----> Installing requirements with pip
remote:        Collecting asgiref==3.2.3 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/a5/cb/5a235b605a9753ebcb2730c75e610fb51c8cab3f01230080a8229fa36adb/asgiref-3.2.3-py2.py3-none-any.whl
remote:        Collecting dj-database-url==0.5.0 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/d4/a6/4b8578c1848690d0c307c7c0596af2077536c9ef2a04d42b00fabaa7e49d/dj_database_url-0.5.0-py2.py3-none-any.whl
remote:        Collecting Django==3.0.3 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/c6/b7/63d23df1e311ca0d90f41352a9efe7389ba353df95deea5676652e615420/Django-3.0.3-py3-none-any.whl (7.5MB)
remote:        Collecting django-cors-headers==3.2.1 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/19/4e/dd037bf42cc33d1d61e45b973507303afad14fc18bd36329ec8ab3673373/django_cors_headers-3.2.1-py3-none-any.whl
remote:        Collecting django-heroku==0.3.1 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 5))
remote:          Downloading https://files.pythonhosted.org/packages/59/af/5475a876c5addd5a3494db47d9f7be93cc14d3a7603542b194572791b6c6/django_heroku-0.3.1-py2.py3-none-any.whl
remote:        Collecting djangorestframework==3.11.0 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 6))
remote:          Downloading https://files.pythonhosted.org/packages/be/5b/9bbde4395a1074d528d6d9e0cc161d3b99bd9d0b2b558ca919ffaa2e0068/djangorestframework-3.11.0-py3-none-any.whl (911kB)
remote:        Collecting djangorestframework-jwt==1.11.0 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 7))
remote:          Downloading https://files.pythonhosted.org/packages/2b/cf/b3932ad3261d6332284152a00c3e3a275a653692d318acc6b2e9cf6a1ce3/djangorestframework_jwt-1.11.0-py2.py3-none-any.whl
remote:        Collecting gunicorn==20.0.4 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 8))
remote:          Downloading https://files.pythonhosted.org/packages/69/ca/926f7cd3a2014b16870086b2d0fdc84a9e49473c68a8dff8b57f7c156f43/gunicorn-20.0.4-py2.py3-none-any.whl (77kB)
remote:        Collecting haversine==2.2.0 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 9))
remote:          Downloading https://files.pythonhosted.org/packages/72/8e/6df8b563dd6b2961a36cd740b34c00b89142f1b97d92092c133379b2973f/haversine-2.2.0-py2.py3-none-any.whl
remote:        Collecting psycopg2==2.8.4 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 10))
remote:          Downloading https://files.pythonhosted.org/packages/84/d7/6a93c99b5ba4d4d22daa3928b983cec66df4536ca50b22ce5dcac65e4e71/psycopg2-2.8.4.tar.gz (377kB)
remote:        Collecting PyJWT==1.7.1 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 11))
remote:          Downloading https://files.pythonhosted.org/packages/87/8b/6a9f14b5f781697e51259d81657e6048fd31a113229cf346880bb7545565/PyJWT-1.7.1-py2.py3-none-any.whl
remote:        Collecting python-decouple==3.3 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 12))
remote:          Downloading https://files.pythonhosted.org/packages/c7/82/dd20cdca396f58be86c6e710a3958f4a34ca98c5dd3989ee978b6cb9f97e/python-decouple-3.3.tar.gz
remote:        Collecting pytz==2019.3 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 13))
remote:          Downloading https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl (509kB)
remote:        Collecting sqlparse==0.3.0 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 14))
remote:          Downloading https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
remote:        Collecting whitenoise==5.0.1 (from -r /tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/requirements.txt (line 15))
remote:          Downloading https://files.pythonhosted.org/packages/ae/25/0c8f08c9d3c93192cd286594f1e87b17bab496fb9082c2a69e17051b91fd/whitenoise-5.0.1-py2.py3-none-any.whl
remote:        Installing collected packages: asgiref, dj-database-url, pytz, sqlparse, Django, django-cors-headers, psycopg2, whitenoise, django-heroku, djangorestframework, PyJWT, djangorestframework-jwt, gunicorn, haversine, python-decouple
remote:          Running setup.py install for psycopg2: started
remote:            Running setup.py install for psycopg2: finished with status 'done'
remote:          Running setup.py install for python-decouple: started
remote:            Running setup.py install for python-decouple: finished with status 'done'
remote:        Successfully installed Django-3.0.3 PyJWT-1.7.1 asgiref-3.2.3 dj-database-url-0.5.0 django-cors-headers-3.2.1 django-heroku-0.3.1 djangorestframework-3.11.0 djangorestframework-jwt-1.11.0 gunicorn-20.0.4 haversine-2.2.0 psycopg2-2.8.4 python-decouple-3.3 pytz-2019.3 sqlparse-0.3.0 whitenoise-5.0.1
remote: 
remote: -----> $ python manage.py collectstatic --noinput
remote:        163 static files copied to '/tmp/build_52fe0d19e00192f0a9677e08bbaa4f5c/static'.
remote: 
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 56.8M
remote: -----> Launching...
remote:        Released v7
remote:        https://cafemoa-django.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/cafemoa-django.git
 * [new branch]      heroku -> master
(venv) 
지렸다 뭔가..
```

```bash
$ yarn build
yarn run v1.22.0
$ react-scripts build
Creating an optimized production build...
Compiled successfully.

File sizes after gzip:

  367.54 KB  build\static\js\2.89061373.chunk.js
  80.6 KB    build\static\css\2.3da2b790.chunk.css
  5.94 KB    build\static\js\main.323ebc5d.chunk.js
  2.59 KB    build\static\css\main.d873af95.chunk.css
  783 B      build\static\js\runtime-main.fb7ee4a6.js

The project was built assuming it is hosted at the server root.
You can control this with the homepage field in your package.json.
For example, add this to build it for GitHub Pages:

  "homepage" : "http://myname.github.io/myapp",

The build folder is ready to be deployed.
You may serve it with a static server:

  yarn global add serve
  serve -s build

Find out more about deployment here:

  bit.ly/CRA-deploy

Done in 66.99s.
```

```bash
$ firebase deploy

=== Deploying to 'cafemoa-bbe6b'...

i  deploying hosting
i  hosting[cafemoa-bbe6b]: beginning deploy...
i  hosting[cafemoa-bbe6b]: found 1 files in dist
+  hosting[cafemoa-bbe6b]: file upload complete
i  hosting[cafemoa-bbe6b]: finalizing version...
+  hosting[cafemoa-bbe6b]: version finalized
i  hosting[cafemoa-bbe6b]: releasing new version...
+  hosting[cafemoa-bbe6b]: release complete

+  Deploy complete!

Project Console: https://console.firebase.google.com/project/cafemoa-bbe6b/overview
Hosting URL: https://cafemoa-bbe6b.firebaseapp.com
```

