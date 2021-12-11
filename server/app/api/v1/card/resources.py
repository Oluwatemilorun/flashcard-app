from uuid import UUID, uuid4
from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from app.utils.response import success, error

from .models import CardSchema
from .dao import (
    get_all_cards,
    create_new_card,
    get_card,
    get_flash_cards,
    mark_card_correct,
    mark_card_incorrect,
)

schema = CardSchema()


class CardResource(Resource):
    def get(self):
        owner = request.headers.get("x-owner-id")
        cards = []

        if owner:
            try:
                cards = get_all_cards(UUID(owner))
            except ValueError:
                raise ValidationError("Invalid owner ID", "header")

        return success(data=schema.dump(cards, many=True))

    def post(self):
        owner = request.headers.get("x-owner-id")

        if owner:
            try:
                UUID(owner)
            except ValueError:
                raise ValidationError("Invalid owner ID", "header")

        owner = UUID(owner) if owner else uuid4()
        body = request.get_json(force=True)
        card = create_new_card(owner=owner, card=schema.load(body))

        return success(data=schema.dump(card), message="Card created successfully.")


class FlashCardResource(Resource):
    def get(self):
        owner = request.headers.get("x-owner-id")
        cards = []

        if owner:
            try:
                cards = get_flash_cards(UUID(owner))
            except ValueError:
                raise ValidationError("Invalid owner ID", "header")

        return success(data=schema.dump(cards, many=True))


class CorrectCardResource(Resource):
    def put(self, card_id):
        card = get_card(card_id)

        if card is None:
            return error(message="Card not found", status=404)

        card = mark_card_correct(card)

        return success(data=schema.dump(card), message="Card updated successfully.")


class IncorrectCardResource(Resource):
    def put(self, card_id):
        card = get_card(card_id)

        if card is None:
            return error(message="Card not found", status=404)

        card = mark_card_incorrect(card)

        return success(data=schema.dump(card), message="Card updated successfully.")
