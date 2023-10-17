import fitz  # PyMuPDF library


class PDFMinion:
    ex = ["pdf"]

    def get_meta_inf(self, path):
        try:
            pdf_document = fitz.open(path)  # type: ignore
            num_pages = pdf_document.page_count
            pdf_document.close()

            metadata = {"Pages": num_pages}
            return metadata
        except Exception as e:
            return {"error": str(e)}
