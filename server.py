from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # لتفعيل دعم الـ CORS

@app.route('/')
def home():
    return "مرحباً بك في السيرفر!"

@app.route('/receive_location', methods=['POST'])
def receive_location():
    data = request.get_json()
    print(f"الموقع المستلم: {data}")
    return jsonify({"status": "success", "message": "تم استلام الموقع"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # استخدام المتغير البيئي لتحديد المنفذ
    app.run(host='0.0.0.0', port=port)
