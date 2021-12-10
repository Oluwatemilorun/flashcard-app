from flask import request
from flask_restful import Resource

from app.utils.response import success, error

from .models import CardBin, CardBinSchema
from .dao import create_card_bin, get_all_card_bins

schema = CardBinSchema()

class CardBinResource(Resource):
    def post(self):
        body = request.get_json(force=True)
        card_bin = create_card_bin(schema.load(body))

        return success(
            data=schema.dump(card_bin),
            message="Card bin created sucessfully"
        )
        

    def get(self):
        card_bins = get_all_card_bins()

        return success(
            data=schema.dump(card_bins, many=True), message="Card bins fetched successfully"
        )


