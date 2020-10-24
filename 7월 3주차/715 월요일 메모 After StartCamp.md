# 7/15 월요일 메모 After StartCamp

## StartCamp Review

Open Source 

API(Application Programming Interface)

CLI(Command Line Interface)

Web Crawling

git & GitHub

Working directory -> INDEX -> HEAD -> GitHub

HTML(정적 웹) & CSS

Flask 동적 웹처럼 서비스가 어떻게 돌아갈 수 있을까 그려주는 것.

Client(브라우저) & Server

request & response 요청과 응답 JSON형식의 타입으로도 할 수 있음.

Telegram으로 챗봇 만들어봄. 브라우저 뿐만 아니라 다른 플랫폼에서도 할 수 있다.

pythonanywhere로 언제 어디서든 끊김 없게 베포할 수 있음. 단, 여기는 1개 까지만.

## Python Week

Github는 오픈 소스계의 성지이다. 그 중에서 star라는 기능이 있음.(인기도 측정?)

배워보려고 하는 것!

1) Bootstrap 4 - Responsive Web 스타일을 많이 쉽게 적용시킬 수 있다.

2) Flask와 SQL(데이터베이스를 조작하는 언어)

SQL을 통해 데이터베이스를 어떻게 조작할 수 있는지.

3) django(main)

메인이라고 볼 수 있음. Flask같은 웹을 만드는 프레임워크 중 하나. 이 프레임워크로 쉽게 웹을 만들 수 있음.

이런 것까지 전부 다 해줘? 라는 느낌.

4) JS(Java Script)

동적으로 다루는 것. 웹 3총사 중 하나.

aws(아마존 웹 서비스)라는 클라우드 컴퓨팅 파워를 빌려서 우리가 만든 웹 어플리케이션을 운영.

pip install = 파이썬에서 새로운 모듈을 설치할 때 사용하는 것.

```
pip install jupyter
jupyter notebook
을 해서 나오는 URL은 켜놔야한다.
```

로컬 호스트 8888 라는 식으로 나오는 것.

```python
vi ~/.bashrc # 편집툴임.
alias jn="jupyter notebook"
cat .bashrc
touch .bash_profile
source .bashrc
jn
```

touch 는 새로운 빈 파일을 생성

jn은 약간 링크를 만드는 느낌인가???

Github에서 profile로 들어가서 organization으로 가면 있다.

PEP-8 : 파이썬에서 제공하는 스타일 가이드. 이를 활용해서 작성함.

jupyter notebook은 설계부터 마우스를 없이도 조작이 가능하도록 설계되어있음.

jupyter를 키지 않으면 실행이 되지 않는다.

```python
pip install jupyter_contrib_nbextensions
jupyter contrib nbextensions install --user
# 위의 과정들은 확장 프로그램을 설치하는 과정이다.
```

구글에 jupyter notebook extensions을 검색하면 이에 대한 정보들을 얻을 수 있다.

table of contents 기능 : 목차를 만들어준다.

ctrl + enter : 해당 기능을 실행시키는 기능

shift + enter : 실행시키고 다음 블럭으로 넘어가는 기능

```python
import keyword
print(keyword.kwlist)
```

내장 모듈은 그냥 하면 되고 외장 모듈은 import로 뽑아와야한다.

쥬피터 노트북은 위쪽에서 실행한 내용들이 메모리에 저장이 되어있음.

파이썬 한줄로 표기할 때에는 ;을 사용하면 된다.

id는 메모리 어딘가에 저장이 되어있는 공간의 id값이 출력됨.

## After Lunch

development 폴더 생성(student 안에)

```
$ ls -al
```

a라는 옵션은 숨긴 폴더나 파일까지 다 보여달라는 명령어

commit은 버전을 의미하는건가? 그럼 커밋마다 자료들이 다 별개로 존재하는 것?

```
git init
$git remote add origin URL
$git remote -v
잘 되었는지 확인해보는 것!
근데 origin은 함수 개념???...
```

아이디랑 비밀번호는 day1 아니면 day2에 했었지.

```
jupyter notebook
python -m notebook
을 치면 하던게 자동으로 켜진다.
```

## Python 기초 - 2. 변수(variable) 및 자료형

변수가 더 많게 되면 오류가 난다.

```python
# n 진수를 만들어보고, 출력 해봅시다.
binary_number = 0b10
octal_number = 0o10
decimal_number = 10
hexadecimal_number = 0x10
print(f'''
2진수 : {binary_number}
8진수 : {octal_number}
10진수 : {decimal_number}
16진수 : {hexadecimal_number}
'''
)
```

```python
# 복소수와 관련된 메소드들을 확인해봅시다.
# 메소드는 함수를 칭하는 말. 펀션도 함수를 칭하는 말이다.
print(a.imag)
print(a.real)
print(a.conjugate())
# imag는 허수 부분
# real은 실수 부분
# conjugate는 켤레복소수
-4.0
3.0
(3+4j)
```

문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능하다.

자신마다 익숙한 형식을 해주는 것이 좋다.

사용자에게 받는 input은 기본적으로 str임

\\\ 이거 두개를 활용해서 분리 가능하다.

```
1) %-formatting

2) str.format()

3) f-strings : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.
```

이거 3가지 모두 알아두면 좋다.

특히, 3번째는 나온지가 얼마 안된 최신 기능이다. 그만큼 편하고 활용 가능성이 많다.

## 연산자와 형변환!!!

True는 암시적으로 1을 의미한다.

### 시퀀스(sequence) 자료형

`시퀀스`는 데이터의 순서대로 나열된 형식을 나타낸다. 

**주의! 순서대로 나열된 것이 정렬되었다라는 뜻은 아니다.**

파이썬에서 기본적인 시퀀스 타입은 다음과 같다.

1. 리스트(list)

2. 튜플(tuple)

3. 레인지(range)

4. 문자열(string)

5. 바이너리(binary) : 따로 다루지는 않습니다.

- `set`과 `dictionary`는 기본적으로 순서가 없습니다.
- 순서가 없는 것이 포인트



## 마지막 숙제

cd homeworkshop

touch 는 그냥 생성인가?
