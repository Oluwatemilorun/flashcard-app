from flask import Blueprint
from flask_restful import Api

from .resources import CardResource, CorrectCardResource, IncorrectCardResource, FlashCardResource

card_endpoint = 'cards'
card_bp = Blueprint(card_endpoint, __name__)
card_api = Api(card_bp)

# Add endpoints
card_api.add_resource(CardResource, '')
card_api.add_resource(FlashCardResource, '/flash')
card_api.add_resource(CorrectCardResource, '/<string:card_id>/mark-correct')
card_api.add_resource(IncorrectCardResource, '/<string:card_id>/mark-incorrect')
