from datetime import datetime
from os import listdir

from utils.database import db_session_handler
from models import Manifest
from config.logger import logger


def validate_filename(filename: str) -> bool:
    parsed_name = filename.split('.')
    if len(parsed_name) != 3:
        logger.warning('Make sure that you have 3 parts to your filename')
        return False
    try:
        file_date = datetime.date(
            datetime.strptime(parsed_name[1], '%Y%m%d'))
    except ValueError:
        logger.warning(
            'Check that the date in the filename is formatted correctly: yyyymmdd')
        return False
    if parsed_name[0] != 'member_eligibility':
        logger.warning(
            'Check that the tablename in the filename is correct: member_eligibility')
        return False
    if parsed_name[2] != 'psv':
        logger.warning('Check that the file type is psv')
        return False
    if filename not in listdir('./data'):
        logger.warning('Check that the file exists in the data directory')
        return False
    with db_session_handler() as db_session:
        existing_record = db_session.query(Manifest)\
            .filter(Manifest.TABLE == 'member_eligibility')\
            .filter(Manifest.LOAD_DATE == file_date)\
            .first()
    if existing_record:
        logger.warning(f'file {filename} has already been loaded')
        return False
    else:
        return True
