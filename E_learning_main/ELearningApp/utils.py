import os
import PyPDF2
file=open('main.pdf','rb')   # open file in read-binary mode
grabber=PyPDF2.PdfFileReader(file)
grabber.decrypt('')

command=('cp '+file+" temp.pdf")
print(grabber.numPages)
#x=pageObj.extractText()
#print(type(x),x)
