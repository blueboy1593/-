# Vue_Start

SPA: Single Page Application

html은 한개!! 하나의 html에서 우리는 파트를 나눠서 할 것이다!!

```
Vue.js devtools
설치 크롬 확장 프로그램!!!
```

여기서 이벤트같은거 다 확인할 수 있다.

## div 파트

```html
div#app 으로 id 자동완성 가능합니다!!!

<div>
    {{ message }}
    <div id="app">
        {{ message }}
    </div>
</div> 
app이 아닌 친구에게 이렇게 하면

{{ message }}
Hello, Vue!

이런 식으로 텍스트가 그대로 출력된다.

<button v-on:click="plus">plus</button>
<button v-on:click="minus">minus</button>
<!-- 이거는 v-on을 하면 플러스라는 함수를 하라고 하는거 같은데...? -->

<li v-for="todo in todos" v-if="!todo.completed" @click="toggleTodo(todo)">
    {{ todo.content }}
</li>
<li v-else v-on:click="toggleTodo(todo)">[완료!]</li>
if 문과 for문 그리고 click하는 기능 등은 이렇게 구현 가능하다!

```

## Script Part

```html
methods: {
        plus: function() {
          // function 키워드로 함수정의를 해야 this 가 Vue 인스턴스를 가르친다.
          // 애로우 function에서 views는 윈도우 머시기를 가르친다.
          // 이렇게 만들어주는게 굉장히 중요해
          this.count++
        },
        minus: function() {
          this.count--
        }
      }

methods: {
        toggleTodo: function(todo){
          todo.completed = !todo.completed
          // 이거 true false를 왔다갔다 하면서 자유자재로 할 수 있는 그런 기능인듯
        }
      },
```

## Vue.js

```javascript
app.message = "by"
"by"
app.count = 101
101
app.$data
{__ob__: Observer}
app.$data.message = "가능합니당"
"가능합니당"
```

// 1. Vue instance 에 함수를 "정의할때" 는 function 키워드를 사용한다.

// 2. Vue instance 에 정의된 함수 내에서 callback 함수를 사용할 때 arrow function 을 사용한다.

```html
<li v-for="todo in todos">
    <input v-model="todo.completed" type="checkbox">
    {{ todo.content }}
</li>
v-model은 링크를 시켜줌
```

### async await

```javascript
const handleData = async function() {
  const response = await getDataPromise()
  console.log(response)
}
```



# npm init

```bash
# 1. node project 시작
$ npm init

# 2. vue 설치
$ npn install vue # === "npm i vue"

# 3. Webpack 설치
# -D 는 개발환경에서만 사용하겠다. 옵션
# webpack 은 개발자의 편의성을 위한 툴
$ npm i -D webpack webpack-cli

# 4. webpack 설정파일 설정
$ touch webpack.config.js

# 5.
$ npm install -D vue-loader vue-template-compiler
```



















