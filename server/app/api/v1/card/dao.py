from datetime import datetime
from typing import Any, List
from sqlalchemy.sql.expression import desc

from app.core.db import db
from app.api.v1.card_bin.dao import get_card_bin
from app.api.v1.card_bin.models import CardBin

from .models import Card


def get_card(id) -> Card:
    card = Card.query.get(id)

    return card


def get_all_cards(owner) -> List[Card]:
    cards = Card.query.filter_by(owner=owner).all()

    return cards


def get_flash_cards(owner) -> List[Card]:
    cards = (
        Card.query.filter_by(owner=owner)
        .join(CardBin)
        .order_by(desc(CardBin.bin))
        .all()
    )

    cards = [card for card in cards if card.current_bin.bin != -1]

    return cards


def create_new_card(owner: Any, card: Card) -> Card:
    card_bin = get_card_bin(0)
    card.current_bin = card_bin
    card.owner = owner

    db.session.add(card)
    db.session.commit()

    return card


def mark_card_correct(card: Card):
    card.no_correct = card.no_correct + 1
    current_bin = card.current_bin
    if current_bin.bin < 11:
        new_bin = get_card_bin(current_bin.bin + 1)
        card.current_bin = new_bin
    card.bin_updated_at = datetime.utcnow()

    db.session.commit()

    return card


def mark_card_incorrect(card: Card):
    card.no_wrong = card.no_wrong + 1
    if card.no_wrong == 10:
        new_bin = get_card_bin(-1)
        card.current_bin = new_bin
    else:
        new_bin = get_card_bin(1)
        card.current_bin = new_bin
    card.bin_updated_at = datetime.utcnow()

    db.session.commit()

    return card
