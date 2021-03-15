import argparse

from utils.database import set_member_eligibility, set_manifest
from utils.files import validate_filename
from utils.logger import log_execution_time


parser = argparse.ArgumentParser(description='PSV Parser')
parser.add_argument('--filename', required=True,
                    help='The name of the psv file in the /data directory to parse')


@log_execution_time
def run(filename: str):
    is_valid = validate_filename(filename)
    if is_valid:
        set_member_eligibility(filename)
        set_manifest(filename)


if __name__ == '__main__':
    args = vars(parser.parse_args())
    run(args['filename'])
