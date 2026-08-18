import json

def lambda_handler(event, context):
  # TODO implement
  return {
    'statusCode': 200,
    'body': json.dumps('Hello Lambda! Hopefully you get this greeting from VS Code.')
  }
