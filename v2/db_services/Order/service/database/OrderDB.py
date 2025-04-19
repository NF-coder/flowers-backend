from sqlalchemy import String, Integer, ForeignKey, Boolean, DateTime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime,timezone

class OrderDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'Order'


    id = mapped_column(Integer, nullable=False, unique=True, primary_key=True)

    costumerFirstName: Mapped[str] = mapped_column(String(64), nullable=False)
    costumerSecondName: Mapped[str] = mapped_column(String(64), nullable=False)
    comment: Mapped[str] = mapped_column(String(1024), nullable=False)
    phoneNumber: Mapped[str] = mapped_column(String(32), nullable=False)

    isFinished: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    isCanceled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    geoId: Mapped[int] = mapped_column(ForeignKey("Geo.id", ondelete="RESTRICT"), nullable=False) # FK
    userId: Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="RESTRICT"), nullable=False) # FK
    productId: Mapped[int] = mapped_column(ForeignKey("Catalog.id", ondelete="RESTRICT"), nullable=False) # FK

    orderStatus: Mapped[str] = mapped_column(String(32), nullable=False, default="Обрабатывается...")
    orderCreatedTime: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

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