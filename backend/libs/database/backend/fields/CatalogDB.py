from sqlalchemy import String, Integer, Column, LargeBinary, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, mapped_column, Mapped

class CatalogDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'Catalog'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    title = Column(String(128), nullable=False)
    titleImage = Column(String(1024), nullable=False)

    supplierId = Column(Integer, ForeignKey("SuppliersInfo.id"))
    author = relationship(
        "SuppliersInfo",
        back_populates="productItem", #
        uselist=False # Tells that it's one-to-one relationship
    )

    additionalImages = relationship("ProductAdditionalImages", back_populates="productItem")
    
    # We use only RUB this time.. So there's a problem for future developers)
    cost = Column(Integer, nullable=False)
    description = Column(Text)

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