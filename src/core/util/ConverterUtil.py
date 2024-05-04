from src.user.UserModel import NewUserModel


class ConverterUtil:
    def user_converter(self, user):
        return NewUserModel(
            id=str(user["_id"]),
            name=user["name"],
            lastName=user["lastName"],
            email=user["email"],
            cep=user["cep"],
            password=user["password"],
            position=user["position"],
            skills=user["skills"],
            photo=user["photo"] if "foto" in user else "",
        )
