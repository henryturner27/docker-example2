from .base import Base
from .manifest import Manifest
from .member_eligibility import MemberEligibility
from config.database import engine


Base.metadata.create_all(engine)
