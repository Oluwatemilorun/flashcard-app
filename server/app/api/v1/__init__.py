from flask import Blueprint

from .user import user_bp, user_endpoint
from .card_bin import card_bin_bp, card_bin_endpoint
from .card import card_bp, card_endpoint

api_v1_bp = Blueprint("v1", __name__)

# register API (v1) blueprints
api_v1_bp.register_blueprint(user_bp, url_prefix=user_endpoint)
api_v1_bp.register_blueprint(card_bin_bp, url_prefix=card_bin_endpoint)
api_v1_bp.register_blueprint(card_bp, url_prefix=card_endpoint)
