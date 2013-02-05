import time

from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash, jsonify, Response
from flask.ext.rq import RQ
from werkzeug.serving import run_simple
from flask.ext.rq import job

app = Flask(__name__)
rq = RQ(app)

@job
def do_something(echo):
    time.sleep(1)
    return echo


@app.route('/')
def hello_world():
    return render_template('submit.html')

if __name__ == '__main__':
    run_simple('localhost', 8000, app, use_reloader=True, use_debugger=True, use_evalex=True)


