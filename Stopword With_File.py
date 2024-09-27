import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
try:
    stop=set(stopwords.words("english"))
    filename=input("Please enyter existing .txt filename: ")
    file1=open(filename)
    line=file1.read().lower()
    words=line.split()
    for r in words:
        if not r in stop:
            appendFile=open("sample.txt","a")
            appendFile.write(r+" ")
            appendFile.close()
    print("Stopwords successfully removed")
except:
    print("The error occured")
