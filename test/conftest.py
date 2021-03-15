import pytest
from os import remove

from utils.database import db_session_handler
from models import MemberEligibility, Manifest


@pytest.fixture(scope='session', autouse=True)
def setup():
    yield
    remove('test.db')


@pytest.fixture(scope='function')
def client():
    with db_session_handler() as db_session:
        db_session.query(Manifest).delete()
        db_session.query(MemberEligibility).delete()
    return
