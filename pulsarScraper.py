from mechanize import Browser
from BeautifulSoup import BeautifulSoup

br = Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open('https://pulsar.cnu.edu/soc/socquery.aspx')

pulsarForm = br.response()

br.select_form(nr=0)

br.set_all_readonly(False)

br.form['startyearlist']=['1',]
#br.form['DisciplinesListBox']=['Computer Science', 'Computer Engineering', 'Engineering']

returned_form = br.submit(nr=0).read()
with open('output.html', 'w') as f:
	f.write(returned_form)

soup = BeautifulSoup(returned_form)
table = soup.find("table")
rows = table.findAll("tr")
tableHeader = ['CRN', 'Course', 'Section', 'Title', 'Hours', 'AoI', 'Type', 'Days','Time','Location','Instructor','Seats','Status']
data = []
for row in rows:
	cells = row.findAll("td")
	cells = [ele.text.strip() for ele in cells]
	rowDict = dict(zip(tableHeader, cells))
	
	data.append(rowDict)

