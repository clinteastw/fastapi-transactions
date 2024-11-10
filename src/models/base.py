from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column



class Base(DeclarativeBase):
    # type_annotation_map = {
    #     dict[str, Any]: JSON
    # }
    
    id: Mapped[int] = mapped_column(primary_key=True)