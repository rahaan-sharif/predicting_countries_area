import mysql.connector
from sklearn import tree

cnx = mysql.connector.connect(user="rahaan_database", password="sharifi",
                              host="localhost", database="country")
cursor=cnx.cursor()
cursor.execute("select * from v;")
resault=cursor.fetchall()


x=[]
y=[]
#third: population        fourth: area
for row in resault:
          x+=[[row[2]]]
          y+=[[row[3]]]

clf=tree.DecisionTreeClassifier()
clf.fit(x,y)

new_population=[[int(input("enter population: "))]]
predicted_area=clf.predict(new_population)
print("\npredicted area:    ", predicted_area[0])

          
          
cnx.close()