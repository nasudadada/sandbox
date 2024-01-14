import json


def hello(event, context):
    body = {
        "body": "{\"message\": \"Hello World!\", \"input\": {}}",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
