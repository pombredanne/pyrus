from abc import abstractmethod, ABCMeta
from multiprocessing import Manager
from multiprocessing.util import ForkAwareThreadLock


def enum(**enums):
    return type('Enum', (), enums)


class MultiProcessBorg():
    __metaclass__ = ABCMeta
    _mutex = ForkAwareThreadLock()

    def __init__(self, *args, **kwds):
        self._mutex.acquire()
        try:
            if not hasattr(type(self), '_shared_state'):
                type(self)._shared_state = {}
            self.__dict__ = self._shared_state
            if not self.is_initialized():
                self._manager = Manager()
                self._initialize(*args, **kwds)
                self.initialized = self._manager.Value(bool, True)
        finally:
            self._mutex.release()

    def is_initialized(self):
        """
        Is the shared state initialized?
        """
        return self.__dict__.get('initialized', False)

    @abstractmethod
    def _initialize(self, *args, **kwds):
        pass
