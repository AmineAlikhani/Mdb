from abc import ABC, abstractmethod
import pyodbc


def fetch_useragent():
    server = '172.20.20.200,1433'
    database = 'domains'
    username = 'sa'
    password = 'Salam1Salam2'
    connection = 'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
    conn = pyodbc.connect(connection)
    curs = conn.cursor()
#sql = " SELECT [id] ,[rndkey]  FROM [dbo].[rndkeymaker] where [grade]='easy' "
    sql = "SELECT useragent from agents"
    curs.execute(sql)
    rows = curs.fetchall()
    return rows
#loginUsers = curs.execute("select top(200) rkey,userid,ownerid, dmn_id from userslog where status=3 and active=1 order by id desc")


'''
class DB(ABC):
    @abstractmethod
    def _get_x(self):
        ...
    @abstractmethod
    def _set_x(self, val):
        ...
    x = property(_get_x, _set_x)

    @property
    @abstractmethod
    def keys(self):
        pass
    @keys.setter
    @abstractmethod
    def key(self, val):
        pass
    @classmethod
    @abstractmethod
    def create_array(cls):
        pass
'''

def mongo_connction():
    import pymongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Manzoomeh"]
    return db
#    "select top (100) * from useragents"


class Db():
    def generate_db(adress):
        import glob
        import json
        from datetime import datetime

        db_list = list()

        date = datetime.now().strftime("%Y_%m_%d-%I_%p")
        daily_log = open(f"daily_log_{date}.log", "a")

        for log_file in glob.glob(str(adress)):
            f = open(log_file, "r")
            print("Reading a new file..")
            for line in f:
                try:
                    new_line = json.loads(line)
                except:
                    line = line.strip()
                    new_line = json.loads(line[3:])
                new_data_dic = {
                "owner_id": new_line["owner_id"],
                "domain_id": new_line["domain_id"],
                "url": new_line["data"]["url"],
                "user_agent_id": new_line["data"]["user_agent_id"],
                "status_code": new_line["data"]["status_code"],
                "ip": new_line["data"]["ip"],
                "request_time": new_line["data"]["request_time"],
                }
                daily_log.write(f"{new_data_dic} \n")
                db_list.append(new_data_dic)
            print(f"Entered new log")
        print("New daily log added")
        return db_list
    def clean_url():
        for i in db_list:
            url = i["url"]
            import re
            ndurl = re.split("/", url, 1)
            ndurl = str(ndurl[1])
            i["ndurl"] = ndurl
        print(db_list)
        return db_list

    def add_useragent(self):
        useragent_info = fetch_useragent() 
        for i in db_list:
            useragent_info.find
            if i["user_agent_id"] == useragent_info["id"]:
                pass                
        

if __name__ == "__main__":        
    db = mongo_connction()
    collection = db["logs"]
    db_list = Db.generate_db('Files/**/Domain Log/**/*.log')
    Db.clean_url()
    collection.insert_many(db_list)
    print("Data is in mongo server now!")
    fetch_useragent()
