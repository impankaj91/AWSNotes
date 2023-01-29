def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']
    response = event['Records'][0]['cf']['response']

    if response['status'] == '403':
        response['status'] = 302
        response['statusDescription'] = 'Found'
        response['headers']['location'] = [            {                'key': 'Location',                'value': request['uri'],
            }
        ]

    return response
