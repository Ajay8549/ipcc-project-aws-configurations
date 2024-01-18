import json
import requests

def lambda_handler(event, context):
    jenkins_url = "http://<jenkins-ec2-instance-ip>:<jenkins-port>"
    username = "<your-jenkins-user-name>"
    token = "<token-generated-in-jenkins>"
    job_name = "<your-pipeline-job-name>"
    
    auth = requests.auth.HTTPBasicAuth(username, token)
    build_url = f"{jenkins_url}/job/{job_name}/build?token={token}"
    
    response = requests.post(build_url, auth=auth)
    
    if response.status_code == 201:
        print("Jenkins job triggered successfully!")
    else:
        print("Failed to trigger Jenkins job. Response:", response.text)
    
    return {
        'statusCode': 200,
        'body': 'Jenkins job trigger attempt complete'
    }
