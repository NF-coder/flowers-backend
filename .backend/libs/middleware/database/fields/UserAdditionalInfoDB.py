# FAST FEATURE! MAY HAVE MANY ERRORS!

from sqlalchemy import String, Integer, Column, LargeBinary, ForeignKey, Boolean, Text
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import relationship, mapped_column, Mapped

from sqlalchemy.ext.declarative import declarative_base

from ......v2.db_services.Users.database.UsersDB import UsersDB

# TODO: rewrite using foreign keys and relations!
class UserAdditionalInfoDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'UserAdditionalInfo'


    id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, primary_key=True)

    userId: Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="CASCADE"), nullable=False) # FK

    firstName: Mapped[str] = mapped_column(String(128), nullable=True)
    secondName: Mapped[str] = mapped_column(String(128), nullable=True)
    phone: Mapped[str] = mapped_column(String(32), nullable=True)
    birthDate: Mapped[str] = mapped_column(String(8), nullable=True)
    gender: Mapped[str] = mapped_column(String(1), nullable=True)

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