from decouple import config

API_KEY = config('API_KEY')
print("Using API Key:", API_KEY)
