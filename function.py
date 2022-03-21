from collections import Counter
text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
freq = Counter(text.split()).most_common()
print(freq)