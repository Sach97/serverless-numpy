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
    
    return {'statusCode': 201, 'body': l }

if __name__ == "__main__":
    main('', '')
