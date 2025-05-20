import bcrypt

# Hash the password
password = input("Enter your password: ").encode()
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print("Stored hash:", hashed)

# Verification (for demo)
if bcrypt.checkpw(password, hashed):
    print("Password match!")
else:
    print("Incorrect password")
