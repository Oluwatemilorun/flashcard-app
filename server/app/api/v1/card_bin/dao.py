from typing import List

from app.core.db import db

from .models import CardBin


def create_card_bin(card_bin) -> CardBin:
    db.session.add(card_bin)
    db.session.commit()

    return card_bin


def get_all_card_bins() -> List[CardBin]:
    bins = CardBin.query.all()

    return bins
    # try:
    #     bins = CardBin.query.all()

    #     return bins
    # except Exception as e:
    #     print(e)
    #     return []


def get_card_bin(bin: int) -> CardBin:
    card_bin = CardBin.query.filter_by(bin=bin).first()

    return card_bin
