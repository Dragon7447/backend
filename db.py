import sqlite3

# Create database
conn = sqlite3.connect("coupons.db")
c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE IF NOT EXISTS coupons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coupon_text TEXT NOT NULL
)
""")

# Insert some coupons
c.executemany("INSERT INTO coupons (coupon_text) VALUES (?)", [
    ("🎉 You Won 30% Off!",),
    ("🔥 Free Shipping on Your Next Order!",),
    ("💎 ₹100 Cashback Coupon!",),
    ("🎁 Buy 1 Get 1 Free Offer!",)
])

conn.commit()
conn.close()

print("✅ Database initialized with coupons!")
