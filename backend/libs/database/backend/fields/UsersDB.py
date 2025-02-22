from sqlalchemy import String, Integer, Column, LargeBinary, UniqueConstraint, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

class UsersDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'Users'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(LargeBinary(), nullable=False)
    type = Column(String(16), nullable=False)

    isEmailConfirmed = Column(Boolean, nullable=False, default=False)
    isSupplierStatusConfirmed = Column(Boolean, nullable=False, default=False)
    isAdmin = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        '''
            Method, that returns human-readable data about rows
            Returns:
                str: Description of row
        '''
        return f"""<Users(
                        id={self.id},
                        email={self.email},
                        password={self.password},
                        type={self.type},
                        isEmailConfirmed={self.isEmailConfirmed},
                        isSupplierStatusConfirmed={self.isSupplierStatusConfirmed}
                        isAdmin={self.isAdmin}
                    )>
                """