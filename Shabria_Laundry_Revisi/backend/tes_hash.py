import bcrypt

# Password yang mau di-hash (harus diubah ke byte pakai awalan 'b')
password = b"admin123"

# Proses hashing murni
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Cetak ke layar sebagai teks biasa biar gampang di-copy
print(hashed.decode('utf-8'))