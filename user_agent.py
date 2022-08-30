import pyodbc

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
print(rows)
#loginUsers = curs.execute("select top(200) rkey,userid,ownerid, dmn_id from userslog where status=3 and active=1 order by id desc")

