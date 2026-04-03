from pypdf import PdfReader

def extract_text_with_metadata(file_path):
    reader = PdfReader(file_path)
    
    docs = []
    
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        
        if text:  # avoid None
            docs.append({
                "text": text,
                "page": i + 1
            })
    
    return docs