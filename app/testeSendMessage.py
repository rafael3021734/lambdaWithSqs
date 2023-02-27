import boto3
sqs = boto3.resource('sqs')
queue = sqs.Queue(url='http://192.168.99.100:4566/000000000000/localstack')
client = boto3.client('sqs')

def create_sqs(name, attributes):
    sqs.create_queue(QueueName=name, Attributes=attributes)


def send_messages_to_sqs(name, message):
    queue = sqs.get_queue_by_name(QueueName='localstack')
    client.send_message(QueueUrl='queue', MessageBody=message)

if __name__ == '__main__':

    attributes = {
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '600'
    }

    #create_sqs('sqs_messages', attributes)

    send_messages_to_sqs('sqs_messages', "Hello, SQS!")