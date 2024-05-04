import motor.motor_asyncio
from decouple import config

from src.core.util.ConverterUtil import ConverterUtil
from src.user.UserModel import UserModel

#Conexão com MongoDB
MONGO_URL = config('DATABASEMONGODB_URL')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client.tinderMentoria

user_collection = database.get_collection("user")

converterUtil = ConverterUtil()


class UserRepository:
    async def create_user(self, user: UserModel) -> UserModel:
        user_dict = {
            "name": user.name,
            "lastName": user.lastName,
            "email": user.email,
            "cep": user.cep,
            "password": user.password,
            "position": user.position,
            "skills": user.skills,
            "photo": user.photo
        }

        create_user = await user_collection.insert_one(user_dict)

        new_user = await user_collection.find_one({"_id": create_user.inserted_id})

        return converterUtil.user_converter(new_user)

    async def search_for_user_by_email(self, email: str) -> UserModel:
        user = await user_collection.find_one({"email": email})

        if user:
            return converterUtil.user_converter(user)