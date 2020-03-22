
#Goal: Scrape Worldometers

import lxml.html as LH
import requests

page = requests.get('https://www.worldometers.info/coronavirus/#countries')
doc = LH.fromstring(page.content)


tr_elements = doc.xpath('//tr')

#sanity check: do the rows have same number of columns
#outlist = [len(T) for T in tr_elements[:12]]
#print (outlist)

hcol=[]
j=0

#this loop is to get names from table header
for t in tr_elements[0]:
    name = t.text_content()
    #print ('%d:"%s"' % (j, name))
    hcol.append((name,[]))
    #j+=1
    
#this test loop is to print country name and cases from top countries
#for i in range(1,4):
#    j=0
#    for t in tr_elements[i]:
#        name = hcol[j]
#        value = t.text_content()
#        print ('"%s": "%s"' % (name, value))
#        j+=1
#        if j == 3:
#           break

#ccases is a key-value store for countries vs cases
#the cases are the current cases (need to build history separately)
ccases = {}
for i in range(1,4):
    country = tr_elements[i][0].text_content()
    cases = tr_elements[i][1].text_content()
    ccases.update( {str(country) : cases} )

for key in ccases.keys():
    value = ccases[key]
    print("Country ", key, ":  ", value, " total cases")
