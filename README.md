# Serverless-CRUD-Flask-APP
Simple fully managed CRUD Flask API server using AWS API Gateway, Lambda, S3 and Flask. Also it include an infrastructure deployment by serverless framework.

## Tools & Packages

* [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [AWS S3](https://aws.amazon.com/s3/)
* [serverless](https://serverless.com/) 3.32.2 (npm package)
* [serverless-wsgi](https://github.com/logandk/serverless-wsgi) 3.0.2
* [serverless-python-requirements](https://github.com/UnitedIncome/serverless-python-requirements) 6.0.0
* [Flask](http://flask.pocoo.org/) 2.3.2 (API server)
* Python 3.10
* aws-cli 2.12.0
* node v9.6.7

## Prerequisite

* node.js (npm) greater than or equal to v4
* aws account
* awscli

## Running in local mode

```
# Download source
export mode=local

python -m virtualenv venv
venv/bin/pip install -r requirements.txt
venv/bin/python src/app.py
```

## Setup & Deploy   

```
# Download source
git clone git@github.com:GabrielCasemiro/Serverless-CRUD-Flask-App.git
cd Serveless-Flask-Sample-API

# Install serverless globally
npm install serverless -g

# Deploy to aws
serverless deploy

# Remove deployed resources
serverless remove
```

## API usage
After the deploy, you will receive the URL of your function on your terminal. For example:
<https://jjxxxx.execute-api.us-east-1.amazonaws.com/dev/>

Copy and use the url to make requests.
