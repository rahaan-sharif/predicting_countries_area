import mysql.connector
import requests
from bs4 import BeautifulSoup

web_address="https://www.scrapethissite.com/pages/simple/"
response1=requests.get(web_address)
response2=BeautifulSoup(response1.text, "html.parser")
response3=response2.find("h3")
response4=response2.find_all("h3")
print("\n\n\n\n")


#capital:
capt_list=[]

tmp_str=[]
for item in response4:
          counter=0
          while(1):
                    tmp=str(item).split()[5+counter]
                    if(tmp!=str(item).split()[-1]):
                              tmp_str+=[tmp]
                    else:
                              break
                    counter+=1
          capt_list+=[" ".join(tmp_str)]
          tmp_str=[]


#population, area, capital
temp_list2=[]
response5=response2.find_all("span")
for i in range(len(response5)):
          list=[]
          temp_list=str(response5[i]).replace("<",">").split(">")
          value=temp_list[-3]
          list=[value]
          temp_list2+=[list]


var_list=[]
for i in range(int(len(temp_list2)/3)):
          temp_list3=[capt_list[i], temp_list2[3*i+0][0], int(temp_list2[3*i+1][0]), float(temp_list2[3*i+2][0])]
          var_list+=[temp_list3]


#*****************************************************
#in this level, we save the values to our databases:
cnx=mysql.connector.connect(user="rahaan_database", password="sharifi", 
                            host="localhost", database="country")
print("connected to database")
cursor=cnx.cursor()
for i in range(len(var_list)):
          print(var_list[i][0], "   ",var_list[i][1],"   ", var_list[i][2],"   ", var_list[i][3])
          cursor.execute("insert into v values(\"%s\", \"%s\", %i, %i)"
                         %(var_list[i][0], var_list[i][1], var_list[i][2], var_list[i][3]))
          cnx.commit()
cnx.commit()
cnx.close()
print("end of program")
