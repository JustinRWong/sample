from flask import Flask, Response, request, abort, jsonify, render_template, make_response, session, redirect, url_for, flash, redirect
from flask_cors import CORS

from app import app
from routes_utils import *
from models.User import User

'''
App Routes
'''
@app.route('/', methods=['GET'])
def index():
    '''
    Returns all routes
    52bc79c3a5dd623e3da8087509bf1da828bf8de4
    '''
    get_links = []
    post_links = []
    all_endpoints = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            get_links.append((url, rule.endpoint))
        if "POST" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            post_links.append((url, rule.endpoint))
        all_endpoints.append(rule.endpoint)
    # links is now a list of url, endpoint tuples
    return render_template('site-map.html',    get_links=get_links,
                                        post_links=post_links,
                                        all_endpoints=all_endpoints,
                                        status='ALIVE',
                                        time=datetime.fromtimestamp(time.time()))
