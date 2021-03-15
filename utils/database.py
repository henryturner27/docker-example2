from contextlib import contextmanager
from sqlalchemy.orm import Session
from csv import DictReader
from datetime import datetime

from models import engine, MemberEligibility, Manifest
from config.logger import logger


@contextmanager
def db_session_handler():
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def set_member_eligibility(filename: str):
    with open(f'data/{filename}') as file:
        psv_reader = DictReader(file, delimiter='|')
        new_records = []
        logger.info(f'loading file: {filename}')
        with db_session_handler() as db_session:
            for row in psv_reader:
                row['ELIGIBILITY_START'] = datetime.strptime(
                    row['ELIGIBILITY_START'], '%Y-%m-%d')
                row['ELIGIBILITY_END'] = datetime.strptime(
                    row['ELIGIBILITY_END'], '%Y-%m-%d') if row['ELIGIBILITY_END'] else None
                new_records.append(MemberEligibility(**row))
            db_session.bulk_save_objects(new_records)


def set_manifest(filename: str):
    with db_session_handler() as db_session:
        file_date = datetime.strptime(filename.split('.')[1], '%Y%m%d')
        logger.info(f'appending to manifest')
        new_record = {
            'TABLE': 'member_eligibility',
            'LOAD_DATE': file_date,
        }
        db_session.add(Manifest(**new_record))
