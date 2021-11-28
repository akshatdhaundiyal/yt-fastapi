from passlib.context import CryptContext
pwd_context = CryptContext(schemes= ["bcrypt"],deprecated = "auto" )

def hash(password: str):
    return pwd_context.hash(password)

# To compare the 2 password, 1 from attempt and another is hashed password from db
def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)