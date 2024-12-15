import logging


logging.basicConfig(
    level=logging.WARNING,
    filename='test.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


x = 5
y = 2

try:
    z = x / y
    logging.info(f'Successfully divided {x} by {y}')
except ZeroDivisionError:
    logging.error(f'Cannot divide {x} by {y}')
