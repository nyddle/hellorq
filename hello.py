import time

import requests
import redis
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash, jsonify, Response
from flask_rq import RQ
from rq.job import Job
from rq import use_connection
from flask_rq import get_worker
from werkzeug.serving import run_simple
#from flask.ext.rq import job, get_queue
import pprint
from jobs import count_words_at_url

app = Flask(__name__)
app.debug = True

RQ(app)

connection = redis.StrictRedis()
print connection

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/addjob',methods=['POST'])
def add_job():
    #print job.result
    print request.form['url']
    task = count_words_at_url.delay(request.form['url'])
    return jsonify({'job_id' : task._id})


@app.route('/api/check_job',methods=['GET'])
def check_job():
    return render_template('index.html')

@app.route('/get/<jobid>')
def getjob(jobid):
    use_connection()
    job = Job()
    job = job.fetch(jobid)
    return str(job.result)


if __name__ == '__main__':
    run_simple('localhost', 8000, app, use_reloader=True, use_debugger=True, use_evalex=True)


