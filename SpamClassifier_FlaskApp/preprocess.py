import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def Preprocess(message):
    print("Preprocess Started")
    corpus = []
    msg = re.sub('[^a-zA-Z]', ' ', message[0])
    msg = msg.lower()
    msg = msg.split()
    msg = [lemmatizer.lemmatize(word)  for word in msg if not word in stopwords.words('english')]
    msg = ' '.join(msg)
    corpus.append(msg)
    print("Corpus",corpus)
    print("Message Joined")
    print(type(corpus))
    # print(type(corpus))
    return corpus


