import secrets

token = secrets.token_urlsafe(16)
print("Secure token:", token)
