import csv

with open('data_fixed.csv') as f:
	with open('newDB_string.csv', 'w') as f2:
		csvReader = csv.reader(f)
		f2.write('{\n'+"\"data\" : [\n")
		for row in csvReader:
			strText = "\"text\" : \"Can you show me how to say "+row[1]+" in ASL\","
			lenStr = len("Can you show me how to say ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line1= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line1)


			strText = "\"text\" : \"Tell me how to say "+row[1]+'\",'
			lenStr = len("Tell me how to say ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line2= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line2)

			strText = "\"text\" : \"I want to say "+row[1]+'\",'
			lenStr = len("I want to say ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line3= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line3)

			strText = "\"text\" : \"I want to translate in sign language "+row[1]+'\",'
			lenStr = len("I want to translate in sign language ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line4= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line4)

			strText = "\"text\" : \"I'm interested in saying "+row[1]+" in sign language"+'\",'
			lenStr = len("I'm interested in saying ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line5= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line5)

			strText = "\"text\" : \"Can you show me how to say "+row[1]+" in ASL"+'\",'
			lenStr = len("Can you show me how to say ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line6= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line6)

			strText = "\"text\" : \"Please show me how to translate "+row[1]+" in ASL"+'\",'
			lenStr = len("Please show me how to translate ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line7= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line7)

			strText = "\"text\" : \"What is "+row[1]+'\",'
			lenStr = len("What is ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line8= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line8)

			strText = "\"text\" : \"I want the word "+row[1]+'\",'
			lenStr = len("I want the word ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line9= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line9)

			strText = "\"text\" : \"I want "+row[1]+'\",'
			lenStr = len("I want ")
			indexStart = lenStr
			lenWord = len(row[1])
			indexEnd = indexStart+lenWord
			line10= '{'+'\n'+strText+'\n'+"\"entities\" : ["+'\n'+'{'+'\"entity\" : \"intent\",'+'\n'+'\"value\" : \"\\"'+row[1]+'\\"\",'+'\n'+"\"start\" : "+ str(indexStart)+',\n'+"\"end\" : "+ str(indexEnd)+'\n}\n]\n},'
			f2.write(line10)
		f2.write("]\n}")