# Git

### 기본 명령어

1. Git 저장소 설정

   ```
   $ git init
   ```

   주의! 반드시 현재 디렉토리에 git을 사용하고 있는지, (master) 표기가 없는지 확인할 것!

2. git add

   `git add`는 현재 working directory에서 commit 할 목록에 파일들을 담아놓는 것이다.

   그리고 그 목록은 `Index(staging area)`라고 한다.

   ```
   $ git add <폴더이름 혹은 파일이름>
   ```

3. git commit

   현재 소스코드 상태를 저장하는것, **스냅샷**을 찍는것과 동일하다.

   `staging area`(git add로 추가한 파일들이 담기는 곳)에 있는 내용을 이력으로 기록한다.

   ```
   $ git commit -m "커밋 메세지"
   ```

4. git status

   git의 현재 상태를 확인한다.

   커밋할 목록에 담겨있는지 혹은 untracked인지, 커밋할 내역이 있는지 등등 다양한 정보를 제공한다.

   ```
   $ git status
   ```

5. git log

   현재까지 커밋된 모든 이력을 확인할 수 있다.

   ```
   $ git log
   ```
   
6. git remove

   ```bash
   $ git remote remove origin
   ```

7. git init 자체를 삭제하기

   ```bash
   rm -rf .git
   ```



## 원격 저장소 활용하기



1. 원격 저장소(remote repository) 등록하기

   ```
   $ git remote add origin __경로__
   ```

   원격 저장소(remote)를 등록(add) 한다. origin 이라는 이름으로!

   최초에 한번만 등록하면 된다.

   아래의 명령어로 현재 등록된 원격 저장소를 확인할 수 있다.

   ```
   $ git remote -v
   origin  https://github.com/blueboy1593/TIL.git (fetch)
   origin  https://github.com/blueboy1593/TIL.git (push)
   ```

2. remote 삭제해버리기

   ```bash
   $ git remote remove origin
   이 코드를 사용하면 깃 리모트를 삭제하고 새로 할 수 있다.
   ```

3. 원격 저장소에 올리기

   ```
   $ git push origin master
   ```

   origin이라는 원격저장소의 master 브랜치로 지금까지의 커밋 내역을 올려줘!

   origin은 원격 저장소의 이름

   master는 브랜치의 이름

4. 원격 저장소에서 가져오기

   ```
   $ git pull origin master
   ```

5. 원격 저장소를 로컬에 복사하기

   ```
   $ git clone __경로__
   ```

   다운받기를 원하는 폴더에서 git bash를 열고 위의 명령어를 입력한다.

   경로는 github에서 우측에 있는 초록색 버튼을 누르면 나타난다.
   
6. Git Bash 에 등록되어 있는 정보 확인하기

   ```bash
   $ git config --global user.name
   $ git config --global user.email
   ```

7. Git 협업하기 명령어

   Master 주소에서 Fork 따오기

   Pull request 하기

   ```bash
   git remote add upstream (주인의 주소)
   git push upstream master
   git pull upstream master
   ```

   

ref: https://backlog.com/git-tutorial/kr/



# Branch 연습

```bash
$ git checkout -b eb-deploy
로 가지 새로 만들어서 들어옴.

$ git checkout f6b1a8b930643d263e1e00fecf7d5edfa9a5cb47
이건 뭘까? 이전에 작업했던 내용....?

$ git branch
  eb-deploy
  master
* tmp
어떤 브랜치가 있는지 확인

$ git branch -D master
$ git checkout -b master
이걸로 현재 새로 브랜치를 만든다.!!

$ git push origin +master
이 명령어는 추가 push인 듯.

```



