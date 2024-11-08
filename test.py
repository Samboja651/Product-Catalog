import os

DATABASE = "products.db"

ans = os.path.exists(DATABASE)

if ans:
    print("db present")
else:
    print("absent")