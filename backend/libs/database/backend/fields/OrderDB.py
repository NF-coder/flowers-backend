# FAST FEATURE! MAY HAVE MANY ERRORS!

from sqlalchemy import String, Integer, Column, LargeBinary, ForeignKey, Boolean, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, mapped_column, Mapped

from datetime import datetime

from .UsersDB import UsersDB

# TODO: rewrite using foreign keys and relations!
class OrderDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'Order'


    id = Column(Integer, nullable=False, unique=True, primary_key=True)

    costumerFirstName = Column(String(64), nullable=False)
    costumerSecondName = Column(String(64), nullable=False)
    comment = Column(String(1024), nullable=False)
    phoneNumber = Column(String(32), nullable=False)

    isFinished = Column(Boolean, nullable=False, default=False)
    isCanceled = Column(Boolean, nullable=False, default=False)

    geoId = Column(Integer, nullable=False) # FK
    userId = Column(Integer, nullable=False) # FK
    productId = Column(Integer, nullable=False) # FK

    orderStatus = Column(String(32), nullable=False, default="Обрабатывается...")
    orderCreatedTime = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        '''
            Method, that returns human-readable data about rows
            Returns:
                str: Description of row
        '''
        return f"""<Order(
                        id={self.id},
                        userId={self.userId},
                        costumerFirstName={self.costumerFirstName},
                        costumerSecondName={self.costumerSecondName},
                        comment={self.comment},
                        phoneNumber={self.phoneNumber},
                        orderStatus={self.orderStatus},
                        isFinished={self.isFinished},
                        isCanceled={self.isCanceled},
                        geoId={self.geoId},
                        orderCreatedTime={self.orderCreatedTime},
                        productId={self.productId}
                    )>
                """