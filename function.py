def lambda_handler(event, context, callback):
    # Get the original URL that the user requested
    requested_url = event['Records'][0]['cf']['request']['uri']
  
    # Redirect the user to the original URL
    response = {
        'status': '302',
        'statusDescription': 'Found',
        'headers': {
            'location': [{
                'key': 'Location',
                'value': requested_url
            }]
        }
    }
    callback(None, response)
