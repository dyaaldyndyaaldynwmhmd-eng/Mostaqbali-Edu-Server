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
    if username == "admin" and password == "123":
        return jsonify({"success": True, "message": "مرحباً بك في منصة مستقبلي"})
    return jsonify({"success": False, "message": "خطأ في البيانات"})

if __name__ == '__main__':
    app.run()

