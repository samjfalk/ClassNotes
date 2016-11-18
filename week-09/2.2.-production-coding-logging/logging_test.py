import logging
logging.basicConfig(filename='logging_test.log', level= logging.DEBUG)
log = logging.getLogger(__name__)

log.debug('very granular')
log.info('simple update')
log.warning("you've seen these many times")
log.error('log error message')
log.critical('S*** F***')
