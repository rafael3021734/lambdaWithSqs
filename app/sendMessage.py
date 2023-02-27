# Get the service resource
import boto3

sqs = boto3.resource('sqs')
queue = sqs.Queue(url='http://192.168.99.100:4566/000000000000/localstack')
print(queue)
# Get the queue
#queue = sqs.get_queue_by_name(QueueName='localstack')



# Create a new message
#response = queue.send_message(MessageBody='world')

# create messages with custom attributes
response = queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Daniel',
        'DataType': 'String'
    }
})
print(queue)

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))