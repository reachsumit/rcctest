import pymysql, csv, requests
from pymysql import MySQLError

from PIL import Image
from io import BytesIO

connection = pymysql.connect(host='us-cdbr-iron-east-05.cleardb.net',
                             user='b02d8834ffb9be',
                             password='c9268f14',
                             db='heroku_5dbfec48ecba66c',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

with open("scraped_data.csv","r") as filename:
    reader = csv.reader(filename,delimiter=',')
    next(reader)
    for row in reader:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO webapp_bikes (`SKU`, `name`, `description`,`rating`,`price`,`quantity`,`type`,`image`) VALUES (\"%s\", \"%s\",\"%s\",%f,%f,%d,\"%s\",\"%s\")" % (row[0],row[1],row[2].replace('"',''),float(row[3]),float(row[4]),int(row[5]),row[6],row[7])
                cursor.execute(sql)
                connection.commit()
        except MySQLError as e:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
    connection.close()