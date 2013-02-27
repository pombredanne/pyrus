from pyrus.mplogging import Logger, DEBUG
from multiprocessing import Manager

logger = Logger('TEST', DEBUG)
logger.info('Starting')

def test(i):
	logger.debug('Test: ' + str(i))

manager = Manager()

if __name__ == '__main__':
	pool = manager.Pool(4)
	nums = [ i for i in range(10)]
	pool.map_async(test, nums)
	pool.close()
	pool.join()
