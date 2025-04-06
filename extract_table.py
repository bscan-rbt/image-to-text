from img2table.document import Image
from img2table.ocr import EasyOCR



def convert_image(src_path: str, dest_path: str):
    image = Image(src=src_path)
    reader = EasyOCR(['en'])

    image.to_xlsx(dest_path, ocr= reader, borderless_tables= True, min_confidence=10)

