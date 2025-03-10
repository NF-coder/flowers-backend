from sqlalchemy import String, Integer, Column, LargeBinary, UniqueConstraint, Text, Boolean
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

class UsersDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, primary_key=True)
    email: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(LargeBinary(), nullable=False)
    type: Mapped[str] = mapped_column(String(16), nullable=False)

    isEmailConfirmed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    isSupplierStatusConfirmed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    isAdmin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

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