import time

import requests
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash, jsonify, Response
from flask_rq import RQ 
from werkzeug.serving import run_simple
#from flask.ext.rq import job, get_queue
import pprint
from jobs import *

app = Flask(__name__)
app.debug = True

rq = RQ(app)
tasks = {}


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/addjob',methods=['POST'])
def add_job():
    #q = get_queue()
    #q.enqueue(count_words_at_url, request.form['url'])
    #print dir(job)
    #print job.result
    tasks['task'] = count_words_at_url.delay(request.form['url'])
    print  tasks['task']
    return render_template('index.html')

@app.route('/api/check_job',methods=['GET'])
def check_job():
    return render_template('index.html')


if __name__ == '__main__':
    run_simple('localhost', 8000, app, use_reloader=True, use_debugger=True, use_evalex=True)


