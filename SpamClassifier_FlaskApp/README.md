# Flask App to classify Spam messages

## Deployment pipeline architecture

<img width="1152" alt="Screenshot 2020-10-07 at 11 38 52 PM" src="https://user-images.githubusercontent.com/25937235/95514656-ee918700-09d9-11eb-9af8-358171311689.png">


## Details of the files used to create this APP :

    1. training.ipynb : Juputer notebook which is used to train the spam Vs ham messages using Naive Bayes.
    2. spam.csv : Training Data
    3. NB_spam_model.pickel : Model inference
    4. cv.pickel : Count vectorizer inference
    5. app.py : Main Flask app file
    6. preprocess.py : File called my app.py to do all preprocessing
    7. static : Contains style.css to give basic style to html page
    8. templates : Consists :-
        1. home.html -  Main home page where user can write the message which he wants to classify. It will call the predict function from app.py to do the prediction.
        2. result.html - File which is used to give the output, it get the result from the app.py.
