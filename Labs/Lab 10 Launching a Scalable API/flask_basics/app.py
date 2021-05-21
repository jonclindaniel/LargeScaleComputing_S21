'''
Run application with `python app.py` or `flask run` command
in terminal window
'''
from flask import Flask, render_template
import numpy as np

# Create an instance of Flask class (represents our application)
# Pass in name of application's module (__name__ evaluates to current module name)
app = Flask(__name__)

# Define Python functions that will be triggered if we go to defined URL paths
# Anything we `return` is rendered in our browser as HTML by default
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# We're not limited to short HTML phrases or a single URL path:
@app.route("/scores")
def scores():
    student = {'name': 'Jon'}
    assignments = [
        {
            'name': 'A1',
            'score': 89
        },
        {
            'name': 'A2',
            'score': 82
        },
        {
            'name': 'A3',
            'score': 95
        }
    ]

    # Compute the average score:
    avg = np.mean([assignment['score'] for assignment in assignments])

    # Render results using HTML template (Flask automatically looks
    # for HTML templates in app/templates/ directory)
    return render_template('scores.html',
                            student=student,
                            assignments=assignments,
                            avg=avg)

# We can also run arbitrary Python code and return the results
# of our computations:
@app.route("/random")
def random():
    ran = np.random.randint(1, 10)
    return "<p>Your random number is {}</p>".format(ran)

# And return results of computations based on user-defined input:
@app.route("/num_chars/<word>")
def num_chars(word):
    return "<p> There are {} characters in {} </p>".format(len(word), word)

if __name__ == "__main__":
    app.run() # allows us to run app via `python app.py`
