from sqlalchemy import String, Integer, Column, LargeBinary, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, mapped_column, Mapped

from .UsersDB import UsersDB

# TODO: rewrite using foreign keys and relations!
class CatalogDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'Catalog'


    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    title = Column(String(128), nullable=False)
    titleImage = Column(String(1024), nullable=False)

    # TODO: refactor it to CompaniesInfo database
    supplierId = Column(Integer, nullable=False) # FK

    # We use only RUB this time.. So there's a problem for future developers)
    cost = Column(Integer, nullable=False)
    description = Column(Text)

    def __repr__(self):
        '''
            Method, that returns human-readable data about rows
            Returns:
                str: Description of row
        '''
        return f"""<CatalogDB(
                        id={self.id},
                        supplierId={self.supplierId},
                        title={self.title},
                        titleImage={self.titleImage},
                        cost={self.cost},
                        description={self.description},
                    )>
                """