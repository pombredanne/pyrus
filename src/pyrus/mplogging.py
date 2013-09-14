from atexit import register
from multiprocessing import Queue
from logging import getLogger, Formatter, StreamHandler
from logging.handlers import QueueHandler, QueueListener

from pyrus import MultiProcessBorg


DEFAULT_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] [%(name)s] ' +\
    '%(message)s'
ROOTLOGGER = 'pyrus'


class MultiprocessLogManager(MultiProcessBorg):
    """
    A multiprocessing friendly log manager with shared state across processes.
    """
    def __init__(self):
        super(MultiprocessLogManager, self).__init__()

    def _initialize(self):
        self.loggers = {}
        self.queue = Queue(-1)
        self.queue_handler = QueueHandler(self.queue)
        self.handler = StreamHandler()
        self.listener = QueueListener(self.queue, self.handler)
        self.listener.start()
        self.logformat = DEFAULT_FORMAT

    @property
    def logformat(self):
        return self.handler.formatter._fmt

    @logformat.setter
    def logformat(self, fmt):
        self.set_formatter(Formatter(fmt))

    @property
    def loglevel(self):
        return self.handler.level

    @loglevel.setter
    def loglevel(self, level):
        self.handler.setLevel(level)

        for logger in self.loggers.values():
            logger.setLevel(level)

    def set_formatter(self, formatter):
        """
        Set the formatter instance for the manager

        :Parameters:
            `formatter`: The `logging.Formatter` instance to use
        """
        self.handler.setFormatter(formatter)

    def get_logger(self, name=ROOTLOGGER):
        """
        Get a named logger. A new logger is created and added to the shared
        state if none exists, else the existing logger is returned.

        :Parameters:
            `name`: Logger's name. Defaults to `ROOTLOGGER`.
        """
        if name in self.loggers:
            return self.loggers[name]

        logger = getLogger(name)
        logger.addHandler(self.queue_handler)

        self.loggers[name] = logger
        return logger

    def stop(self):
        """
        Stops this instance of the manager
        """
        self.listener.stop()


manager = MultiprocessLogManager()


def get_logger(name=ROOTLOGGER):
    """
    Get a named logger
    """
    return manager.get_logger(name)


def set_format(fmt):
    """
    Set the global log format
    """
    manager.logformat = fmt


def setLevel(level):
    """
    Set the global loging level
    """
    manager.loglevel = level


@register
def stop():
    manager.stop()
