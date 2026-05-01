import getpass
import hashlib
import os

def biometric_auth(prompt, password):
    # Biometrik tasdiqlash uchun foydalanuvchi so'rovi
    response = getpass.getpass(prompt)

    # Foydalanuvchi kiritgan so'zni hash qilish
    user_hash = hashlib.sha256(response.encode()).hexdigest()

    # Foydalanuvchi parolini hash qilish
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Foydalanuvchi parolini saqlash uchun fayl yaratish
    if not os.path.exists('password.txt'):
        with open('password.txt', 'w') as f:
            f.write(password_hash)

    # Foydalanuvchi so'zini saqlash uchun fayl yaratish
    if not os.path.exists('response.txt'):
        with open('response.txt', 'w') as f:
            f.write(user_hash)

    # Foydalanuvchi so'zini hash qilish va saqlangan hash bilan solishtirish
    with open('response.txt', 'r') as f:
        stored_hash = f.read()

    # Foydalanuvchi parolini hash qilish va saqlangan hash bilan solishtirish
    with open('password.txt', 'r') as f:
        stored_password_hash = f.read()

    # Foydalanuvchi so'zini hash qilish va saqlangan hash bilan solishtirish
    if user_hash == stored_hash:
        return True
    else:
        return False

# Sensitive action uchun biometrik tasdiqlash
password = "sensitive_action_password"
if biometric_auth("Enter biometric code: ", password):
    print("Tasdiqlangan!")
else:
    print("Tasdiqlanmagan!")
