import hashlib

data = input("Enter data: ")

hash_value = hashlib.sha256(data.encode()).hexdigest()

print("Original Data:", data)
print("SHA-256 Hash:", hash_value)