
# written by zhaoliyuan
# read data of index values to test all kinds of period identification

import numpy as np
import pandas as pd
from ipdb import set_trace
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlhelper.tableToDataframe import toSQL, toDf
from optparse import OptionParser

Base = declarative_base()

class index_value(Base):
    
    __tablename__  = 'index_value'

    iv_globalid = Column(Integer, primary_key = True)
    iv_general_code = Column(String)
    iv_time = Column(Date)
    iv_value = Column(Float)
    created_at = Column(DateTime)
    updates_at = Column(DateTime)

# 股票指数
class aindexeodprices(Base):
    
    __tablename__  = 'aindexeodprices'

    OBJECT_ID = Column(Integer, primary_key = True)
    S_INFO_WINDCODE = Column(String)
    TRADE_DT = Column(Date)
    S_DQ_CLOSE = Column(Float)

# 债券指数


# 宏观指标



def loadIndexClose(key = 'base', code = '000001', sdate = '2017-01-01' , edate = '2019-10-10'):
#    sql = toSQL(key)
#    sql = sql.query(index_value.iv_value, index_value.iv_time)
#    sql = sql.filter(index_value.iv_general_code == code)
#    sql = sql.filter(index_value.iv_time.between(sdate,edate))
#    sql = sql.statement
#    df = toDf(key, sql, parse_dates = '')
#    df.set_index('iv_time', inplace = True)


    print(df)

if __name__ == '__main__':
     
    loadIndexClose()

