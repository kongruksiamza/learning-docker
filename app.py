from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

#setting database
client = MongoClient("mongodb://db:27017")
db = client["mydb"] #database
collection = db["users"] #collection

@app.route('/')
def home():
   return "<h1>ยินดีต้อนรับเข้าสู่เว็บไซต์<h1>"

@app.route('/about')
def about():
   return "<h1>เกี่ยวกับฉัน : นายก้อง 3025<h1>"

@app.route('/data')
def get_data():
    users = collection.find()
    return "<br>".join([f"<h2>ชื่อ : {user['name']} , อายุ {user['age']} ปี </h2><hr>" for user in users])

def init_data():
   if collection.count_documents({}) == 0:
      collection.insert_one({"name": "ก้องรักสยาม", "age": 30})
      print("บันทึกข้อมูลเรียบร้อย")

if __name__ == '__main__':
   init_data() #insert data
   app.run(host="0.0.0.0", port=5000)
