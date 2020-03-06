import logging

def setup_logger(name):
    formatter = logging.Formatter(fmt='[%(levelname)s][{}] %(asctime)s:%(threadName)s:%(message)s'.format(name), datefmt='%Y-%m-%d %H:%M:%S')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    return logger
