from lxml import html

fi = open("Edmodo2.html","r",encoding="utf-8")
htmldata=fi.read()
tree = html.fromstring(htmldata)
quizzes = tree.xpath('//span[@class="quiz-name-long"]/text()')

fo = open("quizzes2.csv","w",encoding="utf-8")
for quiz in quizzes:
    fo.write('"'+quiz+'"')
    fo.write("\n")
fo.close()

print(len(quizzes),"lines written")




