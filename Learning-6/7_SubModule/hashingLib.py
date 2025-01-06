import hashlib

password = b"sami5671"

hash_OBJ = hashlib.sha256(password)
hashed_password = hash_OBJ.hexdigest()

print(hashed_password)
