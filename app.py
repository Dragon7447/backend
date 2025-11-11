from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # allows frontend (Netlify / localhost) to call this API

# Function to fetch a random coupon from the database
def get_coupon_from_db():
    conn = sqlite3.connect("coupons.db")
    cursor = conn.cursor()
    cursor.execute("SELECT coupon_text FROM coupons ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    conn.close()

    if row:
        return {"couponText": row[0]}
    else:
        return {"couponText": "😞 No coupons available right now!"}


# API route
@app.route("/api/coupon", methods=["GET"])
def get_coupon():
    return jsonify(get_coupon_from_db())


if __name__ == "__main__":
    # When testing locally:
    app.run(host="0.0.0.0", port=5000, debug=True)
