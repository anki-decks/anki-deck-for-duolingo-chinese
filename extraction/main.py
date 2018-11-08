import unicodecsv as csv

cn2en = {}

subjects = []
state = 0

subject = {}
lessons = []

notFoundDict = {}
notFoundList = []

duoWordsDict = {}
duoWordsList = []

with open('duolingo_words.txt') as inFile:
  
  for line in inFile:
    line = line.strip()

    if line == "" :
      if state != 0 :
        subject["lessons"] = lessons
        subjects.append(subject)
        subject = {}
        lessons = []
        state = 0
    elif state == 0 :
      subject["title"] = line
      state = 1
    else :
      lessons.append([line])

if state != 0:
  subject["lessons"] = lessons
  subjects.append(subject)    

with open("duolingo_all_words_mdbg_corrected.csv", "rb") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    #print(row['Chinese'] ,row ['Pinyin'],row ['Definition'])
    tmpKey = row['Chinese']

    if tmpKey in cn2en.keys() :
      print("Word {} already exists in HSK".format(tmpKey))

    cn2en[row['Chinese']] = row

writeFile = open("duolingo.html", "w")

writeFile.write("<!DOCTYPE html><html><head>")
writeFile.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">')

writeFile.write('<style>#toc_container { background: #f9f9f9 none repeat scroll 0 0; border: 1px solid #aaa; display: table; font-size: 95%; margin-bottom: 1em; padding: 20px; width: auto; } .toc_title { font-weight: 700; text-align: center; } #toc_container li, #toc_container ul, #toc_container ul li{ list-style: outside none none !important; }</style>')

writeFile.write("</head><body>")
writeFile.write('<div class="container">')
writeFile.write('<div class="row">')
writeFile.write('<h3>Introduction</h3>')
writeFile.write('<p>This file contains the words list of Duolingo Chinese Mandarin. The word list was taken on 7 Jan 2018. The word definition is picked from https://www.mdbg.net/chinese/dictionary. Please note there might be mistakes. Please email anishcr@gmail.com for any corrections/updates.</p>')
writeFile.write('</div>')

writeFile.write('<div class="row"><div class="col-sm-8">')

id = 0

writeFile.write('<div id="toc_container">')
writeFile.write('<p class="toc_title">Contents</p>')
writeFile.write('<ul class="toc_list">')

for subject in subjects:
  id += 1

  lessonNum = 0

  lessons = subject["lessons"]

  writeFile.write('<li><a href="#{}">{}</a>'.format(id, subject["title"]))
  writeFile.write('  <ul>')

  for lesson in lessons :
    lessonNum += 1
    id += 1

    writeFile.write('    <li><a href="#{}">Lesson {}</a></li>'.format(id, lessonNum))

  writeFile.write('  </ul>')
  writeFile.write('</li>')

writeFile.write('</ul>')
writeFile.write('</div>')

id = 0
for subject in subjects:
  id += 1
  lessons = subject["lessons"]
  lessonNum = 0

  writeFile.write('<h3 id="{}">{}</h3>'.format(id, subject["title"]))

  for lesson in lessons:
    #print(lesson)

    lessonNum += 1
    id += 1

    writeFile.write('<table class="table table-bordered" id="{}">'.format(id))
    writeFile.write('<caption>Lesson - {}</caption>'.format(lessonNum))
    writeFile.write('<thead><tr> <th class="col-sm-2">Simplified Chinese</th> <th class="col-sm-2">Traditional Chinese</th> <th class="col-sm-2">Pinyin</th> <th class="col-sm-4">English Definition</th> </tr></thead><tbody>')

    words = lesson[0].split(", ")


    for word in words:
      #print("Word - {}".format(word))

      if not word in duoWordsDict.keys():
        duoWordsDict[word] = True
        duoWordsList.append(word)

      if word in cn2en.keys() :
        tr = cn2en[word]

        #print("Check 1 Word - {}, Word - {}".format(word, tr['Chinese']))
        
        pinyin     = tr['Pinyin']
        definition = tr['Definition']
 
        pinyin = pinyin.replace("<br />", "<br /><br />");
        definition = definition.replace("<br />", "<br /><br />");

        writeFile.write("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(tr['Chinese'], tr['Traditional'], pinyin, definition))

      else :
        if word not in notFoundDict.keys() :
          notFoundDict[word] = word
          notFoundList.append(word)

        writeFile.write("<tr><td>{}</td><td>-</td><td>-</td></tr>".format(word))

    writeFile.write("</tbody></table><br/>")

writeFile.write('</div></div></div>')
writeFile.write("</html></body>")
