import time

import requests
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash, jsonify, Response
from flask_rq import RQ 
from flask_rq import get_worker
from werkzeug.serving import run_simple
#from flask.ext.rq import job, get_queue
import pprint
from jobs import *
# Creates a worker that handle jobs in ``default`` queue.

app = Flask(__name__)
app.debug = True

RQ(app)



tasks = {}


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/addjob',methods=['POST'])
def add_job():
    #print job.result
    print request.form['url']
    task = count_words_at_url.delay(request.form['url'])
    tasks[task._id] = task
    return jsonify({'job_id' : task._id})


@app.route('/api/check_job',methods=['GET'])
def check_job():
    return render_template('index.html')



if __name__ == '__main__':
    run_simple('localhost', 8000, app, use_reloader=True, use_debugger=True, use_evalex=True)

