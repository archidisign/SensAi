import requests
import csv
import nltk
from nltk import pos_tag, word_tokenize

mycsv = open("dbcsv3.csv", 'wt')
mywriter = csv.writer(mycsv, delimiter='|', quoting=csv.QUOTE_NONE)

headings = '#,Word,Link,POS,Definition\n'
mycsv.write(headings)
#headings = ['#','Word','Link','POS','Definition']
#for column in headings:
#    mycsv.write('%s|' % column)
#mycsv.write('\n')

for i in range(3000,5000):

    # Exceptions (accent problem with word 'fiancee')
    if (i==2416):
        word = "fiancee"
        fulllink = "https://www.handspeak.com/word/f/fiancee.mp4"
        myPOS = nltk.pos_tag(word_tokenize(word))
        POS = myPOS[0][1]
        # Define the definition
        defStart = '<span itemprop="description">'
        lenStart2 = len(defStart)
        indexStart2 = data.find(defStart)
        newData = data[indexStart2:]
        # Find the good end index
        indexEnd2 = indexStart2+newData.find('\n')
        indexEnd3 = indexStart2+newData.find('</span>')
        if indexEnd2<indexEnd3:
            official_end = indexEnd2
        else:
            official_end = indexEnd3
        defin = data[indexStart2+lenStart2:official_end]
        # Define values in CSV format
        finalline = str(i)+','+word+','+fulllink+','+POS+'\n'
        mycsv.write(finalline)
        continue

    # Extract data from site
    r = requests.get('https://www.handspeak.com/word/search/index.php?id='+str(i))
    data = r.text

    # Define the word
    wordStart = '<h2><span itemprop="name">ASL sign for: '
    wordEnd = '</span></h2>'
    lenStart = len(wordStart)
    indexStart = data.find(wordStart)
    indexEnd = data.find(wordEnd)
    word = data[indexStart+lenStart:indexEnd]

    # Define the link
    mp4Start = '<video id="mySign" class="v-asl" autoplay'
    mp4End = '" type="video/mp4"'
    lenStart1 = len(mp4Start)
    lenStart01 = len('src="')
    indexStart1 = data.find(mp4Start)
    indexEnd1 = data.find(mp4End)
    weblink = data[indexStart1+lenStart1+lenStart01+lenStart01:indexEnd1]
    addtolink = "https://www.handspeak.com"
    fulllink = addtolink+weblink

    # Define the part of speech (POS)
    myPOS = nltk.pos_tag(word_tokenize(word))
    POS = myPOS[0][1]

    # Define the definition
    defStart = '<span itemprop="description">'
    lenStart2 = len(defStart)
    indexStart2 = data.find(defStart)
    newData = data[indexStart2:]

    # Find the good end index
    indexEnd2 = indexStart2+newData.find('\n')
    indexEnd3 = indexStart2+newData.find('</span>')
    if indexEnd2<indexEnd3:
        official_end = indexEnd2
    else:
        official_end = indexEnd3
    defin = data[indexStart2+lenStart2:official_end]

    # Exceptional cases
    if (i==196):
        defin = 'Osama bin Laden (1957-2011), notorious international Saudi-born terrorist and leader of the terrorist network Al-Qaeda.'
    if (i==385):
        defin = 'a communist nation in East Asia; the world\'s most populous country.'

    # Define values in CSV format
    finalline = str(i)+',"'+word+'",'+fulllink+','+POS+'\n'
    #finalline = str(i)+'|'+word+'|'+fulllink+'|'+POS+'|'+defin+'\n'
    #finalline = [str(i),word,fulllink,POS,defin]
    print(finalline)

    # Write in CSV file
    mycsv.write(finalline)
    #for column in finalline:
        #mycsv.write('%s|' % column)
    #mycsv.write('\n')

mycsv.close()