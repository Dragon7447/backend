from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import random

app = Flask(__name__)
CORS(app)

def get_coupon_from_db():
    conn = sqlite3.connect("coupons.db")
    cursor = conn.cursor()
    cursor.execute("SELECT type, coupon_text, coupon_image FROM coupons ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"type": "text", "couponText": "😞 No coupons available right now!"}

    coupon_type, coupon_text, coupon_image = row

    if coupon_type == "image" and coupon_image:
        return {"type": "image", "couponImage": coupon_image}
    else:
        return {"type": "text", "couponText": coupon_text or "🎉 You got a reward!"}

@app.route("/api/coupon", methods=["GET"])
def get_coupon():
    return jsonify(get_coupon_from_db())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
