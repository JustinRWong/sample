from flask import Blueprint, request, render_template, Response
from flask_cors import cross_origin
import json, time
from datetime import datetime

path_blueprint = Blueprint('path', __name__, template_folder='templates')

@path_blueprint.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

@path_blueprint.route('/', methods=['GET', 'POST'])
def path_status():
    json_resp = {"Status": "ALIVE", "Time": time.time()}
    return json.dumps(json_resp)

@path_blueprint.route('/__healthcheck__', methods=['GET', 'POST'])
def health_check():
    '''
    Health check responds for GET and POST
    GET: returns time time of server receiving request.
    POST: echos parameters and data passeed by request.
    '''
    ## Query parameter argumeents
    query_string_params = request.args

    ## data parameters from http request application/json
    application_json_params = request.get_json()


    if request.method == 'GET':
        posted = {  'query_params': query_string_params,
                    'application/json_data': application_json_params}
        return render_template( 'healthcheck.html',
                                title='Healthcheck',
                                ttr={'time of response': time.time(), 'date': datetime.now()},
                                echo=posted)

    if request.method == 'POST':
        ## from form on html page for POST
        html_form_params = request.form['form_param']
        posted = {  'query_params': query_string_params,
                    'application/json_data': application_json_params,
                    'html_form_data': html_form_params}
        return render_template( 'healthcheck.html',
                                title='Healthcheck',
                                ttr={'time of response': time.time(), 'date': datetime.now()},
                                echo=posted)
