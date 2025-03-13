import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from ..database.api.UsersAPI import UsersAPI
from ..database.fields.UsersDB import UsersDB

from .schemas.UsersSchemas import *

class Users():
    def __init__(self) -> Self:
        '''
            Method that starts connection to database
            Returns:
                `Users` object
        '''
        self.UsersAPI = UsersAPI(UsersDB, SecurityConfig.DATABASE_URL)
    
    async def is_email_registered(self, email: str) -> bool:
        '''
            Method that checks if login is in database
            Args:
                login(str): login (email in our case)
            Returns:
                bool: True if already in database
        '''

        return len(await self.UsersAPI.get_by_email(email)) == 1
    
    async def is_id_registered(self, id: int) -> bool:
        '''
            Method that checks if id is in database
            Args:
                id(int): id
            Returns:
                bool: True if already in database
        '''

        return len(await self.UsersAPI.get_by_id(id)) == 1
    

    async def get_info_by_email(self, email: str) -> UserDTO:
        '''
            Method that gets user from database.
            Args:
                email(str): user's email (in our case)
            Returns:
                schemas.UserInfoSchema:
            Raises:
                NotExist: if no users with specified email
        '''
        
        if not (await self.is_email_registered(email)):
            raise NotExist(description = "User does not exist")
        
        userInfo = await self.UsersAPI.get_by_email(email)
        
        return UserDTO(
            id=userInfo.id,
            email=userInfo.email,
            type=userInfo.type,
            isEmailConfirmed=userInfo.isEmailConfirmed,
            isSupplierStatusConfirmed=userInfo.isSupplierStatusConfirmed,
            isAdmin=userInfo.isAdmin
        )
    
    async def get_info_by_id(self, id: int) -> UserDTO:
        '''
            Method that gets user info from database.
            Args:
                id(int): user's id
            Returns:
                schemas.UserInfoSchema:
            Raises:
                NotExist: if no users with specified id
        '''

        if not (await self.is_id_registered(id)):
            raise NotExist(description = "User does not exist")
        
        userInfo = await self.UsersAPI.get_by_id(id)

        return await UserDTO.parse(userInfo)

    async def check_password_by_email(self, email: str, password: str) -> bool:
        '''
            Method that gets user from database by email.
            Args:
                email(str): user's email (in our case)
            Returns:
                NoneType:
            Raises:
                NotExist: if no users with specified email
        '''

        if not (await self.is_email_registered(email)):
            raise NotExist(
                description="User does not exist"
            )
        return bcrypt.checkpw(
            password.encode(),
            (await self.UsersAPI.get_by_email(email))[0]["password"]
        )
    
    async def confirm_email(self, id: int) -> None:
        '''
            Method that sets user's email confirmation status to True
            Args:
                id(int): User's id
                status(bool?): New email confirmation status. Default `True`
            Returns:
                NoneType:
        '''

        await self.UsersAPI.set_email_confirmation_status_by_id(
            id=id,
            status=True
        )
    
    async def delete_user_by_id(self, id: int) -> None:
        '''
            ## CAN CAUSE SECURITY INCIDENTS! USE CAREFULLY!
            Method that deletes user with specified id
            Args:
                id(int): User's id
            Returns:
                NoneType:
        '''
        await self.UsersAPI.delete_by_id(
            id=id
        )
    
    async def delete_user_by_email(self, email: str) -> None:
        '''
            ## CAN CAUSE SECURITY INCIDENTS! USE CAREFULLY!
            Method that deletes user with specified id
            Args:
                email(str): User's email
            Returns:
                NoneType:
        '''
        await self.UsersAPI.delete_by_email(
            email=email
        )
    
    async def find_unconfirmed_suppliers(
            self,
            start: int,
            count: int,
            sort: str
        ) -> List[UserDTO]:
        '''
            Method that deletes user with specified id
            Args:
                count (int):
                    How many users may database find.
                    Number of returned users be smaller, then specified lenght
                start (int):
                    Offset of firs user in list. Can affect result array lenght
                sort(str):
                    Sort type. Available values: `time_upscending` `time_descending`
            Returns:
                NoneType:
        '''

        if sort == "time_descending":
            result = await self.UsersAPI.find_suppliers_with_status_descending(
                start = start,
                count = count,
                confrmationStatus=False
            )
        elif sort == "time_upscending":
            result = await self.UsersAPI.find_suppliers_with_status_upscending(
                start = start,
                count = count,
                confrmationStatus=False
            )
        else:
            raise Developing(description="Sorry, I not implemented some filters")
    
        return [
            await UserDTO.parse(userInfo)
            for userInfo in result
        ]
    
    async def make_admin_by_email(self, email: str) -> None:
        '''
            Method that makes user admin
            Args:
                email(str): User's email
            Returns:
                NoneType:
        '''
        
        await self.UsersAPI.set_admin_status_by_email(
            email=email,
            status=True
        )
    
    async def confirm_supplier(self, email: str = None, id: int = None) -> None:
        '''
            Method that implements supplier confirmation.
            `email` or `id` must be specified.
            If specified both function prefer `email`
            Args:
                email(str?): User's email
                id(int?): User's id
            Returns:
                NoneType:
        '''
        
        if email is not None:
            await self.UsersAPI.set_supplier_status_by_email(
                email=email,
                status=True
            )
            return
        elif id is not None:
            await self.UsersAPI.set_supplier_status_by_id(
                id=id,
                status=True
            )
            return
        
        raise NotEnoudhArguments("email or id must be specified")
