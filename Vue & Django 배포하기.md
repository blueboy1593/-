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

12. ? Configure as a single-page app (rewrite all urls to /index.html)? (y/N)

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

    

35. Google 에 Heroku 검색해서 가입만 해놓기.

36. ```
    Heroku ID
    snb0303@naver.com
    ```

37. 