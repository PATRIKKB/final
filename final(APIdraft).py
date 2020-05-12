import requests, bs4

#res = requests.get('https://eservices.minnstate.edu/registration/search/advancedSubmit.html?campusid=305&searchrcid=0305&searchcampusid=305&yrtr=20205&subject=ITEC&courseNumber=&courseId=&openValue=OPEN_PLUS_WAITLIST&delivery=ALL&showAdvanced=&starttime=&endtime=&mntransfer=&credittype=ALL&credits=&instructor=&keyword=&begindate=&site=&resultNumber=250')

#res.raise_for_status()

#eservices_soup = bs4.BeautifulSoup(res.text, features="lxml")
#type(eservices_soup)

eservices_file = open('/Users/Pan 1/Pictures/Course Search Results - Student e-Services.html')
eservices_soup = bs4.BeautifulSoup(eservices_file, features="lxml")
elems_a = eservices_soup.select('a')
#print(type(elems_a))
#print(len(elems_a))
#print(type(elems_a[4]))
#print(elems_a[5].getText())

x = -1
while int(x) < 1000:
    try:
        x += 1
        for i in elems_a:
            if elems_a[x] == '':
              pass  
            else:
                print(elems_a[x].getText())
                #print(elems_a[x].attrs)
            break
    except IndexError:
        break
