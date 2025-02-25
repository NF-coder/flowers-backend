# FAST FEATURE! MAY HAVE MANY ERRORS!

from sqlalchemy import String, Integer, Column, LargeBinary, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, mapped_column, Mapped

from .UsersDB import UsersDB

# TODO: rewrite using foreign keys and relations!
class OrderProductsDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'OrderProducts'


    id = Column(Integer, nullable=False, unique=True, primary_key=True)

    userId = Column(Integer, nullable=False) # FK

    orderId = Column(Integer, nullable=False) # FK
    productId = Column(Integer, nullable=False) # FK

    def __repr__(self):
        '''
            Method, that returns human-readable data about rows
            Returns:
                str: Description of row
        '''
        return f"""<OrderProducts(
                        id={self.id},
                        userId={self.userId},
                        orderId={self.orderId},
                        productId={self.productId}
                    )>
                """