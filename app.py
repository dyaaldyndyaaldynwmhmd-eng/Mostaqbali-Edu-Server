from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Mostaqbali Server is Running!"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username == "mohammed baguira" and password == "m1o2h3a4m5e6d":
        return jsonify({"success": True, "message": "مرحباً بك في منصة مستقبلي"})
    return jsonify({"success": False, "message": "خطأ في البيانات"})

if __name__ == '__main__':
    app.run()

