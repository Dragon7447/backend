import sqlite3

# Create database
conn = sqlite3.connect("coupons.db")
c = conn.cursor()

# Create table (supports both text and image types)
c.execute("""
CREATE TABLE IF NOT EXISTS coupons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,           -- 'text' or 'image'
    coupon_text TEXT,
    coupon_image TEXT
)
""")

# Clear old data (optional if re-running)
c.execute("DELETE FROM coupons")

# Insert sample coupons
coupons = [
    ("text", "🎉 You Won 30% Off!", None),
    ("text", "💎 ₹100 Cashback Coupon!", None),
    ("image", None, "https://i.imgur.com/O7MskhH.png"),
    ("image", None, "https://i.imgur.com/4AiXzf8.jpeg")
]

c.executemany("INSERT INTO coupons (type, coupon_text, coupon_image) VALUES (?, ?, ?)", coupons)

conn.commit()
conn.close()
print("✅ Database initialized with text and image coupons!")
