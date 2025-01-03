import logging


logging.basicConfig(
    level=logging.WARNING,
    filename='test.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

x = 5
y = 0

try:
    z = x / y
    logger.info(f'Successfully divided {x} by {y}')
except ZeroDivisionError:
    logger.error(f'Cannot divide {x} by {y}')
