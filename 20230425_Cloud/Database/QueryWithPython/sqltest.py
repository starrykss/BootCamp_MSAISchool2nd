import pyodbc

server = 'mysqlserver-rg111.database.windows.net'
database = 'mySampleDatabase'
username = 'devastra'
password = ''
driver= '{ODBC Driver 18 for SQL Server}'

cnxn = pyodbc.connect('DRIVER=' + driver + '; PORT=1433; SERVER=' + server + ';PORT=1443; DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

# 쿼리 실행하기
cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()

# 행 삽입하기
count = cursor.execute("""
    INSERT INTO SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) 
    VALUES (?, ?, ?, ?, GETDATE())""",
    'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0).rowcount
cnxn.commit()
print('Rows inserted: ' + str(count))