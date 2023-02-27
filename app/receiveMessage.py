import boto3

# Create SQS client
sqs = boto3.client('sqs')
sqs_client = boto3.client(
            'sqs',endpoint_url="http://192.168.99.100:4566",
#            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name='us-east-1')

#queue_url = 'https://sqs.sa-east-1.amazonaws.com/333273817192/test'
queue_url = 'http://192.168.99.100:4566/000000000000/localstack'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
print('Received and deleted message: %s' % message)