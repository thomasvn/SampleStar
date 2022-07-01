import flask

import os
import json
import random
import string
import datetime

################################################################################
# SETUP
################################################################################

# If the req2seq dictionary exists in the flat-file database, load it into memory
req2seq = {}
if os.path.exists('./db/requestId_to_sequenceId.json'):
    with open('./db/requestId_to_sequenceId.json', 'r') as f:
        req2seq = json.load(f)

# Start Flask app
app = flask.Flask(__name__)

################################################################################
# HELPER FUNCTIONS
################################################################################

def randomFloat():
    """Stub function that generates a pseudo-random float.

    It will eventually be replaced by a query to the hardware device which can
    generate genuinely random numbers.

    """

    return random.random()

def genSeqId():
    """Generate a pseudo-random id to associate with this generated sequence.
    """
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    seq_id = 'seq_' + x

    # If this seq_id already exists in db, try generating another seq_id
    if os.path.exists('./db/' + seq_id + '.json'):
        return(genSeqId())

    return seq_id

################################################################################
# ROUTES
################################################################################

@app.route('/')
def hello():
    return 'Welcome to SampleStar!'

@app.route('/api/randomSequence', methods=['POST'])
def randomSequence():
    """Request a new sequence of random numbers or an existing `sequenceId`.

    Params:
    * requestId:        string (alphanumerics and "_") to identify the request
    * sequenceLength:   requested amount of random numbers returned
    * tag:              string (alphanumerics and "_") with tag/description of 
                        this request

    Response:
    If the `requestId` received already exists, this response will have empty
    fields except for the `sequenceId`.
    {
        'dateProcessed': '',
        'randomSequence': [float],
        'request': {
            'requestId': '',
            'sequenceLength': '',
            'tag': ''
        },
        'sequenceId': ''
    }

    200: Ok
    400: Bad Request. Invalid input

    """

    response = {
        'dateProcessed': '',
        'randomSequence': [],
        'request': {
            'requestId': '',
            'sequenceLength': '',
            'tag': ''
        },
        'sequenceId': ''
    }

    # Parse Arguments
    requestId = flask.request.args['requestId']
    sequenceLength = flask.request.args['sequenceLength']
    tag = flask.request.args['tag']

    # Input sanitization
    if not requestId.isidentifier():
        return 'requestId is not an identifier (alphanumerics and _)', 400
    if not sequenceLength.isdigit():
        return 'sequenceLength is not a valid digit', 400
    if not tag.isidentifier():
        return 'tag is not an identifier (alphanumerics and _)', 400

    # If the requestId exists, return the sequenceId to the user
    if requestId in req2seq:
        response['sequenceId'] = req2seq[requestId]
        return response

    # If the requestId doesn't exist, return sequence of numbers and metadata
    # TODO: more metadata
    response['dateProcessed'] = str(datetime.datetime.now())
    for _ in range(int(sequenceLength)):
        response['randomSequence'].append(randomFloat())
    response['request']['requestId'] = requestId
    response['request']['sequenceLength'] = sequenceLength
    response['request']['tag'] = tag
    response['sequenceId'] = sequenceId = genSeqId()

    # Update our req2seq lookup dict
    req2seq[requestId] = sequenceId

    # Write output to database
    # TODO: What if the program crashes right here? Roll back?
    with open('./db/requestId_to_sequenceId.json', 'w') as f:
        json.dump(req2seq, f)
    with open('./db/' + sequenceId + '.json', 'w') as f:
        json.dump(response, f)

    # Send response to user
    return response

@app.route('/api/retrieveSequence', methods=['POST'])
def retrieveSequence():
    """Given a sequenceId, show the sequence and original request & reponse.

    Params:
    * sequenceId:   string (alphanumerics and "_") to identify the original
                    request

    Response:
    {
        'dateProcessed': '',
        'randomSequence': [float],
        'request': {
            'requestId': '',
            'sequenceLength': '',
            'tag': ''
        },
        'sequenceId': ''
    }

    200: Ok
    400: Bad Request. Invalid Input
    404: Not Found. Requested resource (`sequenceId`) doesn't exist

    """

    response = {
        'dateProcessed': '',
        'randomSequence': [],
        'request': {
            'requestId': '',
            'sequenceLength': '',
            'tag': ''
        },
        'sequenceId': ''
    }

    # Parse Arguments
    sequenceId = flask.request.args['sequenceId']
    
    # Input sanitization
    if not sequenceId.isidentifier():
        return 'sequenceId is not an identifier (alphanumerics and _)', 400

    # sequenceId does not exist in the database
    if not os.path.exists('./db/' + sequenceId + '.json'):
        return 'requested sequenceId does not exist', 404

    # Retrieve the original request
    with open('./db/' + sequenceId + '.json', 'r') as f:
        response = json.load(f)
    return response
