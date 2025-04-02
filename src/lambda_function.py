def lambda_handler(event, context):
    print("Hello from Lambda! in ci cd!")
    return {
        'statusCode': 200,
        'body': 'Hello from your Lambda Function!'
    }