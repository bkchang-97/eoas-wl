"""
* get submissions

"""
from canvasapi import Canvas
import pdb
import json
from pathlib import Path
import os

import requests
import logging
import json

def flatten(module_list):
    """
    Given a list of modules return a list of dictionaries of all module items
    """
    outlist=dict()
    for module in module_list:
        outlist[module.id]=dict(name=module.name,items=[])
        items=module.get_module_items()
        for an_item in items:
            outlist[module.id]['items'].append(json.loads(an_item.to_json()))
    return outlist

in_file='sandbox.json'
full_path = Path(__file__).resolve().parent / Path(in_file)
with open(full_path,'r') as f:
    box_dict=json.load(f)

debug=False    
if debug:
    # Enabling debugging at http.client level (requests->urllib3->http.client)
    # you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # the only thing missing will be the response.body which is not logged.
    from http.client import HTTPConnection
    HTTPConnection.debuglevel = 1

    logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
#
# get the canvas api token
#
my_home=Path(os.environ['HOME'])
full_path=my_home / Path('.canvas.json')
with open(full_path,'r') as f:
    secret_dict=json.load(f)
token=secret_dict['token']
#
# set up short names for canvas courses
#
API_URL = "https://canvas.ubc.ca"
# Canvas API key
API_KEY = token
nicknames={'a301':'ATSC 301 Atmospheric Radiation and Remote Sensing',
           'e340':'EOSC 340 101 Global Climate Change',
           'box':'Philip_Sandbox'}
#
# get the courses and make a dictionary of coursename,id values
#
canvas = Canvas(API_URL, API_KEY)
courses=canvas.get_courses()
keep=dict()
for item in courses:
    for shortname,longname in nicknames.items():
        if item.name.find(longname) > -1:
            keep[shortname]=item.id
#
# find all modules in cource
#
course_name='box'
course=canvas.get_course(keep[course_name])
modules=course.get_modules()
module_list=flatten(modules)

submissions=course.get_multiple_submissions(student_ids='all')
print(list(submissions))

    
#
# change the module name and write back tuo canvas
#
# print(f'found module: {assign_module}')
# assign_module.edit(module={'name':'assignphaVV','published':True})
# new_module=course.get_module(assign_module.id)
# star10='*'*10
# print(f'\n{star10}\nchanged module name to {new_module.name}\n{star10}\n')
# all_items=list(new_module.get_module_items())
# out=dict(courseid=course.id,moduleid=assign_module.id)
#pdb.set_trace()










