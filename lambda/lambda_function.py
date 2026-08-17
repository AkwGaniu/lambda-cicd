import json

def lambda_function(event, context):
  # TODO implement
  return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda! \n I hope you are good today')
  }
