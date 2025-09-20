from collections import Counter
text = """    
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
text.strip()
text = text.lower()
text = text.replace("!", ".")
text1 = text.split('.')
p1 = text1[0].strip()
p2 = text1[1].strip()
p3 = text1[2].strip()
wl = p1.split(' ')
cpython = wl.count('python')
print(p1.startswith('python', p1.endswith('python')))
print(len(text), text.count('a'), text.find('data'))
d = p1 + p2 + p3
d1 = '-'.join(p1 + p2 + p3)
print(d1)
print(Counter(d))
text = p1 + p2 + p3
def clean_text(text):
    text = text.replace('.', ' ').replace('.', ' ').replace(',', ' ')
    text = text.strip()
    text = text.lower()
    return text
print(clean_text(text))
