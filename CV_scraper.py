
#Goal: Scrape Worldometers
#authors: Mihir, Bharadwaj, <add more>

import lxml.html as LH
import requests

page = requests.get('https://www.worldometers.info/coronavirus/#countries')
doc = LH.fromstring(page.content)


tr_elements = doc.xpath('//tr')

#sanity check: do the rows have same number of columns
#outlist = [len(T) for T in tr_elements[:12]]
#print (outlist)

hcol=[]
i=0

#this loop is to get names from table header
for t in tr_elements[0]:
    i+=1
    name = t.text_content()
    #print ('%d:"%s"' % (i, name))
    hcol.append((name,[]))

# this loop is to get country name and cases from top countries
for i in range(1,4):
    j=0
    for t in tr_elements[i]:
        value = t.text_content()
        name = hcol[j]
        print ('"%s": "%s"' % (name, value))
        j+=1
        if j == 3:
            break

