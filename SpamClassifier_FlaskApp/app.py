from flask import Flask,render_template,url_for,request
import pickle
from sklearn.feature_extraction.text import CountVectorizer
# import joblib
from preprocess import Preprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():
    # loading the model inference and count vectoriser intference
    # NB_spam_model = open('NB_spam_model.pkl','rb')
    # load pickle
    cv = pickle.load(open("cv.pickel", "rb"))
    clf = pickle.load(open("NB_spam_model.pickel", "rb"))
    print("cv object cretaed")
    # clf = joblib.load(NB_spam_model)

    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        # print(data)
        # print(type(data))
        msg = Preprocess(data)
        print("msg", msg)
        msg = cv.transform(msg).toarray()
        my_prediction = clf.predict(msg)
        print(my_prediction, "final prediction")

    return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
    app.run(debug=True)