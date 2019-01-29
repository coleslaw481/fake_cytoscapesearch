# -*- coding: utf-8 -*-

"""Top-level package for fake_cytoscapesearch."""

__author__ = """Chris Churas"""
__email__ = 'churas.camera@gmail.com'
__version__ = '0.0.1'

from datetime import datetime

import random
import os
import uuid
import flask
from flask import Flask, jsonify, request
from flask_restplus import reqparse, Api, Resource, fields, marshal
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


desc = """Fake cytoscape search service
 
 # THIS IS A FAKE SERVICE WITH RANDOM RESULTS YOU HAVE BEEN WARNED!!!!!

 
 **NOTE:** This service is experimental. The interface is subject to change.

https://docs.google.com/document/d/1Z1KCs--XFWQc4o22RxsEaB5nvCotH1duX9cj-OV1zcM/edit 
""" # noqa


random.seed(os.urandom(16))
CYTOSEARCH_REST_SETTINGS_ENV = 'CYTOSEARCH_REST_SETTINGS'
# global api object
app = Flask(__name__)

JOB_PATH_KEY = 'JOB_PATH'
WAIT_COUNT_KEY = 'WAIT_COUNT'
SLEEP_TIME_KEY = 'SLEEP_TIME'
DEFAULT_RATE_LIMIT_KEY = 'DEFAULT_RATE_LIMIT'

app.config[JOB_PATH_KEY] = '/tmp'
app.config[WAIT_COUNT_KEY] = 60
app.config[SLEEP_TIME_KEY] = 10
app.config[DEFAULT_RATE_LIMIT_KEY] = '360 per hour'

app.config.from_envvar(CYTOSEARCH_REST_SETTINGS_ENV, silent=True)

LOCATION = 'Location'
CYTOSEARCH_NS = 'cytoscapesearch'


api = Api(app, version=str(__version__),
          title='Fake Cytoscape Search ',
          description=desc, example='put example here')

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=[app.config[DEFAULT_RATE_LIMIT_KEY]],
    headers_enabled=True
)
for handler in app.logger.handlers:
    limiter.logger.addHandler(handler)

# need to clear out the default namespace
api.namespaces.clear()

ns = api.namespace(CYTOSEARCH_NS,
                   description='Fake Cytoscape Search Service')

app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

