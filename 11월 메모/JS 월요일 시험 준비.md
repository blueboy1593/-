# 월요일 시험

1. typeof 이거 겁나 중요함. 한문제 나올듯

   ```javascript
   typeof[1,2,3]
   typeof {1,2,3}
   typeof 1234
   typeof null
   typeof NaN
   typeof Infinity
   ```

2. for 문 in이랑 of 차이 알아두기

   in 은 인덱스 번호, of 은 값 나옴

   ```javascript
   numbers = [1,2,3,4,5]
   for (const number in numbers) {
       console.log(number)
   }
   for (const number of numbers) {
       console.log(number)
   }
   ```

3. == 가 야기할 수 있는 문제들 <-- 동등 연산자

   === 를 쓰면 완전 해결 가능 <-- 일치 연산자

   ```javascript
   0 == '0'
   true
   0 == []
   true
   '0' == []
   false
   ```

4. 엔드게임 인덱스 접근하는거 조심. my-lovers 이런거 형식에 맞지 않다.

   ```javascript
   const endGame = {
   title: '어벤져스: 엔드게임',
   'my-lovers': [
   {name: '아이언맨', actor: '로다주'},
   {name: '헐크', actor: '마크 러팔로'}
   ]
   }
   endGame.title
   "어벤져스: 엔드게임"
   endGame['title']
   "어벤져스: 엔드게임"
   endGame.my-lovers
   VM560:1 Uncaught ReferenceError: lovers is not defined
       at <anonymous>:1:12
   이런 식으로 구리게 나온다.
   
   endGame["my-lovers"]
   (2) [{…}, {…}]
   일반적이지 않은 것은 이렇게 접근 가능.
   endGame["my-lovers"][0]
   {name: "아이언맨", actor: "로다주"}
   ```

5. syntatic sugar

   ```javascript
   const abc = 123
   undefined
   const obj = { abc : abc }
   undefined
   obj
   {abc: 123}
   const obj = { abc }
   // 위와 같은 형식으로 줄여서 쓸 수 있다.
   ```

6. this 짚고 넘어가기

   ```javascript
   const me = {
   name: 'Kim',
   greeting: function(message) {
   return `${this.name} : ${message}`
   }
   }
   undefined
   me.name
   "Kim"
   me.greeting()
   "Kim : undefined"
   me.greeting(124155)
   "Kim : 124155"
   ```

   일반적 함수 실행은 전역 개체로부터 실행되는 것.

   전역에서 this는 window 이다

   ```js
   this
   Window {parent: Window, opener: null, top: Window, length: 3, frames: Window, …}
   this == window
   true
   this === window
   true
   ```

7. Json - JavaScript Object Notation 자바스크립트 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포멧이다.

   ```js
   JSON.stringify(obj)
   "{"abc":123}"
   제이슨 형태로 바꿔주는 것.
   
   json
   "{"abc":123}"
   JSON.parse(json)
   {abc: 123}
   ```

   오브젝트를 string 값으로 바꾸고 string을 object 로 바꿔줄 수 있다.

8.  Array Helper Methods

   ```
   forEach 포문 돌려주는 것.
   map 도 for처럼 하나씩 돌면서 만들어줌
   filter 조건에 맞는 것을 필터링한다.
   find 특정 조건에 부합하는 첫번째 아이템을 반환하겠다.
   every 특정 조건에 모든 배열이 조건을 가지면 true
   some 하나라도 특정 조건을 만족하면 true
   reduce 위에 있는 것들을 다 구현할 수 있는 만능의 도구
   ```

9. Event Listener 구분하기. 어떤 것들이 있나 알아두기.

10.  DOM selector 

    ```
    querySelector()     ---- 하나만 가져옴
    querySelectorAll()  ---- 해당하는 모든 것을 가져와. 그래서 배열의 형태로 가져올 것이다.
    이 두가지 차이 알기
    ```

11. 이거 중요하다고 함

    ```javascript
    const icon = document.querySelector('.icon')
    undefined
    icon.addEventListener('click', function() {
        console.log(123)
        console.log(this)
    })
    
    여기서 icon과 this 는 같다!!!
    ```

12. axios

    희망편과 절망편 참조.

    ```js
    axios는 브라우저에서 XHRXMLHttpRequest)를 보내주고 그 결과를
    promise 객체로 반환해주는 라이브러리이다.
    
    axios.get()
    	.then(res => console.log(res))
    	.then(() => {})
    	.catch(error => console.error)
    ```

    비동기적이기 때문에 우리가 생각하는 것과 좀 다르게 동작한다. 여기는

13.  Ajax 및 django 

    쭉 한번 그냥 읽어보고, 내용 그냥 한번 보기. 설마 나오겠나 여기....

    ```js
    쟝고에서 Ajax 마지막에 좋아요 기능 바꿀때 썼었음.
    axios.post
    처럼 post로 바꿔서 보내주는 것.
    get이었던 axios를 포스트로 바꿈.
    
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
    
    이거 뭔가 은근 강조하심
    ```

    이렇게 하면 post 로 보낼때 쟝고로 csrftoken을 잘 전달할 수 있다.

나머지는 개념적인 부분들 잘 읽어보면 된다.

14. 브라우저는 싱글쓰레드에서 이벤트 기반(event driven) 방식으로 실행된다.  

    이 부분 공부를 잘 해보면 좋을 것.