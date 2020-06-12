# QRGenPy

## QR코드 생성기 (by Python)

Python을 사용하여 QR코드 생성

 - 코로나 19의 영향으로 여러 시설에서 QR코드를 각 건물 및 호실마다 QR코드를 부착하는 경우가 많이 생김
 - Google에 검색하여 나오는 QR코드 생성기의 경우 UTF8이 지원되지 않거나 수작업이 동반되는 경우가 많음
 - 수작업을 최대한 줄여 QR코드를 jpg파일로 생성하여 모두가 편안
 
## Download

 - [최신 Release](https://github.com/EleutheriusKim/QRGenPy/raw/master/release/1.0.0.zip)
 
## WEB실행

- [웹에서 실행하기](https://gitpod.io/#https://github.com/EleutheriusKim/QRGenPy)
 
## 사용방법

 - 압축 풀기
 - 동일한 경로의 폴더에 QR코드를 생성 할 코드 혹은 문장을 작성 (UTF-8)
 - exe파일 실행
 
## 주의사항

 - 작성된 파일은 \n문자를 기준으로 split됨
 - 특수문자 모두 포함가능 하나, 출력되는 파일명은 일부 특수문자 제거