FAKE_CX = [{'numberVerification': [{'longNumber': 281474976710655}]}, {'metaData': [{'consistencyGroup': 1, 'elementCount': 1, 'lastUpdate': 1504297829644, 'name': 'ndexStatus', 'properties': [], 'version': '1.0'}, {'consistencyGroup': 1, 'elementCount': 1, 'lastUpdate': 1504297829657, 'name': 'provenanceHistory', 'properties': [], 'version': '1.0'}, {'consistencyGroup': 1, 'elementCount': 2, 'idCounter': 5, 'name': 'nodes'}, {'consistencyGroup': 1, 'elementCount': 1, 'idCounter': 5, 'name': 'edges'}, {'consistencyGroup': 1, 'elementCount': 1, 'idCounter': 5, 'name': 'supports'}, {'consistencyGroup': 1, 'elementCount': 1, 'idCounter': 5, 'name': 'citations'}, {'consistencyGroup': 1, 'elementCount': 9, 'idCounter': 5, 'name': 'edgeAttributes'}, {'consistencyGroup': 1, 'elementCount': 1, 'idCounter': 5, 'name': 'edgeSupports'}, {'consistencyGroup': 1, 'elementCount': 2, 'idCounter': 5, 'name': 'networkAttributes'}, {'consistencyGroup': 1, 'elementCount': 4, 'idCounter': 5, 'name': 'nodeAttributes'}]}, {'ndexStatus': [{'externalId': '653a65b2-8f54-11e7-a10d-0ac135e8bacf', 'creationTime': 1504297829644, 'modificationTime': 1504297829644, 'visibility': 'PRIVATE', 'published': False, 'nodeCount': 2, 'edgeCount': 1, 'owner': 'bgyori', 'ndexServerURI': 'http://public.ndexbio.org', 'readOnly': False}]}, {'provenanceHistory': [{'entity': {'uri': 'http://public.ndexbio.org/v2/network/653a65b2-8f54-11e7-a10d-0ac135e8bacf/summary', 'creationEvent': {'startedAtTime': 1504297829644, 'endedAtTime': 1504297829644, 'eventType': 'Program Upload in CX', 'inputs': None, 'properties': [{'name': 'user', 'value': 'Benjamin Gyori'}, {'name': 'user name', 'value': 'bgyori'}]}, 'properties': [{'name': 'edge count', 'value': '1'}, {'name': 'node count', 'value': '2'}, {'name': 'dc:title', 'value': 'indra_assembled'}]}}]}, {'nodes': [{'@id': 0, 'n': 'MEK'}, {'@id': 1, 'n': 'ERK'}]}, {'edges': [{'@id': 2, 's': 0, 't': 1, 'i': 'Phosphorylation'}]}, {'supports': [{'text': 'MEK phosphorylates ERK', 'citation': None, '@id': 4, 'attributes': []}]}, {'citations': [{'@id': 3, 'dc:title': None, 'dc:contributor': None, 'dc:identifier': 'pmid:19760502', 'dc:type': None, 'dc:description': None, 'attributes': []}]}, {'edgeAttributes': [{'po': 2, 'n': 'INDRA statement', 'v': 'Phosphorylation(MEK(), ERK())'}, {'po': 2, 'n': 'INDRA json', 'v': '{"type": "Phosphorylation", "enz": {"name": "MEK", "db_refs": {"BE": "MEK", "TEXT": "MEK"}, "sbo_definition": "http://identifiers.org/sbo/SBO:0000460"}, "sub": {"name": "ERK", "db_refs": {"BE": "ERK", "TEXT": "ERK"}, "sbo_definition": "http://identifiers.org/sbo/SBO:0000015"}, "evidence": [{"source_api": "reach", "pmid": "19760502", "text": "MEK phosphorylates ERK", "annotations": {"found_by": "Phosphorylation_syntax_1a_verb"}, "epistemics": {"section_type": null, "direct": true}}], "id": "364e57c7-9768-43ea-8ce8-cfd65212aff0", "sbo_definition": "http://identifiers.org/sbo/SBO:0000216"}'}, {'po': 2, 'n': 'type', 'v': 'Modification'}, {'po': 2, 'n': 'polarity', 'v': 'positive'}, {'po': 2, 'n': 'ndex:citation', 'v': ['pmid:19760502'], 'd': 'list_of_string'}, {'po': 2, 'n': 'Belief score', 'v': '1.00'}, {'po': 2, 'n': 'Text', 'v': 'MEK phosphorylates ERK'}, {'po': 2, 'n': 'indra', 'v': ''}, {'po': 2, 'n': 'supportType', 'v': 'literature'}]}, {'edgeSupports': [{'po': [2], 'supports': [4]}]}, {'networkAttributes': [{'n': 'name', 'v': 'indra_assembled'}, {'n': 'description', 'v': ''}]}, {'nodeAttributes': [{'po': 0, 'n': 'type', 'v': 'proteinfamily'}, {'po': 0, 'n': 'BE', 'v': 'http://sorger.med.harvard.edu/indra/entities/MEK'}, {'po': 1, 'n': 'type', 'v': 'proteinfamily'}, {'po': 1, 'n': 'BE', 'v': 'http://sorger.med.harvard.edu/indra/entities/ERK'}]}, {'status': [{'error': '', 'success': True}]}]

ERROR_RESP = api.model('ErrorResponseSchema', {
    'errorCode': fields.String(description='Error code to help identify issue'),
    'message': fields.String(description='Human readable description of error'),
    'description': fields.String(description='More detailed description of error'),
    'stackTrace': fields.String(description='stack trace of error'),
    'threadId': fields.String(description='Id of thread running process'),
    'timeStamp': fields.String(description='UTC Time stamp in YYYY-MM-DDTHH:MM.S')
})

TOO_MANY_REQUESTS = api.model('TooManyRequestsSchema', {
    'message': fields.String(description='Contains detailed message about exceeding request limits')
})

RATE_LIMIT_HEADERS = {
 'x-ratelimit-limit': 'Request rate limit',
 'x-ratelimit-remaining': 'Number of requests remaining',
 'x-ratelimit-reset': 'Request rate limit reset time'
}


class ErrorResponse(object):
    """Error response
    """
    errorCode = ''
    message = ''
    description = ''
    stackTrace = ''
    threadId = ''
    timeStamp = ''

    def __init__(self):
        """
        Constructor
        """
        dt = datetime.utcnow()
        self.timeStamp = dt.strftime('%Y-%m-%dT%H:%M.%s')


