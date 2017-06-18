import csv
import json
import StringIO



with open('DB_fixed_s_i.csv', 'rb') as csvfile:
    with open('fileName.csv', 'w') as f:
        spamreader = csv.reader(csvfile)
        spamwriter = csv.writer(f)
        string = '{\n  "data" : [\n'

        for row in spamreader:
            myarray = [10]
            myarray.append("Tell me how to say " + x)
            myarray.sppend("Can you show me how to say " + x)
            myarray.append("I want to say " + x  )
            myarray.append("Can you tell me how to say " + x )
            myarray.append("I want to translate in sign language " + x)
            myarray.append("I'm interested in saying " + x + " in sign language")
            myarray.append("Can you show me how to say " + x + " in ASL")
            myarray.append("Please show me how to translate " + x + " in ASL")
            myarray.append("What is " + x )
            myarray.append("I want the word " + x )
            myarray.append("I want " + x)
            myarray.append("Tell me how to say " + x)

            x = row[1]
            lgt = len(x)
            string1 = '    {\n      "text": '+myarray[0]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'
            string2 = '    {\n      "text": '+myarray[1]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'
            string3 = '    {\n      "text": '+myarray[2]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'
            string4 = '    {\n      "text": '+myarray[3]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'
            string5 = '    {\n      "text": '+myarray[4]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'
            string6 = '    {\n      "text": '+myarray[5]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'
            string7 = '    {\n      "text": '+myarray[6]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'
            string8 = '    {\n      "text": '+myarray[7]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'
            string9 = '    {\n      "text": '+myarray[8]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'
            string10 = '    {\n      "text": '+myarray[9]+',\n      "entities": [\n        {\n          "entity": "intent",\n          "value": "\\"'+x+'\\"",\n          "start": '+str(idx)+',\n          "end": '+str(idx+lgt)+'\n        }\n      ]\n    },'

            for row2 in f:
                f.write(string)
        #datap = {}
        #insidedic = {}
        #mystuff['text'] = dotit1
        #datap['data'] = mystuff
        #json_data = json.dumps(data)





csvfile.close()