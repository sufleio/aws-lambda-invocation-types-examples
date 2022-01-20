This example contains the different ways to invoke AWS Lambda functions with using Python and boto3.
You can check out the blog post about this project at https://www.sufle.io/blog/lambda-invocation-types

## Requirements
- python >= 3.7
- pip

## Installation
After cloning the project, in the main directory:
- `virtualenv -p python3 venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## Example Usage
To perform a synchronous invocation, run the command below;
```bash
python test_lambda.py --name <your-function-name> --type sync
```
For asynchronous invocation;
```bash
python test_lambda.py --name <your-function-name> --type async
```
For event-source mapping with DynamoDB Streams, run;
```bash
python test_lambda.py --name <your-dynamodb-streams-function-name> --payload records.json --type sync
```