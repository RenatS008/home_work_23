from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from models import BatchRequestParams
from search_engine import search_query

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query/', methods=['POST'])
def perform_query() -> Response:
    try:
        params = BatchRequestParams().load(request.json)  # type: ignore

    except ValidationError as error:
        return Response(response=error.messages, status=400)

    result = None

    for query in params['queries']:
        print(type(query['cmd']))
        result = search_query(cmd=query['cmd'],
                              param=query['value'],
                              data=result,
                              )

    return jsonify(result)
