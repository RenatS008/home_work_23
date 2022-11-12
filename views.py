from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models import BatchRequestParams
from search_engine import search_query

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():

    try:
        params = BatchRequestParams().load(request.json)
    except ValidationError as error:
        return error.messages, 400

    result = None

    for query in params['queries']:
        result = search_query(cmd=query['cmd'],
                              param=query['value'],
                              data=result
                              )

    return jsonify(result)
