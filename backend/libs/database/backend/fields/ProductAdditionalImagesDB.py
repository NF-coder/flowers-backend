from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

# TODO: rewrite using foreign keys and relations!
class ProductAdditionalImagesDB(declarative_base()):
    # Self-documentated code
    
    __tablename__ = 'ProductAdditionalImages'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    imageUrl = Column(String(1024), nullable=False)

    productId = Column(Integer, nullable=False) # FK

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