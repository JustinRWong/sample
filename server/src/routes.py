from flask import Flask, Response, request, abort, jsonify, render_template, make_response, session, redirect, url_for, flash, redirect
from flask_cors import CORS

from app import app
from routes_utils import *

'''
DEMO Routes
'''
@app.route('/', methods=['GET'])
def demo():
    return render_template('demo.html',
                            ENV=app.config.get('ENV')
                            )

@app.route('/finish_order')
def finish_order():
    return render_template('finish_order.html',
                            ENV=app.config.get('ENV')
                            )
