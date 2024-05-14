import motor.motor_asyncio
from bson import ObjectId
from decouple import config

from src.core.util.AuthUtil import AuthUtil
from src.core.util.ConverterUtil import ConverterUtil
from src.user.UserDTO import RegisterDTO
from src.user.UserModel import UserModel

#Conexão com MongoDB
MONGO_URL = config('DATABASEMONGODB_URL')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client.tinderMentoria

user_collection = database.get_collection("user")

converterUtil = ConverterUtil()
authUtil = AuthUtil()


class UserRepository:
    async def create_user(self, user: RegisterDTO, url_photo: str) -> UserModel:
        user.password = authUtil.encrypted_password(user.password)  #Criptografando a senha

        user_dict = {
            "name": user.name,
            "lastName": user.lastName,
            "email": user.email,
            "cep": user.cep,
            "password": user.password,
            "position": user.position,
            "skills": user.skills,
            "interests": user.interests,
            "photo": url_photo
        }

        create_user = await user_collection.insert_one(user_dict)

        new_user = await user_collection.find_one({"_id": create_user.inserted_id})

        return converterUtil.user_converter(new_user)

    async def search_for_user_by_email(self, email: str) -> UserModel:
        user = await user_collection.find_one({"email": email})

        if user:
            return converterUtil.user_converter(user)

    async def search_for_user_by_id(self, id: str) -> UserModel:
        user = await user_collection.find_one({"_id": ObjectId(id)})

        if user:
            return converterUtil.user_converter(user)

    async def update_user(self, id: str, user_data: dict) -> UserModel:
        if 'password' in user_data:
            user_data['password'] = authUtil.encrypted_password(user_data['password'])

        user = await user_collection.find_one({'_id': ObjectId(id)})

        if user:
            await user_collection.update_one({'_id': ObjectId(id)}, {'$set': user_data})

            finded_user = await user_collection.find_one({'_id': ObjectId(id)})

            return converterUtil.user_converter(finded_user)
