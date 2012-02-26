
import re
import urllib

url = "http://www.pythontr.org/Python_Programlama/AlarmClock.txt"

f = urllib.urlopen(url)

for i in f:
    nesne = re.search('<a href=".+html">.+</a>',i)
    print i
