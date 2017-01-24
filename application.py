import json
from sklearn.externals import joblib

from flask import Flask, url_for, send_from_directory, request
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


@app.route('/api/v1/predict')
def api_v1_predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    query = pd.get_dummies(query_df)
    prediction = clf.predict(query)
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    clf = joblib.load('filename.pkl')
    app.run(host="0.0.0.0")
