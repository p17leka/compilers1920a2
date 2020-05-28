import re

#function used to turn html special entities into something else according to table

def function(i):
        if(i.group(0) == "&amp;"):
                return '&'
        elif (i.group(0) == "&gt;"):
                return '>'
        elif (i.group(0) == "&lt;"):
                return '<'
        elif (i.group(0) == "&nbsp;"):
                return ' '

rexp1 = re.compile(r'<title>(.+?)</title>') #export title process 1 thats asked
rexp2 = re.compile(r'<!--.*?-->',re.DOTALL) #export comments process 2 thats asked 
rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL) #export script and style tags with their content process 3 thats asked 
rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) #export hrefs-links process 4 thats asked
rexp5 = re.compile(r'(<.+?/>)|(<.+?>|</.+?>)',re.DOTALL) #export tags like <..../> process 5 thats asked also export tags like <...>...<..../> also process 5 thats asked
rexp6 = re.compile(r'&(amp|gt|lt|nbsp)') #export html special entities according to table presented process 6 thats asked
rexp7 = re.compile(r'\s+') #export continuous whitespace characters process 7 thats asked

text = open('testpage.txt','r').read() #read file 
i = rexp1.search(text)
print(i.group(1)) #print title process 1 thats asked

text = rexp2.sub(' ',text) #remove comments process 2 thats asked
text = rexp3.sub(' ',text) #remove script and style tags with their content process 3 thats asked

for i in rexp4.finditer(text):  
        print('{} {}'.format(i.group(1),i.group(2)))  #print links process 4 thats asked

text = rexp5.sub(' ',text) #remove tags process 5 thats asked
text = rexp6.sub(function,text) #replace entities according to table check function used process 6 thats asked
text = rexp7.sub(' ',text) #replace continuous whitespaces with one whitespace process 7 thats asked

print(text) #print the text file after all the processes
