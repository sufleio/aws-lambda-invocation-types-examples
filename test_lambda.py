import boto3, json
import argparse
import pprint

def invoke_syncronous():
    if args.payload:
        with open(args.payload, 'rb') as f:
	        payload = f.read()
    else:
        payloadStr = json.dumps(args.payload)
        payload = bytes(payloadStr, encoding='utf8')
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName=args.name,
        InvocationType="RequestResponse",
        Payload=payload
    )
    return response

def invoke_asyncronous():
    payloadStr = json.dumps(args.payload)
    payload = bytes(payloadStr, encoding='utf8')
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName=args.name,
        InvocationType="Event",
        Payload=payload
    )

    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--type', type=str, required=True)
    parser.add_argument('--payload', type=str, required=False)
    args = parser.parse_args()

    pp = pprint.PrettyPrinter()

    if  args.name == None:
        raise Exception('ERROR: name parameter cannot be NULL')
    if  args.name == None:
        raise Exception('ERROR: type parameter cannot be NULL')
    
    if args.type == 'sync':
        pp.pprint(invoke_syncronous())
    elif args.type == 'async' :
        pp.pprint(invoke_asyncronous())
    else:
        raise ValueError("Invalid argument. You must choise 'sync' or async")
