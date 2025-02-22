from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class ProductAdditionalImagesDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'ProductAdditionalImages'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    imageUrl = Column(String(1024), nullable=False)

    productId = Column(Integer, ForeignKey("Catalog.id"))

    def __repr__(self):
        '''
            Method, that returns human-readable data about rows
            Returns:
                str: Description of row
        '''
        return f"""<ProductAdditionalImages(
                        id={self.id},
                        imageUrl={self.imageUrl},
                        productId={self.productId},
                        productItem={self.productItem}
                    )>
                """