import urllib2
from bs4 import BeautifulSoup

fd = open(r'output.html', 'w')

for i in range(1, 100):
    response = urllib2.urlopen(r'http://ielts-simon.com/ielts-help-and-english-pr/ielts-writing-task-2/page/' + str(i))
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    lst_lesson = soup.find_all(attrs={'class': 'entry-inner'})
    if len(lst_lesson) == 0:
        break
    else:
        for lesson in lst_lesson:
            fd.write(str(lesson))
            # for content in lesson.contents:
            #     fd.write(content)
            #     fd.write('\n')

fd.close()
pass