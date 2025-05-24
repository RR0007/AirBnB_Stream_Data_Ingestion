import boto3
import json
import uuid
import random 

def generator():
    return {
            "bookingId": uuid.uuid1(),
            "userId": random.randint(100,999),
            "propertyId": random.randint(1000,99999),
            "location": random.choice(['dehradun, India', 'new York, US', 'London, UK', 'kpk, India']),
            "startDate": random.choice(["2024-03-12","2024-03-13","2024-03-14"]),
            "endDate": random.choice(["2024-03-13","2024-03-14","2024-03-15"]),
            "price": random.randint(100,999)
        }

def lambda_handler(event, context):
    body=generator()
    sqs=boto3.client('sqs')
    queue_url = "https://sqs.eu-north-1.amazonaws.com/304783065894/AirbnbBookingQueue"
    
    for i in range(0,5):
            sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=json.dumps(body)
            )
