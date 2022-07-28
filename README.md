# 2022 Summer Sillicon Valley Internship Program - Team E

| Name    | 김한규  | 박지은  | 백승민   | 신재용  | 유효주  |
| ------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| role    | Leader & AI & Design   | Backend & Design       | DB & AI       | Backend & DB      | Frontend & DB      |
| Github  | [@Hankyu-Kim](https://github.com/Hankyu-Kim) | [@lucykorea414](https://github.com/lucykorea414) | [@Min100KM](https://github.com/Min100KM) | [@Heo sls0263](https://github.com/sls0263) | [@oohyj](https://github.com/oohyj) |

### 프로젝트명: YeZak
프로젝트 한줄 소개: 미대생 예작 판매 웹사이트

## Web

#### Development Stack - Tools

<p align="center"> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.figma.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> </p>

<br>
<br>

#### Architecture
![img](https://github.com/YeZak/.github/blob/edf5261e7602e7f28b05fd65298289e3105d0c9f/profile/image/Architecture.png)

#### FlowChart
![img](https://github.com/YeZak/.github/blob/edf5261e7602e7f28b05fd65298289e3105d0c9f/profile/image/FlowChart.png)

<br>

## Main Functions - Video Tour

- YeZak main page
![1](https://github.com/YeZak/.github/blob/dcbefe2e3bd41187c5a4d0dd3888dc06bbe1e6ac/profile/image/1.gif)
<br>
- Upload artworks of your own!

![2](https://github.com/YeZak/.github/blob/ced20b6291f17c065f04856064056de628fe3c1b/profile/image/2.gif)

<br>

- AI Clip model automatically labels the genres
- Auto generated interior pictures


![3](https://github.com/YeZak/.github/blob/ced20b6291f17c065f04856064056de628fe3c1b/profile/image/3.gif)



## AI

판매자가 미술품을 등록할때 편의성을 위하여/ 구매자에게 인테리어가 적용된 모습을 보여주기 위해서 keyword 기능과 labeling 기능을 추가하였습니다!

#### keyword

![i](https://github.com/YeZak/.github/blob/edf5261e7602e7f28b05fd65298289e3105d0c9f/profile/image/keyword.JPG)

인공지능 CLIP모델을 사용하였으며 데이터셋에 분류된 클래스를 기준으로 이미지를 분석하여 문장으로 나타내는데, 이를 str형식으로 받아 저희는 중요한 단어만 추출하여 해당 글에 #(해쉬태그)를 달아 검색에 용이하게 하였습니다.
![p](https://github.com/YeZak/.github/blob/edf5261e7602e7f28b05fd65298289e3105d0c9f/profile/image/1.png)
![p](https://github.com/YeZak/.github/blob/edf5261e7602e7f28b05fd65298289e3105d0c9f/profile/image/2.png)

#### labeling

등록된 게시글을 보면 해당 아트의 장르 또한 인공지능이 분류하는 모습을 볼 수 있는데요,
![p](https://github.com/YeZak/.github/blob/edf5261e7602e7f28b05fd65298289e3105d0c9f/profile/image/labeling.JPG)
이 뿐만 아니라 미술품의 크기를 예상하게 하기위해 + 그에 맞는 인테리어에 담긴 모습을 보여주어 구매자의 욕구를 불러일으킬뿐만 아니라, 역으로 본인의 인테리어에 맞는 작품인것 또한 확인할 수 있습니다.
![p](https://github.com/YeZak/.github/blob/edf5261e7602e7f28b05fd65298289e3105d0c9f/profile/image/%EC%97%85%EB%A1%9C%EB%93%9C%EB%90%9C%20%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%99%95%EC%9D%B8.JPG]