@api.doc('Runs query')
@ns.route('/', strict_slashes=False)
class RunSearchQuery(Resource):
    """
    Submits enrichment query
    """
    POST_HEADERS = RATE_LIMIT_HEADERS
    POST_HEADERS['Location'] = 'URL containing resource/result generated by this request'
    resource_fields = api.model('Query', {
        'geneList': fields.List(fields.String, description='List of genes',
                                example=['brca1'], required=True),
        'databaseList': fields.List(fields.String,
                                    description='List of databases',
                                    example=['enrichment:signor', 'interactome', 'keyword'], default=['enrichment:signor'])
    })

    @api.doc('Runs Query')
    @api.response(202, 'The task was successfully submitted to the service. '
                       'Visit the URL'
                       ' specified in **Location** field in HEADERS to '
                       'status and results', headers=POST_HEADERS)
    @api.response(429, 'Too many requests', TOO_MANY_REQUESTS, headers=RATE_LIMIT_HEADERS)
    @api.response(500, 'Internal server error', ERROR_RESP, headers=RATE_LIMIT_HEADERS)
    @api.expect(resource_fields)
    def post(self):
        """
        Submits query

        Payload in JSON will have genelist which is a list of genes and databaselist which is a list of networkset names corresponding to NDEx network sets. These networks must be normalized such that “n” is gene name, “r” is gene id and “a” is alternate ids
        Initially only signor, PID, wikipathway are supported.


        The service should upon post return 202 and set location to resource to poll for result. Which will
        Match the URL of GET request below.
        """
        app.logger.debug("Post received")

        try:
            if random.choice(['success', 'fail']) is 'fail':
                raise Exception('something failed')

            res = str(uuid.uuid4())

            resp = flask.make_response()
            resp.headers[LOCATION] = CYTOSEARCH_NS + '/' + res
            resp.status_code = 202
            return resp
        except Exception as ea:
            app.logger.exception('Error creating task due to Exception ' +
                                 str(ea))
            er = ErrorResponse()
            er.message = 'Error creating task due to Exception'
            er.description = str(ea)
            return marshal(er, ERROR_RESP), 500


BASE_STATUS = {'status': fields.String(description='One of the following <submitted | processing | complete | failed>',
                                       example='complete'),
               'message': fields.String(description='Any message about query, such as an error message'),
               'progress': fields.Integer(description='% completion, will be a value in range of 0-100',
                                          example=100),
               'wallTime': fields.Integer(description='Time in milliseconds query took to run',
                                          example=341)}


class BaseStatus(object):
    """
    Represents server status, which upon creation will randomly flip around in states
    """
    status = 'submitted'
    message = ''
    progress = 50
    walltime = 1000

    def __init__(self, id):
        """Constructor
        """
        if id is not None:
            self.message = 'id => ' + id + ' '

        self.status = random.choice(['submitted', 'processing', 'complete', 'failed'])
        if self.status is 'complete' or self.status is 'failed':
            self.progress = 100
            self.walltime = random.randint(0, 100000)
            self.message = self.message + random.choice(['okay', 'some warning', 'have a nice day'])
            return

        if self.status is 'submitted':
            self.progress = 0
            self.walltime = 0
            return

        if self.status is 'processing':
            self.progress = random.randint(0, 99)
            self.walltime = 0
            self.message = self.message + random.choice(['hi', 'how', ''])
            return


@ns.route('/<string:id>/status', strict_slashes=False)
class GetTaskStatus(Resource):
    """Class doc here"""

    task_status_resp = api.model('QueryStatus', BASE_STATUS)

    @api.response(200, 'Success', task_status_resp)
    @api.response(410, 'Task not found')
    @api.response(429, 'Too many requests', TOO_MANY_REQUESTS)
    @api.response(500, 'Internal server error', ERROR_RESP)
    def get(self, id):
        """
        Gets status of query

        This lets caller get status without getting the full result back

        """
        bs = BaseStatus(id)
        if bs.status is 'failed':
            er = ErrorResponse()
            er.message = 'There was some error'
            er.description = 'more detailed error heehe'
            return marshal(er, ERROR_RESP), 500

        return marshal(bs, GetTaskStatus.task_status_resp), 200


FULL_STATUS = BASE_STATUS
FULL_STATUS['numberOfHits'] = fields.Integer(description='number of hits being # of networks total')
FULL_STATUS['start'] = fields.Integer(description='Value of start parameter passed in')
FULL_STATUS['size'] = fields.Integer(description='Value of size passed in')
FULL_STATUS['query'] = fields.List(fields.String(),
                                   description='Original query passed in')

