from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#Criptografando a senha
class AuthUtil:

    def encrypted_password(self, password):
        return pwd_context.hash(password)

    def check_password(self, password, encrypted_password):
        return pwd_context.verify(password, encrypted_password)
