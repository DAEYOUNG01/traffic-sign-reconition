# YOLOv8를 사용한 Traffic_sign_recognition(교통 표지판 탐지 및 인식)
---


## **CONTENST**


## 공통으로 들어가야 하는 사항 


* **프로젝트 제목** : 프로젝트의 간략한 이름 및 설명

  
* **프로젝트 개요** : 프로젝트에 대한 전반적인 설명(내가 겪은 여려움을 어떻게 해결했는가?)

  
* **필요한 라이브러리 또는 프로젝트 한계점 설명**

  
* **추후 개선 사항** : 추가로 개선해야 하는 사항에 대한 정리 및 한계점 설명
---


## 머신러닝 & 딥러닝 파트


* **데이터 세트** : 데이터셋에 대한 설명 및 출처

  
* **모델 설명** : 사용한 머신러닝 / 딥러닝 모델의 종류 및 선택 이유

  
* **실험 결과** : 모델 평가에 사용된 지표와 결과(표 또는 그래프)
---


## 프로젝트 제목 : Korea_Traffic_Sign_Recognition


자율주행에서 CV를 통한 대표적 기술

자동차에 장착된 카메라가 교통 신호판 정보를 수집하고 신호의 종류와 위치 등을 인식,
 
교통 신호 정보를 파악하며, 교통 상황 등을 경보음과 같은 방식으로 운전자에게 정보를 전달하는

정밀함을 달성하기 위해, 자동차는 도로 표시를 이해하고 적절한 결정을 내려야 함.

이 기술의 중요성을 분석하면서 교통 표지판 분류 프로젝트를 시도한다.
![image](https://github.com/dbeodud147/traffic-sign-reconition/assets/163965664/0642fd32-78f5-4941-963b-b24a9bdd5718)

---
## **프로젝트 개요**


**1. 영상의 교통 표지판 객체 탐지**


![2024-06-11 21 03 04 (1)](https://github.com/dbeodud147/traffic-sign-reconition/assets/163965664/e58f4162-5c3c-4cfb-b5b9-5fb2bf1fb957)
![2024-06-11 21 04 52 (1)](https://github.com/dbeodud147/traffic-sign-reconition/assets/163965664/f1a5681e-5af1-4739-9c6d-b02ea26b4505)

---


**2. 프로젝트를 진행하면서 발견한 다양한 문제점**


* 한국 교통 표지판의 데이터 셋은 생각보다 많이 구하기 어렵고, 데이터 분할이 제대로 진행된 데이터 셋이 없었음.
* 데이터 셋이 그나마 분할이 잘 되어 있다고 판단된 데이터 셋을 구했지만 이조차 Yolo에서 실행 파일로 사용되는 data.yaml 파일에 클래스 오류가 많았음

![image](https://github.com/dbeodud147/traffic-sign-reconition/assets/163965664/1bc056c2-c5ee-4904-941f-d7e3927bab6a)
![image](https://github.com/dbeodud147/traffic-sign-reconition/assets/163965664/00cab5a7-ffab-4722-ad21-4ed745b343ab)



**3. 발견한 문제점에 대한 해결 방법**


## **필요한 라이브러리 또는 프로젝트 한계점 설명**


## **추후 개선 사항**


##  **데이터 세트**


## **모델 설명**


##  **실험 결과**
