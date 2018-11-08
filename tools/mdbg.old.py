import unicodecsv as csv
import sys
import requests
from bs4 import BeautifulSoup


def getDef(chWord) :
  retVal = {'success' : False}

  page = requests.get("https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb={}".format(chWord))

  if page.status_code != 200 :
    print("error")
    retVal['error'] = "Unable to fetch data"

    return(retVal)

  soup = BeautifulSoup(page.content, 'html.parser')

  #print(soup.prettify())

  wordRslts = soup.find('table', class_='wordresults')

  if len(wordRslts) == 0:
    retVal['error'] = "Unable to find the word"
    return(retVal)

  rows = wordRslts.find('tbody').find_all('tr', class_='row')

  wordDetails = []

  for row in rows:
    wordDetail = {}

    head = row.find('td', class_='head')

    hanzi = head.find('div', class_='hanzi').find('span').text

    pinyin = head.find('div', class_='pinyin').find('span').text
    
    details = row.find('td', class_='details').find('div', class_='defs').text
 
    if (hanzi == chWord) :
      wordDetail['hanzi']   = hanzi
      wordDetail['pinyin']  = pinyin
      wordDetail['details'] = details

      wordDetails.append(wordDetail)

  retVal['word_details'] = wordDetails
  retVal['success']      = True

  return(retVal)


def main(inDefsFileName, outFileName):
  inWordsDict = {}
  inWordsList = []
  outputWords = []

  inDefsWordDetails

  with open(inDefsFileName) as inCsvfile:
    inWordDefs = csv.DictReader(inCsvfile)

    for inWordDef in inWordDefs:
      
      if not exists i

  with open(inWordsFileName) as inFile:
    for line in inFile:
      line = line.strip()
      inWordsList.append(line)

  for inWord in inWordsList :

      rslt = getDef(inWord)

      outputWord = {'Chinese' : inWord, 'Pinyin' : '', 'Definition' : ''}

      if rslt['success'] :
        wordDetails = rslt['word_details']

        pinyinList = []
        defList = []

        for wd in wordDetails:
          pinyinList.append(wd['pinyin'])
          defList.append(wd['details'])

        
        pinyin = "<br />".join(pinyinList)
        definition    = "<br />".join(defList)

        #print('Chinese : {}, PinYin : {}, Details : {}'.format(inWord, pinyin, definition))

        outputWord['Pinyin']     = pinyin
        outputWord['Definition'] = definition
      else :
        print("Failed to fetch details for : {}. Reason : {}".format(inWord, rslt['error']))

      outputWords.append(outputWord)

  keys = outputWords[0].keys()

  with open(outFileName, 'wb') as outFile:
    dictWriter = csv.DictWriter(outFile, fieldnames=keys, lineterminator='\n', quoting=csv.QUOTE_ALL)
    dictWriter.writeheader()
    dictWriter.writerows(outputWords)

    
#main('1.txt', 'mdbg.csv')
main('duolingo_all_words_mdbg_corrected.csv', 'duolingo_all_words_mdbg.csv')
