from sqlalchemy import String, Integer, ForeignKey

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Mapped, mapped_column

class GeoDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'Geo'


    id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, primary_key=True)

    userId: Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="CASCADE"), nullable=False) # FK

    country: Mapped[int] = mapped_column(String(128), nullable=False)
    city: Mapped[str] = mapped_column(String(128), nullable=False)
    street: Mapped[str] = mapped_column(String(128), nullable=False)
    building: Mapped[str] = mapped_column(String(128), nullable=False)
    flat: Mapped[str] = mapped_column(String(128), nullable=False)

    def __repr__(self):
        '''
            Method, that returns human-readable data about rows
            Returns:
                str: Description of row
        '''
        return f"""<Geo(
                        id={self.id},
                        userId={self.userId},
                        country={self.country},
                        city={self.city},
                        street={self.street},
                        building={self.building},
                        flat={self.flat},
                    )>
                """