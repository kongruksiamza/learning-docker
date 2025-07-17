## 🐳 Docker Images


## 📦 Docker Containers


## 🗃️ Docker Registry

## 📝 Dockerfile

#### ติดตั้ง Flask
```
pip install flask
```
#### แสดงรายการ Package
```
pip list
```

#### โค้ดประกอบการสอน (app.py)
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "<h1>Hello World<h1>"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)

```

#### รันแอพพลิเคชั่น

```
python app.py
```

#### สร้างไฟล์เก็บรายชื่อ Package
```
pip freeze > requirements.txt
```

#### คำสั่งใน Dockerfile

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
docker build -t my-python-app:0.1 .
```

## 🚪 Port Mapping
```
docker run --rm -p 3000:5000 --name mycontainer my-python-app:0.1
```

## 🚀 Push Images
