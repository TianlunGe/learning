from sqlalchemy import engine_from_config
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

engine = create_engine('mysql+pymysql://root:root@localhost:3306/finance_data')
# def __init__(self, drivername, username=None, password=None,host=None, port=None, database=None, query=None):

url = URL('mysql','root','root','localhost',3306,'finance_data')
engine = create_engine(url)
