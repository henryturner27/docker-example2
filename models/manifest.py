from sqlalchemy import Column, Integer, String, Date

from .base import Base


class Manifest(Base):
    __tablename__ = 'manifest'

    ID = Column(Integer, primary_key=True)
    TABLE = Column(String(50), nullable=False)
    LOAD_DATE = Column(Date, nullable=True)
