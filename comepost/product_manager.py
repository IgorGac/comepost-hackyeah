from .models import Item
from . import db


def addItem(item_name, item_value):
    try:
        new_item = Item(name=item_name, value=item_value)
        db.session.add(new_item)
        db.session.commit()
    except Exception as e:
        print(str(e))


def addDefaultItems():
    addItem(item_name="Compost", item_value=1)
    addItem(item_name="Test_vegetable", item_value=100)
    addItem(item_name="ATest_fruit", item_value=153.22)

