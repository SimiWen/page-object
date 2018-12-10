import unittest
import datetime
from testcase import test_baidu
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_baidu))

    now = datetime.datetime.now().strftime('%Y-%m-%d')
    bp = BeautifulReport(suite)
    bp.report(filename=f'{now}-测试报告', description='测试报告', log_path='testreport')