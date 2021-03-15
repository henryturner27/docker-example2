from main import run
from datetime import datetime

from utils.database import db_session_handler
from models import MemberEligibility, Manifest


def test_records_loaded(client):
    run('member_eligibility.20200101.psv')
    with db_session_handler() as db_session:
        records = db_session.query(MemberEligibility).all()
        assert len(records) == 4
        manifest = db_session.query(Manifest).all()
        assert len(manifest) == 1
        manifest = manifest[0]
        assert manifest.TABLE == 'member_eligibility'
        assert manifest.LOAD_DATE == datetime.strptime(
            '2020-01-01', '%Y-%m-%d').date()


def test_no_load_bad_filename(client):
    run('member_eligibility.psv')
    with db_session_handler() as db_session:
        records = db_session.query(MemberEligibility).all()
        assert len(records) == 0
        manifest = db_session.query(Manifest).all()
        assert len(manifest) == 0


def test_no_load_bad_file_type(client):
    run('member_eligibility.20200101.csv')
    with db_session_handler() as db_session:
        records = db_session.query(MemberEligibility).all()
        assert len(records) == 0
        manifest = db_session.query(Manifest).all()
        assert len(manifest) == 0


def test_no_load_bad_date(client):
    run('member_eligibility.202.psv')
    with db_session_handler() as db_session:
        records = db_session.query(MemberEligibility).all()
        assert len(records) == 0
        manifest = db_session.query(Manifest).all()
        assert len(manifest) == 0


def test_no_load_bad_tablenmae(client):
    run('member_eligibilit.20200101.psv')
    with db_session_handler() as db_session:
        records = db_session.query(MemberEligibility).all()
        assert len(records) == 0
        manifest = db_session.query(Manifest).all()
        assert len(manifest) == 0
