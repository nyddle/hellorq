import time

import requests
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash, jsonify, Response
from flask_rq import RQ
from rq.job import Job
from rq import use_connection
from rq.connections import Connection
from flask_rq import get_worker
from werkzeug.serving import run_simple
#from flask.ext.rq import job, get_queue
import pprint
from jobs import count_words_at_url

use_connection()
job = Job()
job = job.fetch('e73ea52a-0171-4548-97b5-4c6bd862b8c1')
print job
print job.result

