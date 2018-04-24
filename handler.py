import numpy as np
import json
import logging

logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)

def main(event, context):

    logger.info('Event : {}'.format(event))
    logger.info('Event a : {}'.format(event['a']))
    
    event_a = event['a']
    event_b = event['b']
    event_c = event['c']
    array = np.arange(event_a).reshape(event_b, event_c)
    l = array.tolist()
    
    return {'statusCode': 201,
                'body': l }
        
    # if event.get('httpMethod') == 'POST' and event.get('body'):
    #     logger.info('Message received')
    #     data = json.loads(event.get('body'))
    # data = json.loads(event['body'])
    #if 'a' not in data or 'b' not in data:
    #     logging.error('Validation Failed')
    #     return {'statusCode': 422,
    #             'body': json.dumps({'error_message': 'Couldn\'t find a nor b'})}

    # if not data['text']:
    #     logging.error('Validation Failed - a or b was empty. %s', data)
    #     return {'statusCode': 422,
    #             'body': json.dumps({'error_message': 'Couldn\'t create the array item. As a or b was empty.'})}
    


if __name__ == "__main__":
    main('', '')