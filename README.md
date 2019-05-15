# Band형 그룹핑 SNS 서비스 - SIG

------

#### Smilegate Winter Dev Camp



- 팀명 : JustCoding
- 개발기간 :  2019년 1월 14일 ~ 2019년 2월 26일
- 소개: SIG는 Special Interest Group의 약자로 특정 주제에 관심이 있는 사람들끼리의 모임을 위한 SNS 서비스 라는 뜻을 담았다. 네이버의 Band 서비스를 모방하여 서비스의 주요 기능과 특징을 가져왔다. 주요 기능으로는 밴드 방 생성, 친구 초대, 글 및 댓글 작성, 채팅 등이 있다. 백앤드는 Django, 프론트 앤드는 Vue.js를 활용하였다. 

------



## 주요기능

 

## 폴더 구조

#### - 서버(Backend)

- Backend/AuthServer : **인증서버** - 로그인/로그아웃, 마이페이지
- Backend/ChatServer : **채팅서버** - 사용자 채팅서비스
- Backend/FileServer : **파일서버** - 파일저장
- Backend/PlatformServer : **플랫폼 서버** - 밴드 방 생성, 글 쓰기

#### - 프론트(Frontend)

- Frontend/src/componets : vue components 위치

#### - 자료

- /doc : 발표자료
- /data : 이미지

#### - 설치 패키지

- /requirements.txt



# Server Architecture

![![server_achitecture]](data/server_achitecture.png)



## 서버 별 소개

 

 

## 개발 환경& 프레임워크

 

## 사용모듈





## 배포 



 

## Contributor

- [이정호](https://github.com/publicejh) : Chat Server, File Server 개발, 해당 서버 vue front 개발, 인프라 구축

- [이지영](https://github.com/jiyoung1202) : Platform Server 개발, 해당 서버 vue front 개발, DB 스키마 설계

- [송이현](https://github.com/Ihyun) : Auth Server 개발, 해당 서버 vue front 개발. 에러코드 정리


## 시연영상
https://youtu.be/KkDzQ6pFlMw