result = api.model('QueryResult', {
    'networkUUID': fields.String(description='uuid of network'),
    'databaseUUID': fields.String(description='uuid of database'),
    'databaseName': fields.String(description='name of database'),
    'rank': fields.Integer(description='Rank of result (lower # is better)'),
    'hitGenes': fields.List(fields.String(description='Gene that hit'))
})
FULL_STATUS['results'] = fields.List(fields.Nested(result))


class SingleResult(object):
    """
    Single result
    """
    networkuuid = ''
    databaseuuid = ''
    databasename = ''
    pvalue = 0
    hitgenes = ['']

    def __init__(self):
        """
        Constructor
        """
        self.networkuuid = str(uuid.uuid4())
        self.databaseuuid = str(uuid.uuid4())
        self.databasename = random.choice(['signor', 'pid', 'wikipathways'])
        self.pvalue = random.random()
        self.hitgenes = ['hi']


class FullResult(BaseStatus):
    """
    Full result
    """

    results = []
    query = []
    number_of_hits = 0
    start = 0
    size = 0

    def __init__(self, id, start, size):
        BaseStatus.__init__(self, id)

        self.start = start
        self.size = size
        if self.status is 'failed' or self.status is 'processing' or self.status is 'submitted':
            return

        # processing is completed so lets randomly generate results
        self.number_of_hits = random.randint(0, 100)
        if self.number_of_hits is 0:
            return

        for x in range(self.number_of_hits - 1):
            self.results.append(SingleResult())


@ns.route('/<string:id>', strict_slashes=False)
class GetQueryResult(Resource):
    """More class doc here"""

    fulltask_status_resp = api.model('QueryResults', FULL_STATUS)

    get_params = reqparse.RequestParser()
    get_params.add_argument('start', type=int, location='args',
                            help='Starting index of result, should be an integer 0 or larger',
                            default=0)
    get_params.add_argument('size', type=int, location='args',
                            help='Number of results to return, 0 for all', default=0)

    @api.response(200, 'Successful response from server', fulltask_status_resp)
    @api.response(410, 'Task not found')
    @api.response(429, 'Too many requests', TOO_MANY_REQUESTS)
    @api.response(500, 'Internal server error', ERROR_RESP)
    @api.expect(get_params)
    def get(self, id):
        """
        Gets result of query

        NOTE: For incomplete/failed jobs only Status, message, progress, and walltime will
        be returned in JSON
        """
        params = GetQueryResult.get_params.parse_args(request, strict=True)
        fs = FullResult(id, params['start'], params['size'])
        if fs.status is 'failed':
            er = ErrorResponse()
            er.message = fs.message
            er.description = 'more detailed error heehe'
            return marshal(er, ERROR_RESP), 500

        return marshal(fs, GetQueryResult.fulltask_status_resp), 200

    @api.doc('Creates request to delete query')
    @api.response(200, 'Delete request successfully received')
    @api.response(400, 'Invalid delete request', ERROR_RESP)
    @api.response(429, 'Too many requests', TOO_MANY_REQUESTS)
    @api.response(500, 'Internal server error', ERROR_RESP)
    def delete(self, id):
        """
        Deletes task associated with {id} passed in
        """
        s = random.choice([200, 400, 500])
        if s is 200:
            resp = flask.make_response()
            resp.status_code = s
            return resp

        er = ErrorResponse()
        if s is 400:
            er.message = 'Invalid request somehow'
            er.description = 'hi'
        if s is 500:
            er.message = 'some server error'
            er.description = 'hi there'

        return marshal(er, ERROR_RESP), s


@ns.route('/<string:id>/overlaynetwork', strict_slashes=False)
class GetResultAsCX(Resource):
    """Gets result of query overlayed on network as CX
    """
    get_params = reqparse.RequestParser()
    get_params.add_argument('databaseUUID', type=str, location='args',
                            help='UUID of database', required=True)
    get_params.add_argument('networkUUID', type=str, location='args',
                            help='UUID of network ', required=True)

    @api.response(200, 'Successful response from server and response will be CX')
    @api.response(410, 'Task not found')
    @api.response(429, 'Too many requests', TOO_MANY_REQUESTS)
    @api.response(500, 'Internal server error, or task not completed?', ERROR_RESP)
    @api.expect(get_params)
    def get(self, id):
        """
        Gets result of from a specific database and network as CX

        NOTE: For incomplete/failed 500 will be returned
        """
        s_code = random.choice([200, 410, 500])

        if s_code is 410:
            resp = flask.make_response()
            resp.status_code = s_code
            return resp

        if s_code is 500:
            er = ErrorResponse()
            er.message = 'Internal server error'
            er.description = 'something good'
            return marshal(er, ERROR_RESP), s_code

        resp = jsonify(FAKE_CX)
        resp.status_code = 200
        return resp


