<div id="badges" align="center">

  <div id="header" align="center">
    <img src="https://skillicons.dev/icons?i=docker" width="200"/>
    <h1>โค้ดประกอบการสอน Docker เบื้องต้น</h1>
  </div>

  <a href="https://www.facebook.com/KongRuksiamTutorial" target="_blank">
    <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white"/>
  </a>
    <a href="https://www.udemy.com/user/kong-ruksiam/" target="_blank">
    <img src="https://img.shields.io/badge/Udemy-A435F0?style=for-the-badge&logo=Udemy&logoColor=white"/>
  </a>
    <a href="https://www.youtube.com/@KongRuksiamOfficial/store" target="_blank">
    <img src="https://img.shields.io/badge/Shopee-EE4D2D?style=for-the-badge&logo=Shopee&logoColor=white"/>
  </a>
  <a href="https://medium.com/@kongruksiam" target="_blank">
    <img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white"/>
  </a>
  <a href="https://codepen.io/kongruksiamstudio" target="_blank">
    <img src="https://img.shields.io/badge/Codepen-000000?style=for-the-badge&logo=codepen&logoColor=white"/>
  </a>
  <a href="https://www.tiktok.com/@kongruksiamstudio" target="_blank">
    <img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white"/>
  </a>
  <br>
  <a href="https://github.com/kongruksiamza">
    <img src="https://komarev.com/ghpvc/?username=kongruksiamza&style=flat-square&color=blue" alt="kongruksiamza"/>
  </a>
</div>

## 💻 Flask Application

#### ติดตั้ง Python 
- ดาวน์โหลด : https://python.org/

#### ติดตั้ง Flask
```
pip install flask
```
#### แสดงรายการ Package
```
pip list
```

#### โค้ดประกอบการสอน app.py (Flask)
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "<h1>Hello Application<h1>"

if __name__ == '__main__':
   app.run(host="localhost", port=5000)

```

#### รันแอพพลิเคชั่น

```
python app.py
```


## 📝 Dockerfile

#### สร้างไฟล์เก็บรายชื่อ Package
```
pip freeze > requirements.txt
```

## คำสั่งใน Dockerfile
```
FROM python:3.13
WORKDIR /kongruksiam/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

#### Build Image

```
docker build -t <image-name:tag> .
```

## 🚪 Port Mapping
```
docker run --rm -p 3000:5000 --name mycontainer my-python-app:0.1
```

## 🗄️ MongoDB 

## 🛠️ Docker Compose

## 📚 หลักสูตรที่เกี่ยวข้อง (ภาษาไทย)
- [Docker](#)
- [Python & Flask Framework](https://www.youtube.com/playlist?list=PLltVQYLz1BMBe14u-5pxxEsbJSbdxd1Vs)
- [MongoDB](https://www.youtube.com/playlist?list=PLltVQYLz1BMDcG4oMP-hB3VCmIWVXF-fX)
- [Visual Studio Code](https://www.youtube.com/playlist?list=PLltVQYLz1BMDyQX1B6IccCOeO3TTIsZmp)
