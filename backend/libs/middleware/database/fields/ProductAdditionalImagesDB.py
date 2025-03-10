from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy.ext.declarative import declarative_base

# TODO: rewrite using foreign keys and relations!
class ProductAdditionalImagesDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'ProductAdditionalImages'

    id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, primary_key=True)
    imageUrl:  Mapped[str] = mapped_column(String(1024), nullable=False)

    productId: Mapped[int] = mapped_column(Integer, nullable=False) # FK

    def __repr__(self):
        '''
            Method, that returns human-readable data about rows
            Returns:
                str: Description of row
        '''
        return f"""<ProductAdditionalImages(
                        id={self.id},
                        productId={self.productId},
                        imageUrl={self.imageUrl}
                    )>
                """