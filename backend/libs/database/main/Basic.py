from typing import Self

class Basic:
    @classmethod
    async def start_(cls, api: object, base_fields: object, base_url: str) -> Self:
        '''
            Method that starts connection to database
            Args:
                api(`backend.api.BasicAPI` class inheritor):
                    Low-level API of database. Can be found in backemd.api
                base_fields(`declarative_base()` inheritor):
                    Schema of databse. Can be found in backend.fields
                base_url(str):
                    Link to database. Starts with (for example): `postgresql+asyncpg://`
            Returns:
                self:
        '''

        self = cls()
        self.api = await api.start(base_fields, base_url)

        return self