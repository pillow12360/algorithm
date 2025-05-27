import re

text = "raindroprain"
print(re.search(r"rain", text))

text = text.replace('r','c')
print(text)