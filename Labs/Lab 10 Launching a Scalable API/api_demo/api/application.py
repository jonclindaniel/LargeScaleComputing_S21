from flask import Flask, render_template, jsonify
import boto3

# Create an instance of Flask class (represents our application)
# Pass in name of application's module (__name__ evaluates to current module name)
app = Flask(__name__)
application = app # AWS EB requires it to be called "application"

# on EC2, needs to know region name as well; no config
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('books')

# Provide a landing page with some documentation on how to use API
@app.route("/")
def home():
    return render_template('index.html')

# Get items from DynamoDB `books` table
# Can provide additional API functionality with more complicated SQL queries
@app.route("/api/isbn:<isbn>")
def isbn(isbn):
    response = table.get_item(Key={'isbn': str(isbn)})
    return jsonify(response['Item'])

if __name__ == "__main__":
    application.run()
