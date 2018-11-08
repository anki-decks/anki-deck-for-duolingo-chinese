import csv

cn2en = {}
nonHSK = {}

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
with open("HSK_all.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    #print(row['Chinese'] ,row ['Pinyin'],row ['English Definition'])
    tmpKey = row['Chinese']

    if tmpKey in cn2en.keys() :
      print("Word {} already exists in HSK".format(tmpKey))

    cn2en[row['Chinese']] = row

for key in cn2en.keys():
  keyLen = len(key)

  tr = cn2en[key]

  if (keyLen >= 2) :
    for index, subKey in enumerate(key):
      if not subKey in cn2en.keys():
        #print("index ", index)
        #print(tr['Pinyin'].split(" "))

        entry = {}
        entry['Chinese'] = subKey
        entry['Pinyin'] = tr['Pinyin'].split(" ")[index]
        entry['English Definition'] = ''
        nonHSK[subKey] = entry 

writeFile = open("duolingo.html", "w")

writeFile.write("<!DOCTYPE html><html><head>")
writeFile.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">')

writeFile.write('<style>#toc_container { background: #f9f9f9 none repeat scroll 0 0; border: 1px solid #aaa; display: table; font-size: 95%; margin-bottom: 1em; padding: 20px; width: auto; } .toc_title { font-weight: 700; text-align: center; } #toc_container li, #toc_container ul, #toc_container ul li{ list-style: outside none none !important; }</style>')

writeFile.write("</head><body>")
writeFile.write('<div class="container"> <div class="row"><div class="col-sm-8">')

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
    writeFile.write('<thead><tr> <th class="col-sm-2">Simplified Chinese</th> <th class="col-sm-2">Pinyin</th> <th class="col-sm-4">English Definition</th> </tr></thead><tbody>')

    words = lesson[0].split(", ")


    for word in words:
      #print("Word - {}".format(word))

      if not word in duoWordsDict.keys():
        duoWordsDict[word] = True
        duoWordsList.append(word)

      if word in cn2en.keys() :
        tr = cn2en[word]

        #print("Check 1 Word - {}, Word - {}".format(word, tr['Chinese']))
        
        writeFile.write("<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(tr['Chinese'], tr['Pinyin'], tr['English Definition']))

      elif word in nonHSK.keys() :
        if word not in notFoundDict.keys() :
          notFoundDict[word] = word
          notFoundList.append(word)

        tr = nonHSK[word]

        #print("Check 2 Word - {}, Word - {}".format(word, tr['Chinese']))

        writeFile.write("<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(tr['Chinese'], tr['Pinyin'], tr['English Definition']))
 
      else :
        if word not in notFoundDict.keys() :
          notFoundDict[word] = word
          notFoundList.append(word)

        writeFile.write("<tr><td>{}</td><td>-</td><td>-</td></tr>".format(word))

    writeFile.write("</tbody></table><br/>")

writeFile.write('</div></div></div>')
writeFile.write("</html></body>")

print("Not found words")
print("\n".join(notFoundList))

print("\nDuoLingo words")
print("\n".join(duoWordsList))
