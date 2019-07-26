# 7/26 금요일 Project 2

## 1. 목표

1) 이번에는 Naver의 API를 사용해서 진행하는 프로젝트.



1. 어플리케이션 등록.
2. 사용 API : 검색
3. 환경 추가 WEB 설정

**Client ID** m0YexGybNHVSbIufIkoM

**Client Secret** Wf5J1MVe_H

Documents -> 서비스 API > 검색 > 영화

네이버 영화 검색 결과를 출력해주는 REST API입니다. 비로그인 오픈 API이므로 GET으로 호출할 때 HTTP Header에 애플리케이션 등록 시 발급받은 [Client ID와 Client Secret 값을 같이 전송](https://developers.naver.com/docs/common/apicall)해 주시면 활용 가능합니다.

이런 요구들을 따라줘야 합니다.

호출 예시를 잘 살펴봐야 한다.

헤더는 요청에 대한 정보들이 담겨있는 곳이다.

```
{'errorCode': '024',
 'errorMessage': 'Not Exist Client ID : Authentication failed. (인증에 실패했습니다.)'}
```

헤더를 보내지 않았기에 인증에 실패한 것.

모든 데이터는 바이너리 타입으로 되어 있다. 바이너리 파일로 응답을 받고 작성.<- 원리

네이버로 영화 요청을 보낼 때, 포문을 돌리면 속도가 너무 빠른 컴퓨터가 보내면 차단을 하는 경우가 있다. 

```
import time

time.sleep(3)
3초동안 슬립을 했다가...?
포문 안쪽에서 
time.sleep(0.1)
```

여러가지 정보들이 주어질 수 있는데, 우리가 원하는 것들을 위해서 검증 과정을 해주는 것도 좋다.



## Step 1

csv reading을 해서 movie코드를 리스트로? 받아오는게 좋겠지 아무래도.

질문) dictionary의 key 값으로만 구성할 수 있나??

오픈 reading 안에 모든 것을 넣어도 된다.

딕셔너리의 리스트로.





