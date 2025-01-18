import pypdf as p

reader = p.PdfReader("prez.pdf")
text = ''
for page in reader.pages:
    text += page.extract_text() + "\n"
    
total = 0
words = text.split()
for index, word in enumerate(words):
    if "Timing" in word:
        try:
            num, unit = int(words[index + 1]), words[index + 2][0].lower()
            total += int(words[index + 1]) / (60 if unit == "s" else 1)
        except: # 'Timing' might be on the slide!
            pass
  
print(f"Prez duration {total:.2f} minutes")

