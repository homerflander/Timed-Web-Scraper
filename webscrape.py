import requests
import sys
import time
from bs4 import BeautifulSoup

print("-------Scrape a List off the Web-------")
url=str(input("Enter in the HTML URL you want to scrape \n"))

typeofclass=str(input("Enter in the class type you want to scrape \n"))
nameofclass=str(input("Enter in the class name you want to scrape \n"))
timerwait=int(input("Enter in the desired seconds for the timer that is greater than or equal to 60 seconds. \n"))

url=url.strip()
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
links=soup.find_all(typeofclass,{"class":nameofclass})
counter=1
list1=""
list2=""
exitloop=0
start=time.time()

if(timerwait<60):
    print("You have entered a time that is less that 60. Error. Exiting.\n")
    sys.exit()

print("Here is your initial list (list one), you will notified if any changes occur \n")

for link in links:
    list1=list1+(str(counter) + ". " + link.text + "\n")
    print(str(counter) + ". " + link.text + "\n")
    counter = counter + 1

counter=1

while(exitloop==0):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.find_all(typeofclass, {"class": nameofclass})
    for link in links:
        list2=list2+(str(counter)+". "+link.text+"\n")
        counter=counter+1
    time.sleep(timerwait)
    counter=1
    current=time.time()
    print("Elapsed Time:"+str(current-start)+"\n")
    if(list2!=list1):
        print("A change has occurred. List One:\n"+list1+"\n Does not match with List Two:\n"+list2)
        exitloop=1
    list2=""