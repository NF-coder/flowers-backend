# FAST FEATURE! MAY HAVE MANY ERRORS!

from sqlalchemy import String, Integer, Column, LargeBinary, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, mapped_column, Mapped

from .UsersDB import UsersDB

# TODO: rewrite using foreign keys and relations!
class UserAdditionalInfoDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'UserAdditionalInfo'


    id = Column(Integer, nullable=False, unique=True, primary_key=True)

    userId = Column(Integer, nullable=False) # FK

    firstName = Column(String(128), nullable=True)
    secondName = Column(String(128), nullable=True)
    phone = Column(String(32), nullable=True)
    birthDate = Column(String(8), nullable=True)
    gender = Column(String(1), nullable=True)

    def __repr__(self):
        '''
            Method, that returns human-readable data about rows
            Returns:
                str: Description of row
        '''
        return f"""<UserAdditionalInfo(
                        id={self.id},
                        userId={self.userId},
                        firstName={self.firstName},
                        secondName={self.secondName},
                        phone={self.phone},
                        birthDate={self.birthDate},
                        gender={self.gender}
                    )>
                """