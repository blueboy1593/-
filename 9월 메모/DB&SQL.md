# 09/18 수요일 메모

## 데이터베이스

### RDBMS 관계형 데이터베이스 관리 시스템

### SQL(Structured Query Language)

데이터 관리를 위해 설계된 특수 목적의 프로그래밍 언어

### 설치 과정

1. student\sqlite\ 폴더에 설치해주기.

2. 계정의 환경 변수 편집

   위에 변수 중 path 더블클릭

   C:\Users\student\sqlite 추가해주기.

   왜 하는건지는 잘 모른다!

3. database 폴더 만들고 VScode 열어버리고 ctrl + Z 엔터 또는 .exit 엔터로 빠져나오기.

4. sqlite3 tutorial.sqlite3 입력.

   .databases 입력

   .help 입력하면 도움말이 나온다.

   ```bash
   sqlite> .mode csv
   sqlite> .import hellodb.csv examples
   sqlite> SELECT * FROM examples;
   1,"길동","홍",600,"충청도",010-2424-1232
   csv 파일을 가지고 와서 테이블을 만드는 명령이라고 한다.
   ```

5. ```bash
   sqlite> .headers on
   sqlite> .mode column
   sqlite> SELECT * FROM examples;
   id          first_name  last_name   age         country     phone
   ----------  ----------  ----------  ----------  ----------  -------------
   1           길동          홍           600         충청도         010-2424-1232
   이런식으로 이쁘게 만들어주는 것이다!!
   ```

6. ```ba
   sqlite> CREATE TABLE classmates (
      ...>         id INTEGER PRIMARY KEY,
      ...>         name TEXT
      ...> );
   sqlite> .tables
   classmates  examples
   sqlite> .schema classmates
   CREATE TABLE classmates (
           id INTEGER PRIMARY KEY,
           name TEXT
   );
   sqlite> .schema examples
   CREATE TABLE examples(
     "id" TEXT,
     "first_name" TEXT,
     "last_name" TEXT,
     "age" TEXT,
     "country" TEXT,
     "phone" TEXT
   );
   스키마 라는 명령으로 특정 테이블이 어떻게 생겼는지 어떤 기능들이 있는지 볼 수 있다!
   sqlite> DROP TABLE classmates;
   이거는 테이블을 삭제하는 명령어입니다.
   ```

7. COUNT, AVG, SUM, MIN, MAX 등등 있음.

ALTER TABLE exist_table

RENAME TO new_table;