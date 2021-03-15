from logging import getLogger, StreamHandler, Formatter
from sys import stdout


logger = getLogger()
logger.setLevel('DEBUG')

handler = StreamHandler(stdout)
formatter = Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
