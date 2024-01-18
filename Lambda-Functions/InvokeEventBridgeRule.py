import boto3
import json

def lambda_handler(event, context):
    event_bus_name = "default"  # Replace if using a custom event bus
    event_detail = {
        "detail-type": "ManualTrigger",  # Customize as needed
        "source": "my-lambda-function",
        "message": "Manually triggered event"
    }
    
    json_string = json.dumps(event_detail)

    client = boto3.client('events')
    response = client.put_events(
        Entries=[
            {
                "Source": "my-lambda-function",
                "DetailType": "ManualTrigger",
                "Detail": json_string,
                "EventBusName": event_bus_name
            }
        ]
    )

    return {
        'statusCode': 200,
        'body': response
    }
