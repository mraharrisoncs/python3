# needs pip install python-pptx, see python-pptx.readthedocs.io
from pptx import Presentation

def extract_text(pptx_path):
    presentation = Presentation(pptx_path)
    extracted_text = ""
    for snum, slide in enumerate(presentation.slides):
        if slide.has_notes_slide:
            notes_text = slide.notes_slide.notes_text_frame.text
            extracted_text += f"\S{snum + 1}: {notes_text}"
    return extracted_text

def parse_for_timings(text):
    total = 0
    words = text.split()
    for index, word in enumerate(words):
        if "Timing" in word:
            try:
                num, unit = int(words[index + 1]), words[index + 2][0].lower()
                total += int(words[index + 1]) / (60 if unit == "s" else 1)
            except: # didn't find integers after "Timing" word
                pass
    return total

# MAIN PROGRAM
#pptx_path = 'datastruc2.pptx'
pptx_path = r"C:\Users\alan\OneDrive\#NCCE\AGCSEHub\Externals\ADS\Final Draft\Advanced Data Structures for A-level Computer Science Session 6.pptx"
text = extract_text(pptx_path)
duration = parse_for_timings(text)
print(f"Prez duration {duration:.2f} minutes")
