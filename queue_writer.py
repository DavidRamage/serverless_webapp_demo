import json
import boto3

def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='example_application_queue')
    client = boto3.client('sqs')
    print(event)
    client.send_message(QueueUrl = queue.url, MessageBody = event['body'])
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully wrote to queue.')

    }

