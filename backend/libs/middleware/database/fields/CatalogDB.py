from sqlalchemy import String, Integer, Column, LargeBinary, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase

from .UsersDB import UsersDB

from sqlalchemy.orm import Mapped, mapped_column

# TODO: rewrite using foreign keys and relations!
class CatalogDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'Catalog'


    id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, primary_key=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    titleImage: Mapped[str] = mapped_column(String(1024), nullable=False)

    # TODO: refactor it to CompaniesInfo database
    supplierId: Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="CASCADE"), nullable=False) # FK

    # We use only RUB this time.. So it's a problem for future developers)
    cost: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text)

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