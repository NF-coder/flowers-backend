from .schemas.AuthModels import *

class AuthCommands():
    def __init__(self, client) -> None:
        self.add_auth_by_email__ = client.configure_command(
            functionName="add_auth_method",
            className="EmailAuth"
        )
        self.check_password_by_email__ = client.configure_command(
            functionName="check_password",
            className="EmailAuth"
        )
    
    async def add_auth_by_email(self, email: str, password: str, userId: int) -> None:
        await self.add_auth_by_email__(
            email=email,
            password=password,
            userId=userId
        )
    
    async def check_password_by_email(self, email: str, password: str) -> CheckPasswordResponce:
        return CheckPasswordResponce.model_validate(
            await self.check_password_by_email__(
                email=email,
                password=password
            ),
            from_attributes=True
        )