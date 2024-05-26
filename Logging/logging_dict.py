# https://betterstack.com/community/guides/logging/python/python-logging-best-practices/
# https://www.mybluelinux.com/python-logging-config-via-dictionary-and-config-file/
# https://makesomecode.me/2019/03/python-log-rotation/
# https://habr.com/ru/companies/otus/articles/590067/

import logging
import logging.config


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':
        {
        'default':
            {
            'format': '[%(levelname)s] %(name)s: %(message)s'
            }
        },
    'handlers':
        {
        'stdout':
            {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
            }
        },
    'loggers':
        {
        '':
            {
            'handlers': ['stdout'],
            'level': 'DEBUG',
            'propagate': True
            }
        }
    }


logging.config.dictConfig(LOGGING)

log = logging.getLogger(__name__)
log.debug('foo')
log.info('bar')
log.warning('baz')
