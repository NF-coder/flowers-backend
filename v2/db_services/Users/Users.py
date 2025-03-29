import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import DBSettings

from database.UsersAPI import UsersAPI
from database.UsersDB import UsersDB

from schemas.UsersSchemas import *
from schemas.RPCSchemas import *

from simple_rpc import GrpcServer

app = GrpcServer()

class Users():
    def __init__(self) -> None:
        '''
            Method that starts connection to database
            Returns:
                `Users` object
        '''
        self.UsersAPI = UsersAPI(UsersDB, DBSettings.DATABASE_URL)
    
    @app.grpc_method()
    async def add_new_user(self, request: AddNewUserRequest) -> UserIdModel:
        return UserIdModel(
            userId=await self.UsersAPI.add_new_user(
                type=request.type
            )
        )

    @app.grpc_method()
    async def is_id_registered(self, request: UserIdModel) -> IsIdRegistredRes:
        '''
            Method that checks if id is in database
            Args:
                id(int): id
            Returns:
                bool: True if already in database
        '''

        return IsIdRegistredRes(
            state=(await self.UsersAPI.get_by_id(request.userId)) == 1
        )
    
    @app.grpc_method()
    async def get_info_by_id(self, request: UserIdModel) -> UserDTO:
        '''
            Method that gets user info from database.
            Args:
                id(int): user's id
            Returns:
                schemas.UserInfoSchema:
            Raises:
                NotExist: if no users with specified id
        '''

        userInfo = await self.UsersAPI.get_by_id(request.userId)

        if userInfo == 0:
            raise NotExist(description = "User does not exist")

        return await UserDTO.parse(userInfo[0])

    '''
    async def check_password_by_email(self, email: str, password: str) -> bool:
        
            Method that gets user from database by email.
            Args:
                email(str): user's email (in our case)
            Returns:
                NoneType:
            Raises:
                NotExist: if no users with specified email
        

        if not (await self.is_email_registered(email)):
            raise NotExist(
                description="User does not exist"
            )
        return bcrypt.checkpw(
            password.encode(),
            (await self.UsersAPI.get_by_email(email))[0]["password"]
        )
    '''
    
    @app.grpc_method()
    async def confirm_user(self, request: UserIdModel) -> EmptyModel:
        '''
            Method that sets user's email confirmation status to True
            Args:
                id(int): User's id
            Returns:
                NoneType:
        '''

        await self.UsersAPI.set_email_confirmation_status_by_id(
            id=request.userId,
            status=True
        )
        return EmptyModel()
    
    @app.grpc_method()
    async def delete_user_by_id(self, request: UserIdModel) -> EmptyModel:
        '''
            ## CAN CAUSE SECURITY INCIDENTS! USE CAREFULLY!
            Method that deletes user with specified id
            Args:
                id(int): User's id
            Returns:
                NoneType:
        '''
        await self.UsersAPI.delete_by_id(
            id=request.userId
        )
        return EmptyModel()
    
    @app.grpc_method()
    async def find_unconfirmed_suppliers(
            self,
            request: FindUnconfirmedSuppliers
        ) -> UserDTOArray:
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

        if request.sort == "time_descending":
            result = await self.UsersAPI.find_suppliers_with_status_descending(
                start = request.start,
                count = request.count,
                confrmationStatus=False
            )
        elif request.sort == "time_upscending":
            result = await self.UsersAPI.find_suppliers_with_status_upscending(
                start = request.start,
                count = request.count,
                confrmationStatus=False
            )
        else:
            raise Developing(description="Sorry, I not implemented some filters")
        print(result)
        return await UserDTOArray.parse([
            await UserDTO.parse(userInfo)
            for userInfo in result
        ])
    
    '''
    async def make_admin_by_email(self, email: str) -> None:
            Method that makes user admin
            Args:
                email(str): User's email
            Returns:
                NoneType:
        
        await self.UsersAPI.set_admin_status_by_email(
            email=email,
            status=True
        )
    '''
    
    @app.grpc_method()
    async def confirm_supplier_by_id(self, request: UserIdModel) -> EmptyModel:
        '''
            Method that implements supplier confirmation.
            Args:
                id(int): User's id
            Returns:
                NoneType:
        '''
        
        await self.UsersAPI.set_supplier_status_by_id(
            id=request.userId,
            status=True
        )

        return EmptyModel()

# SimpleRPC server startup

app.configure_service(
    cls=Users(),
    port=50501
)
app.run()
