import time

import requests
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash, jsonify, Response
from flask.ext.rq import RQ
from werkzeug.serving import run_simple
from flask.ext.rq import job

app = Flask(__name__)
rq = RQ(app)


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


@job
def do_something(echo):
    time.sleep(1)
    return echo


@app.route('/')
def hello_world():
    return render_template('submit.html')

@app.route('/api/addjob',methods=['POST'])
def add_job():
    rq.enque(count_words_at_url, request.form['url'])
    return 'job added'

@app.route('/api/check_job',methods=['GET'])
def add_job():
    return render_template('submit.html')


if __name__ == '__main__':
    run_simple('localhost', 8000, app, use_reloader=True, use_debugger=True, use_evalex=True)


