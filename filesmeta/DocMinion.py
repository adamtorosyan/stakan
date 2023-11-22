from docx import Document

try:
    import win32com.client

    MSWORD_INSTALLED = True
except ImportError:
    MSWORD_INSTALLED = False


class DocMinion:
    ex = ["doc", "docx"]

    def get_meta_inf(self, path):
        if path.endswith(".docx"):
            return self.extract_docx_metadata(path)
        elif path.endswith(".doc") and MSWORD_INSTALLED:
            return self.extract_doc_metadata(path)
        else:
            return {"error": "Unsupported file format or Microsoft Word not installed"}

    def extract_docx_metadata(self, path):
        try:
            doc = Document(path)
            metadata = {}

            metadata["Title"] = doc.core_properties.title
            metadata["Author"] = doc.core_properties.author
            metadata["Subject"] = doc.core_properties.subject
            metadata["Keywords"] = doc.core_properties.keywords
            metadata["Pages"] = len(doc.element.xpath("//w:sectPr"))

            return metadata
        except Exception as e:
            return {"error": str(e)}

    def extract_doc_metadata(self, path):
        if not MSWORD_INSTALLED:
            return {"error": "Microsoft Word is not installed for handling .doc files."}
        try:
            word = win32com.client.Dispatch("Word.Application")
            doc = word.Documents.Open(path)
            metadata = {}

            metadata["Title"] = doc.BuiltInDocumentProperties("Title").Value
            metadata["Author"] = doc.BuiltInDocumentProperties("Author").Value
            metadata["Subject"] = doc.BuiltInDocumentProperties("Subject").Value
            metadata["Keywords"] = doc.BuiltInDocumentProperties("Keywords").Value
            metadata["Pages"] = doc.ComputeStatistics(2)

            doc.Close()
            word.Quit()

            return metadata
        except Exception as e:
            return {"error": str(e)}
