from PyPDF2 import PdfFileReader
import pyttsx3
import uuid

fol = None
starter = pyttsx3.init()
pk = uuid.uuid4()

def recog(path):
    f = open(path, 'rb')
    recog.pdf = PdfFileReader(f)

def num_pg():
    recog.pdf.getNumPages()



def read_selected_page(n):
    var = recog.pdf.getPage(n)
    v = var.extractText()
    save_as_audio(n)
    starter.runAndWait()


def save_as_audio(n):
    var = recog.pdf.getPage(n)
    v = var.extractText()
    if recog.pdf.getNumPages() == v:
        starter.save_to_file(v, 'Script.mp3')
    else:

        starter.save_to_file(v,f'{fol}/{pk}.mp3')


