from bs4 import BeautifulSoup
html=input()
soup = BeautifulSoup(html,features="lxml")
s=soup.get_text()
p=s.replace(" ","")
print(" ".join(p))     
