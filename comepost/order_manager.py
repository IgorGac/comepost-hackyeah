from .models import Offer
from . import db

class OfferView:
    owner = ""
    desc = ""
    item = None
    amount = None
    def __init__(self, owner, desc, item, amount):
        self.owner = owner
        self.desc = desc
        self.item = item
        self.amount = amount

def addOffer(owner_id, item_id, amount, offer_desc):
    try:
        new_offer = Offer(owner=owner_id, item=item_id, amount=amount, desc=offer_desc)
        db.session.add(new_offer)
        db.session.commit()
    except Exception as e:
        print(str(e))