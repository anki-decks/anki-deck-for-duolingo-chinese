import re
import unicodecsv as csv
import sys
import requests
from bs4 import BeautifulSoup
import urllib.parse

def getDef(chWord) :
  print("Fecthing word : {}".format(chWord))

  retVal = {'success' : False}

  url = "https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb={}".format(chWord)

  print(url)

  page = requests.get(url)

  if page.status_code != 200 :
    print("error")
    retVal['error'] = "Unable to fetch data"

    return(retVal)

  soup = BeautifulSoup(page.content, 'html.parser')

  #print(soup.prettify())

  wordRslts = soup.find('table', class_='wordresults')

  if len(wordRslts) == 0:
    print("error")
    retVal['error'] = "Unable to find the word"
    return(retVal)

  rows = wordRslts.find('tbody').find_all('tr', class_='row')

  wordDetails = []

  for row in rows:
    wordDetail = {}

    details = row.find('td', class_='details').find('div', class_='defs').text.strip()

    if re.search(r"^(\w*) variant of", details) or re.search(r"^variant of", details) :
      print("Found variant in detail for {}".format(chWord))
      continue

    head = row.find('td', class_='head')

    hanzi = ""
    hanziSpans = head.find('div', class_='hanzi').find_all('span')

    for span in hanziSpans :
      #print ("hanzi in span = {}".format(span.text))
      hanzi = hanzi + span.text.strip()

    pinyin = ""
    pinyinSpans = head.find('div', class_='pinyin').find_all('span')

    for span in pinyinSpans:
      pinyin = pinyin + span.text.strip() + ' '
    
    traditional = ""
    tradHanziDiv = row.find('td', class_='tail').find('div', class_='hanzi')

    if tradHanziDiv :
      tradSpans = tradHanziDiv.find_all('span')
      for span in tradSpans:
        traditional = traditional + span.text.strip() 
 
    if (hanzi == chWord) :
      wordDetail['hanzi']   = hanzi
      wordDetail['traditional']   = traditional
      wordDetail['pinyin']  = pinyin
      wordDetail['details'] = details

      wordDetails.append(wordDetail)

    else :
      print ("Hanzi Mismatch {} != {}".format(hanzi, chWord))

  retVal['word_details'] = wordDetails
  retVal['success']      = True

  return(retVal)


def main(inDefsFileName, outFileName):
  inWordsDict = {}
  inWordsList = []
  outputWords = []

  with open(inDefsFileName, "rb") as inCsvfile:
    inWordDefs = csv.DictReader(inCsvfile)

    print("after CSV reading")

    for inWordDef in inWordDefs:

      if inWordDef["Result"] == "True" :
        outputWords.append(inWordDef)
        continue

      inWord = inWordDef['Chinese']

      rslt = getDef(inWord)

      outputWord = inWordDef
      outputWord['Result'] = False

      if rslt['success'] :
        wordDetails = rslt['word_details']

        pinyinList = []
        defList = []
        tradList = []

        for wd in wordDetails:
          pinyinList.append(wd['pinyin'])
          defList.append(wd['details'])
          tradList.append(wd['traditional'])

        
        if len(pinyinList) > 0:
          pinyin      = "<br />".join(pinyinList)
          definition  = "<br />".join(defList)

          traditional = tradList[0]

          print('Chinese : {}, Traditional : {}, PinYin : {}, Details : {}'.format(inWord, traditional, pinyin, definition))

          outputWord['Traditional'] = traditional
          outputWord['Pinyin']      = pinyin
          outputWord['Definition']  = definition
          outputWord['Result']      = True
        else :
          print('Failed to get details for : {}'.format(inWord))
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