class DatabaseResults(object):
    """
    database results
    """
    results = []
    status_code = 200

    def __init__(self):
        """
        Constructor
        """
        self.status_code = random.choice([200, 500])
        if self.status_code is 500:
            return
        self.results = []
        self.results.append({'uuid': '89a90a24-2fa8-4a57-ae4b-7c30a180e8e6',
                            'description': 'The SIGnaling Network Open Resource organizes and stores signaling information published in the scientific literature in a structured format. The core of this project is a collection of more than 11000',
                            'name': 'signor',
                            'numberOfNetworks': 48})

        self.results.append({'uuid': 'e508cf31-79af-463e-b8b6-ff34c87e1734',
                             'description': 'BioGRID is an online interaction repository with data compiled through comprehensive curation efforts. All interaction data are freely provided through their search index and available via download in a wide variety of standardized formats. This account is maintained by the NDEx Team and updated monthly with the latest released data.',
                             'name': 'biogrid',
                             'numberOfNetworks': 14})


@ns.route('/database', strict_slashes=False)
class GetDatabases(Resource):

    dbres = api.model('DatabaseResult', {
        'uuid': fields.String(description='UUID of database'),
        'description': fields.String(description='Description of database'),
        'name': fields.String(description='Name of database'),
        'numberOfNetworks': fields.Integer(description='Number of networks in database')
    })
    dblist = api.model('DatabaseResults', {
        'results': fields.List(fields.Nested(dbres)),
    })

    @api.doc('Gets ')
    @api.response(200, 'Success', dblist)
    @api.response(429, 'Too many requests', TOO_MANY_REQUESTS)
    @api.response(500, 'Internal server error', ERROR_RESP)
    def get(self):
        """
        Gets list of databases that can be queried

        Result in JSON which is a list of objects with uuid and display
        name for database that can be queried.


        """
        dr = DatabaseResults()

        if dr.status_code is 500:
            er = ErrorResponse()
            er.message = 'Internal server error'
            er.description = 'something good'
            return marshal(er, ERROR_RESP), dr.status_code

        return marshal(dr, GetDatabases.dblist), dr.status_code


class ServerStatus(object):
    """Represents status of server
    """
    status = 'ok'
    message = ''
    pcdiskfull = 0
    load = [0,0,0]
    queries = [0,0,0,0,0]
    rest_version = __version__

    def __init__(self):
        """Constructor
        """

        self.pcdiskfull = random.randint(0, 100)
        if self.pcdiskfull is 100:
            self.status = 'error'
            self.message = 'Disk is full'
        else:
            self.status = random.choice(['ok', 'error'])

        self.load[0] = random.random()*10.0
        self.load[1] = random.random()*10.0
        self.load[2] = random.random()*10.0

        self.queries[0] = random.randint(0, 500)
        self.queries[1] = self.queries[0] + random.randint(0, 500)
        self.queries[2] = self.queries[1] + random.randint(0, 500)
        self.queries[3] = self.queries[2] + random.randint(0, 500)
        self.queries[4] = self.queries[3] + random.randint(0, 500)


@ns.route('/status', strict_slashes=False)
class SystemStatus(Resource):

    OK_STATUS = 'ok'

    statusobj = api.model('StatusSchema', {
        'status': fields.String(description='ok|error'),
        'pcDiskFull': fields.Integer(description='How full disk is in %'),
        'load': fields.List(fields.Float(description='server load'),
                            description='List of 3 floats containing 1 minute,'
                                        ' 5 minute, 15minute load'),
        'queries': fields.List(fields.Integer(description='Number of queries'),
                               description='List of 5 integers containing # '
                                           'queries in last minute, 5 '
                                           'minutes, 15 minutes, hour, 24 '
                                           'hours'),
        'restVersion': fields.String(description='Version of REST service')
    })
    @api.doc('Gets status')
    @api.response(200, 'Success', statusobj)
    @api.response(429, 'Too many requests', TOO_MANY_REQUESTS)
    @api.response(500, 'Internal server error', ERROR_RESP)
    def get(self):
        """
        Gets status of service

        """
        s_code = random.choice([200, 500])

        if s_code is 500:
            er = ErrorResponse()
            er.message = 'Internal server error'
            er.description = 'something good'
            return marshal(er, ERROR_RESP), s_code

        ss = ServerStatus()
        return marshal(ss, SystemStatus.statusobj), s_code
