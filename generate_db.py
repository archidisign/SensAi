import csv
with open('newDB.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    mycsv = open("db_sentence_intent.csv", 'wt')
    mywriter = csv.writer(mycsv)

    for row in spamreader:
        x = row[1]
        myarray = [10]
        mycsv.write("Tell me how to say " + x + "," + x + "\n")
        mycsv.write("I want to say " + x + "," + x + "\n")
        mycsv.write("Can you tell me how to say " + x + "," + x + "\n")
        mycsv.write("I want to translate in sign language " + x + "," + x + "\n")
        mycsv.write("I'm interested in saying " + x + " in sign language " + "," + x + "\n")
        mycsv.write("Can you show me how to say " + x + " in ASL" + "," + x + "\n")
        mycsv.write("Please show me how to translate " + x + " in ASL" + "," + x + "\n")
        mycsv.write("What is " + x + "," + x + "\n")
        mycsv.write("I want the word " + x + "," + x + "\n")
        mycsv.write("I want " + x + "," + x + "\n")
        mycsv.write("Tell me how to say " + x + "," + x + "\n")
        print row
mycsv.close()
csvfile.close()
