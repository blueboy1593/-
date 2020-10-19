# Django & Vue js

```bash
$ npm install -g
이거는 기본 nodejs 설치하구 해주는건가?
$ deactivate
로 끝내주기
$ npm i -g @vue/cli
이거는 글로벌로 설치 하는건가....?
$ vue create todo-front
이건 그냥 vue 프론트엔드 파일 만드는 코드!!!
$ rm -rf .git
이거 쫌 유용한거같은데...?
깃으로 관리되지 않도록 하게 만드는 것!
$ rm .gitignore
파일 삭제하는거
$ vue ui
프로젝트 매니저를 뭔가 만들어준다.
$ npm i bootstrap bootstrap-vue
부트스트랩 까는거.
이거 깔아줘야 부트스트랩 해줄 수 있다.
$ npm i axios
axios 까는거당.
$ npm i vue-session
뷰세션 까는 것.
$ npm i jwt-decode
jwt-decode 까는 것.

$ pip install djangorestframework
$ pip install djangorestframework-jwt
쟝고 레스트프레임워크에서 jwt 인증을 해주는 프레임워크 이다.
$ pip install django-cors-headers
쟝고에서 얘가 설치되어있으면 다른 곳에서부터 리소스를 가져가는 것을 허용해줌.
```

vue ui를 통해서 설치하는 것은 알아서 추가도 자동으로 된다.



## Package.json

```json
"eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/essential",
      "eslint:recommended"
    ],
    "rules": {
      "no-console": "off"
    },
    노콘솔 중요해 노콘술!!! 
    이거 허락을 해줘야하는거야 알았지??
```

.env.local

api나 뭔가 숨기고 싶은 내용을 넣어놓는 곳이다.