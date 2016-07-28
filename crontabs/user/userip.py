__author__ = 'wei.jin'

import knowing.models.tblmarkettransactioncompletelog as completelog


class Userip():
    @staticmethod
    def run():
        sql = "select * from %s" % completelog.TblMarketTransactionCompleteLog.table
        model = completelog.TblMarketTransactionCompleteLog()
        print(model.get_result(sql,limit=100))
