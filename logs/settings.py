"""doc."""

logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno}- {message}',
            'style': '{'
        }
    },
    'handlers': {
        'testHandler': {
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'mode': 'w',
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'app_logger': {
            'handlers': ['testHandler'],
            'propagate': False
        }
    },

    # 'filters': {},
    # 'root': {}   # '': {}
    # 'incremental': True
}
