import json
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }

def lambda_dynamodb_handler(event, context):
    print(f"EVENT: {event}")
    for record in event['Records']:
        print(f"EVENT_ID: {record['eventID']}")
        print(f"EVENT_NAME: {record['eventName']}")
    print('Successfully processed %s records.' % str(len(event['Records'])))
