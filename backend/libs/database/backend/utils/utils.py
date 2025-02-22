class Middleware_utils:
    
    @staticmethod
    def __init__(self): pass

    async def db_answer_to_dict(data: list, table_name: str, column_mode: bool = False) -> list:
        '''
            Implements translation of result of ORM responce to dict
            ### NOTE: describe it later. And also rewrite it
        '''
        # TODO: implement more easier solution from https://stackoverflow.com/questions/1958219/how-to-convert-sqlalchemy-row-object-to-a-python-dict
        
        # old solution
        #return list(
        #            map(
        #                lambda x: {k: v for k, v in x._mapping[table_name].__dict__.items() if k != "_sa_instance_state" and v != None},
        #                data
        #            )
        #        )

        if column_mode:
            expression = lambda x: x._mapping
        else:
            expression = lambda x: {k: v for k, v in x._mapping[table_name].__dict__.items() if k[0] != "_"}

        return list(
                    map(
                        expression,
                        data
                    )
                )