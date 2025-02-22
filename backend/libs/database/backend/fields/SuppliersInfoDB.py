from sqlalchemy import String, Integer, Column, LargeBinary, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

class SuppliersInfoDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'SuppliersInfo'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    companyName = Column(String(256), unique=True)
    products = relationship(
        "Catalog",
        back_populates="author", #
        uselist=False # Tells that it's one-to-one relationship
    )

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