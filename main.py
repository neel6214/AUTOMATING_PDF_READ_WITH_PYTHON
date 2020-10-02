import pyttsx3
import PyPDF2

book = open("DELD_PPT1_SG.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()

start = int(input("Enter the starting page no : "))
for i in range(start, pages):
    page = pdfReader.getPage(i)
    text = " ".join(page.extractText().split())
    print("Pge no : " + str(i) + " " + text)
    speaker.say(text)
    speaker.runAndWait()
