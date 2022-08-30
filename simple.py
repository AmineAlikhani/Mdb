#import os
#from . import mongo_conenction
import pymongo
import json
import glob 
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

import re
url = "www.w3schools.com/python/python_regex.asp#split"
new = re.split("/", url, 1)
print (type(new[1]))



# Connect to mongodb server
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Manzoomeh"]
col = db["logs"]
#! col.insert_many()
"select top (100) * from useragents"

# Get log files, Generate periodic data base
date = datetime.now().strftime("%Y_%m_%d-%I_%p")
data_list = list()
daily_log = open(f"daily_log_{date}.log", "a")



df = {
  "owner_id": [],
  "domain_id": [],
  "url": [],
  "user_agent_id": [],
  "status_code": [],
  "ip": [],
  "request_time":[],
}

for log_file in glob.glob('Files/**/Domain Log/**/*.log'):
  f = open(log_file,"r")
  print("Start new file")
  for line in f:
    try:
      new_line = json.loads(line)
    except:
      line = line.strip()
      new_line = json.loads(line[3:])
      print(f"new line fixed")  
    #data_list.append(new_line)
    print(f"Added a line")
    df["owner_id"].append(new_line["owner_id"])
    df["domain_id"].append(new_line["domain_id"])
    df["url"].append(new_line["data"]["url"])
    df["user_agent_id"].append(new_line["data"]["user_agent_id"])
    df["status_code"].append(new_line["data"]["status_code"])
    df["ip"].append(new_line["data"]["ip"])
    df["request_time"].append(new_line["data"]["request_time"])
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
    data_list.append(new_data_dic)

#daily_log.write(json.dumps(data_list))
print (type(new_data_dic))
print(type(db))
col.insert_many(data_list)
#df = pd.DataFrame(df)
#df.plot(kind='scatter', x='owner_id' , y='request_time')
#plt.plot(df["ip"], df["request_time"])
#plt.show()



# Test

data_list = list()
mypath = "2022-07-23.log"
mylog = open(mypath, 'r')
for line in mylog:
  new_line = json.loads(line)
  
#mycon = mylog.read()
#mydata = json.loads(mycon)
  print("newline",mylog)
  mydata = json.loads(l)
  data_list.append(mydata)  
print(data_list)

# for diffrent pathing
'''
corrent_path = logs_path = "Files"
files = os.listdir(logs_path)
for folder in files:
  corrent_path = f"{logs_path}/{folder}/Domain Log"
  inside_folder = os.listdir(corrent_path)
  for file_name in inside_folder:
    print(f"Folder name is: {file_name}")
    corrent_path = f"{logs_path}/{folder}/Domain Log/{file_name}"
    inside_inside_folder = os.listdir(corrent_path)
    for log_file in inside_inside_folder:
      if log_file.endswith(".log"):
        print(f"inside file name is: {log_file}")
        corrent_path = f"{logs_path}/{folder}/Domain Log/{file_name}/{log_file}"
        f = open(corrent_path,"r")
#        log_data = json.dumps(f)        
        print(f.readline())
#        print(log_data)
#        x = mycol.insert_many(f)
        f.close()        


#def create_db():
# Stablish Mongo Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Create DataBase
db = client["Manzoome"]
# Create Collection(Table)
log_table = db["logs_collection"]
x = log_table.insert_many(mylist)
print (db.list_collection_names())
#    return db

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids) 



class C(ABC):
    @abstractmethod
    def my_abstract_method(self, arg1):
        ...
    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls, arg2):
        ...
    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod(arg3):
        ...

    @property
    @abstractmethod
    def my_abstract_property(self):
        ...
    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self, val):
        ...

    @abstractmethod
    def _get_x(self):
        ...
    @abstractmethod
    def _set_x(self, val):
        ...
    x = property(_get_x, _set_x)

# __subclasshook__(subclass)
class Foo:
    def __getitem__(self, index):
        ...
    def __len__(self):
        ...
    def get_iterator(self):
        return iter(self)

class MyIterable(ABC):

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

MyIterable.register(Foo)

# example
class Animal(ABC):
    @property                 
    def food_eaten(self):     
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}.")

    @property
    @abstractmethod
    def diet(self):
        pass

    @abstractmethod 
    def feed(self, time):
        pass

class Lion(Animal):
    @property                 
    def diet(self):     
        return ["antelope", "cheetah", "buffaloe"]

    def feed(self, time):
        print(f"Feeding a lion with {self._food} meat! At {time}") 

class Snake(Animal):
    @property                 
    def diet(self):     
        return ["frog", "rabbit"]

    def feed(self, time): 
        print(f"Feeding a snake with {self._food} meat! At {time}") 


if __name__ == "__main__":        
  # connect to database
  mongo_conenction.connect()
'''