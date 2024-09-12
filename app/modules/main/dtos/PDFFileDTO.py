class PDFFileDTO:
    def __init__(self, pdf_file, filename):
        self.pdf_file = pdf_file
        self.filename = filename

    def to_dict(self):
        return {
            'pdf_file': self.pdf_file,  
            'filename': self.filename
        }
