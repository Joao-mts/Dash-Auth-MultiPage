from datetime import timedelta, datetime, timezone
from passlib.context import CryptContext
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
import json

load_dotenv()

SECRET_KEY = os.getenv('AUTH_SECRET_KEY')
ALGORITHM = os.getenv('AUTH_ALGORITHM')
TOKEN_EXPIRATION_DELTA = int(os.getenv('TOKEN_EXPIRATION_DELTA'))

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {'users': []}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users_data):
    with open(USERS_FILE, 'w') as f:
        json.dump(users_data, f, indent=4)

def create_user(name: str, email: str, password: str) -> bool:
    try:
        users_data = load_users()
        if any(user['email'] == email for user in users_data['users']):
            return False  # Usuário já existe

        new_user = {
            'name': name,
            'email': email,
            'hashed_password': bcrypt_context.hash(password),
            'is_valid': True
        }
        users_data['users'].append(new_user)
        save_users(users_data)
        return True
    except Exception as e:
        return False

def authenticate_user(email: str, password: str) -> dict:
    users_data = load_users()
    user = next((user for user in users_data['users'] if user['email'] == email), None)
    if not user:  # Usuário não encontrado
        return False
    if not user['is_valid']:  # Usuário não validado
        return False
    if not bcrypt_context.verify(password, user['hashed_password']):  # Senha incorreta
        return False
    return user  # Login Ok, retorna usuário

def create_access_token(email: str, name: str) -> str:
    encode = {'sub': email, 'id': name}
    expires = datetime.now(timezone.utc) + timedelta(hours=TOKEN_EXPIRATION_DELTA)
    encode.update({'exp': expires.timestamp()})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def login_for_access_token(email: str, password: str) -> dict:
    user = authenticate_user(email, password)
    if not user:
        return False
    token = create_access_token(user['email'], user['name'])
    
    return {'token_type': 'bearer', 'access_token': token}

def validate_token(token: str) -> dict:
    if not token:
        return False
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        name: str = payload.get('id')
        expiration: float = payload.get('exp')
        if not expiration or not email or not name:
            return False
        current_time = datetime.now(timezone.utc).timestamp()
        if current_time > expiration:
            return False
        return {'email': email, 'name': name}
    except JWTError:
        return False
