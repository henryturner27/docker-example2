from sqlalchemy import Column, Integer, String, Date

from .base import Base


class MemberEligibility(Base):
    __tablename__ = 'member_eligibility'

    ID = Column(Integer, primary_key=True)
    MEMBER_ID = Column(String(10), nullable=False)
    FIRST_NAME = Column(String(50), nullable=False)
    LAST_NAME = Column(String(50), nullable=False)
    ELIGIBILITY_START = Column(Date, nullable=False)
    ELIGIBILITY_END = Column(Date, nullable=True)
