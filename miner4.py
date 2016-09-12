import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(pdfpath,txtpath):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(pdfpath, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    text_file = open(txtpath, "w")
    text_file.write(text)
    text_file.close()

#convert_pdf_to_txt('sample.pdf','sample3.txt')

for fn in os.listdir('.'):
     filename, file_extension = os.path.splitext(fn)
     if os.path.isfile(fn) and file_extension=='.pdf':
        print (filename)
        convert_pdf_to_txt(filename+'.pdf', filename+'.txt')