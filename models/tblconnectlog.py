__author__ = 'wei.jin'


from knowing.models.connect import Connect

class TblConnectLog(Connect):

    table = 'tbl_ConnectLog'
    limit = 1000

    def __init__(self):
        super().__init__()


    def get_result(self,sql,**kwargs):
        return [x for x in self.get_rows(sql,**kwargs)]



