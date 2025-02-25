# FAST FEATURE! MAY HAVE MANY ERRORS!

from sqlalchemy import String, Integer, Column, LargeBinary, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, mapped_column, Mapped

from .UsersDB import UsersDB

# TODO: rewrite using foreign keys and relations!
class GeoDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'Geo'


    id = Column(Integer, nullable=False, unique=True, primary_key=True)

    userId = Column(Integer, nullable=False) # FK

    country = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    street = Column(String(128), nullable=False)
    building = Column(String(128), nullable=False)
    flat = Column(String(128), nullable=False)

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