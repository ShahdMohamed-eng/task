from PyPDF2 import PdfReader
reader = PdfReader('example.pdf')
number_of_pages=len(reader.pages)
words=[]
for i in number_of_pages:
    page=reader.pages[i]
    for j in page:
        x = []
        if i==" ":
            words.append(x)
            x=[]
        else:
            x.append(i)

print(words)

