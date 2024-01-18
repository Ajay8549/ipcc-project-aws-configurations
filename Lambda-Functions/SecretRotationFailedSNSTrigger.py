import json
import boto3

def lambda_handler(event, context):
    sns_arn = "<target-sns-topic-arn>"
    sns_client = boto3.client('sns')
    
    event_log = json.dumps(event)
    log_dict = json.loads(event_log)
    
    salutation = "Dear Subscriber,"
    line_1 = "Notification received through " + log_dict['detail-type'] + " :"
    line_2 = log_dict['detail']['eventName'] + " event encountered during RDS instance secret rotation"
    line_3 = "Error : " + log_dict['detail']['errorMessage']
    
    strings = [salutation, line_1, line_2, line_3]
    msg = "\n".join(strings)
    
    # print(msg)
    
    response = sns_client.publish(
        TargetArn=sns_arn, 
        Message=msg, 
        Subject="RDS Instance Secret Rotation Failed for IPCC Project"
    )
    return {
        'statusCode': 200,
        'body': 'SNS  trigger attempt complete'
    }

