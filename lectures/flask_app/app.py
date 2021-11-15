import logging
import os

import requests
import io

from minio import Minio
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def read_root():
    return jsonify('hello world')


def _save_to_bucket():
    minio_access_key = os.getenv("MINIO_ACCESS_KEY", '')
    minio_secret_key = os.getenv("MINIO_SECRET_KEY", '')

    client = Minio(
        "s3:9000",
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False,
    )

    response = requests.get('https://poloniex.com/public?command=returnTradeHistory&currencyPair=USDT_BTC')
    raw_json = str(response.json()).encode('utf-8')
    bytes_json = io.BytesIO(raw_json)

    if client.bucket_exists('testbucket'):
        logging.info('bucket exists')
    else:
        logging.warning('bucket doesn\'t exist, create new one')
        client.make_bucket('testbucket')

    client.put_object('testbucket',
                      'data.json',
                      data=bytes_json,
                      length=bytes_json.getbuffer().nbytes,
                      content_type='application/json')

    return '200'


@app.get("/crypto")
def get_crypto():
    return _save_to_bucket()
