from sklearn.externals import joblib
import pandas as pd

from flask import Flask, url_for, send_from_directory, request, jsonify
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
    colls = ['delivery_method', 'body_length', 'sale_duration']
    query_df = pd.DataFrame()
    multi_dict = request.args
    for key in multi_dict:
        # multi_dict.get(key)
        # multi_dict.getlist(key)
        # query_df[key] = query_df.index
        if key in ('delivery_method','body_length','sale_duration'):
            query_df.loc[0, key] = float(multi_dict.get(key))

    # print(query_df.dtypes)
    # p = clf.predict_proba(query_df[colls])[0, 1]
    # l = float(p > 0.5)
    # print(p)

    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # # prediction = clf.predict(query_df)
    # query_df = pd.DataFrame()
    # query_df.loc[0, 'delivery_method'] = 1.0
    # query_df.loc[0, 'body_length'] = 2113
    # query_df.loc[0, 'sale_duration'] = 16.0
    # print(query_df.dtypes)
    # # print(prediction.item(0))
    print(query_df.collumns)
    p = clf.predict_proba(query_df[colls])[0, 1]
    l = float(p > 0.5)
    print(p)
    return jsonify({"sample_uuid":  multi_dict.get("sample_uuid"), "probability": p, "label": l})

    #return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    clf = joblib.load('filename2.pkl')
    app.run(host="0.0.0.0")
