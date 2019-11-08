# JavaScript 입문

Java 와 JavaScript는 전혀 연관성이 없다.

자바의 유명세에 탑승하고자 자바스크립트로 네이밍한 것.

```
ctrl + L 누르면 콘솔에서 내용 사라짐
```

파이썬을 하면서 언어적인 base가 있기 때문에 다른 언어를 할 때에는 이렇게까지 어렵지 않았다 했을것.

VSCODE는 자바스크립트 개발하기에 진짜 최적화된 앱이라고 한다.

```bash
 vi .gitconfig
를 통해서 email과 name을 확인할 수 있다.
```

```
ctrl + shift + i 해서
Open settings(json)
"[javascript]": {
        "editor.tabSize": 2
    },
자바스크립트 탭사이즈 2로 만들어주기.
```

ctrl + , 를 누르면 settings가 켜지는데 여기서 이런저런 설정을 하면 된다. detect indentation을 꺼줘버리기

### 주석

```javascript
/*
      여러줄에 걸친 주석
    */
    // 한줄짜리 주석
```

### 00_variable

```javascript
let x = 1
let x = 3
이런식으로 재 선언은 할 수 없지만,
x = 3 으로 재할당은 가능하다.

console.log(x)
콘솔에 로그를 남기겠다.

print(x)는 진짜 프린트를 하려 하는 것.

if (x === 3) {
    let x = '안녕하세요'
    console.log(x)
}
console.log(x)
안녕하세요
3
이렇게 출력이 된다.
중괄호 안쪽에서만 접근되는 새로운 변수. 함수 안에서 쓰다가 없어지는 것과 비슷한 원리이다.

if (x === 3) {
    let message = '안녕하세요'
    console.log(message)
    // 중괄호 안쪽에서만 접근되는 새로운 변수. 함수 안에서 쓰다가 없어지는 것과 비슷한 원리이다.
}
console.log(message)
Uncaught ReferenceError: message is not defined
```

### 01_types_and_operators

```javascript
const sentence1 = 'Ask and go to the blue'
const sentence2 = "Ask and go to the blue"
const sentence3 = `Ask and go to the blue`

자스에서는 이렇게 3가지로 표현해줄 수 있음.

```

# 2일차

```
http://zzu.li/dino 로 접속
자바스크립트 DOM 조작
Document Object Model
html 문서 모두를 조작할 수 있는 자바스크립트 객체 모델
```

```javascript
document.querySelector('div.bg')
이런식으로 선택할 수 있다.
const bg = document.querySelector('div.bg')
지정지정지정
bg.querySelector('#dino')
셀렉트한 것의 세부로 또 들어갈 수 있는 것!!!
```

```javascript
대상의 자식 요소 삭제하기.
bg.firstElementChild
이거슨 가장 첫번째 자식
bg.lastElementChild
마지막 자식이다
bg.removeChild(bg.firstElementChild)
삭제하는 것!!!
    
document.createElement('img')
이런식으로 태그 만들기
const newDino = document.createElement('img')
newDino.id = 'newDino'

bg.appendChild(newDino)
자식을 추가해줄 수 있는 것.
```

```javascript
// dino 를 클릭 시 console 창에 '아야!' 가 입력되는 이벤트를 등록!
      const dino2 = document.querySelector('#newDino')
      dino2.addEventListener('click', () => {
        console.log('아야아야!')
      })
```

방향키를 눌렀을 때에만 event를 출력하게 만들어주는 기능

```javascript
// 이것은 문서 전체에 이벤트를 걸 예정
      document.addEventListener('keydown', event => {
        // 방향키를 눌렀을 때만 event 를 출력할 수 있도록 조건문을 작성
        if (event.key === 'ArrowDown') {
          console.log(event)  
        }
        else if (event.key === 'ArrowUp') {
          console.log(event)  
        }
        else if (event.key === 'ArrowLeft') {
          console.log(event)  
        }
        else if (event.key === 'ArrowRight') {
          console.log(event)  
        }
      })
```

상하좌우로 공룡이 왔다갔다하는거 기능

```javascript
document.addEventListener('keydown', event => {
        // 방향키를 눌렀을 때만 event 를 출력할 수 있도록 조건문을 작성
        if (event.key === 'ArrowDown') {
          console.log('아래')
          updown += 10
          dino.style.marginTop = `${updown}px`
          dino.style.marginBottom = `${-updown}px`
        }
        else if (event.key === 'ArrowUp') {
          console.log('위')
          updown -= 10
          dino.style.marginTop = `${updown}px`
          dino.style.marginBottom = `${-updown}px`
        }
        else if (event.key === 'ArrowLeft') {
          console.log('왼쪽')
          leftright += 10
          dino.style.marginLeft = `${-leftright}px`
          dino.style.marginRight = `${leftright}px`
        }
        else if (event.key === 'ArrowRight') {
          console.log('오른쪽')
          leftright -= 10
          dino.style.marginLeft = `${-leftright}px`
          dino.style.marginRight = `${leftright}px`
        }
      })
```

실습: 마우스를 갖다 대려고 할 때 도망가게 만들기

```javascript
Math.random()
```

## 실습: 쇼핑리스트 만들어서 지우기 기능 만들기

```javascript
const h1 = document.querySelector('h1')
undefined
h1
<h1>​My Shopping List​</h1>​
h1.innerText
"My Shopping List"
```

# npm

```bash
npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (day03)
version: (1.0.0)
description:
entry point: (00_non_blocking.js)
test command:
git repository:
keywords:
author:
license: (ISC)
About to write to C:\Users\student\KangHyun\javascript\day03\package.json:

{
  "name": "day03",
  "version": "1.0.0",
  "description": "",
  "main": "00_non_blocking.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}

$ npm install axios
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN day03@1.0.0 No description
npm WARN day03@1.0.0 No repository field.

+ axios@0.19.0
added 5 packages from 8 contributors and audited 5 packages in 0.626s
found 0 vulnerabilities
```

# axios

```javascript
const axios = require('axios')

const url = 'https://jsonplaceholder.typicode.com/posts/1'

axios.get(url)
.then(function(response) {
  console.log(response.data)
})
```

