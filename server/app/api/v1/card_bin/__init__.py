from flask import Blueprint
from flask_restful import Api

from .resources import CardBinResource

card_bin_endpoint = 'card-bins'
card_bin_bp = Blueprint(card_bin_endpoint, __name__)
card_bin_api = Api(card_bin_bp)

# Add endpoints
card_bin_api.add_resource(CardBinResource, '')
