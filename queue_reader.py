import json
import boto3

def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='example_application_queue')
    client = boto3.client('sqs')
    response = client.receive_message(
        QueueUrl = queue.url,
        MaxNumberOfMessages=1
        )

    print(response['Messages'][0]['Body'])
    receipt_handle = response['Messages'][0]['ReceiptHandle']
    client.delete_message(
        QueueUrl = queue.url,
        ReceiptHandle = receipt_handle
        )
    return {
        'statusCode': 200,
        'body': response['Messages'][0]['Body']
    }

