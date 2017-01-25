from sklearn.externals import joblib
import pandas as pd

from flask import Flask, url_for, send_from_directory, request, jsonify
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import Resource
app = Flask(__name__)

float_cols = ['delivery_method', 'body_length', 'sale_duration'
    # 'duration', 'campaign', 'pdays', 'previous', 'emp.var.rate',
    # 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed',
]

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
    query_df = pd.DataFrame()
    parser = reqparse.RequestParser()
    for key in float_cols:
        parser.add_argument(key, type=float)
    args = parser.parse_args()
    for key in float_cols:
        query_df.loc[0, key] = args.get(key)

    colls = ['delivery_method', 'body_length', 'sale_duration']
    # multi_dict = request.args
    # print(multi_dict)
    # for key in multi_dict:
    #     print(key)
    #     # multi_dict.get(key)
    #     # multi_dict.getlist(key)
    #     # query_df[key] = query_df.index
    #     if key in ('delivery_method','body_length','sale_duration'):
    #         query_df.loc[0, key] = float(multi_dict.get(key))

    print(query_df.head())
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
    print(query_df.columns)
    p = clf.predict_proba(query_df[colls])[0, 1]
    l = float(p > 0.5)
    print(p)
    return jsonify({"sample_uuid":  args.get("sample_uuid"), "probability": p, "label": l})

    #return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    clf = joblib.load('filename2.pkl')
    app.run(host="0.0.0.0")
