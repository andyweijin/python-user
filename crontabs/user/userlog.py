
import knowing.models.tblconnectlog as tblconnectlog

class Userlog():


    @staticmethod
    def run():
        sql = "select * from %s" % tblconnectlog.TblConnectLog.table
        model = tblconnectlog.TblConnectLog()
        print(model.get_result(sql,limit=100))


