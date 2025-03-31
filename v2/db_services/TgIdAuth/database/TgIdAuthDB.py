from sqlalchemy import String, Integer, Column, LargeBinary, UniqueConstraint, Text, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

class TgIdAuthDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'TgIdAuth'

    tgId: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, primary_key=True)
    userId: Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="CASCADE"), nullable=False, unique=True)

    def __repr__(self):
        '''
            Method, that returns human-readable data about rows
            Returns:
                str: Description of row
        '''
        return f"""<TgIdAuth(
                        tgId={self.tgId},
                        userId={self.userId}
                    )>
                """