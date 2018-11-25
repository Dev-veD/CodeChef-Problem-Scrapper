from bs4 import BeautifulSoup
import requests
print("Enter The Problem Code")
xx=input()
src = requests.get('https://www.codechef.com/problems/'+xx).text
soup = BeautifulSoup(src, 'lxml')
a = soup.find('title').text
a=a.split('|')[0]
print(a)
problem_id=soup.find('span', id="problem-code").text
print(problem_id)

content=soup.find('div',class_="node clear-block")
x=content.find('div',class_='content').text
print(x)
name=a+'.txt'
fo=open(name,'w',encoding='utf-8')
fo.write(a+'\n')
fo.write("Problem Id : "+problem_id+'\n')
fo.write(x)
fo.close()