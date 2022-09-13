#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_lis', strict_slashes=False)
def states_list():
    """ State list """
    all_states = storage.all('States')
    all_states = [state for state in all_states.values()]
    return(render_template('7-states_list.html', all_states=all_states))


@app.teardown_appcontext
def teardown(self):
    """ Method to handle """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
