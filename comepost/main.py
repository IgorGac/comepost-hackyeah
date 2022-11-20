from flask import Blueprint, render_template, flash, redirect, url_for, request
from . import db
from .order_manager import addOffer, OfferView
from .product_manager import addItem
from flask_login import login_required, current_user
from .models import Offer, Item, User
from .value_scrapper import get_current_prices
from json import dumps
main = Blueprint('main', __name__)
#MAIN PAGE && INDIVIDUAL
@main.route('/')
def index():
    return render_template("index.html")
@main.route('/individuals')
def individual():
    return render_template("individuals.html")


@main.route('/market')
def market():
    reverseOffers = False
    if request.args.get('filter') == "desc":
        print("XD")
        reverseOffers = True
    fetched_offers = []
    product_names = {}
    offers = Offer.query.order_by().all()
    products_query = Item.query.order_by().all()
    for prod in products_query:
        product_names[f"{prod.name}"] = (f'{prod.value}')
    for offer in offers:
        owner = User.query.filter_by(id=offer.owner).first().name
        item = Item.query.filter_by(id=offer.item).first().name
        new_offer = OfferView(owner=owner, item=item, amount=offer.amount, desc=offer.desc)
        fetched_offers.append(new_offer)
    reversed_offers = list(reversed(fetched_offers))
    if not reverseOffers:
        return render_template("market.html", offers=reversed_offers, products=product_names, offers_filter="asc")
    else:
        return render_template("market.html", offers=fetched_offers, products=product_names, offers_filter="desc")
@main.route('/market', methods=["POST"])
def market_post():
    try:
        print("Attempting to add an offer...")
        desc = request.form.get('offerdesc')
        amount = request.form.get('offeramount')
        print(request.form.get('offerproduct'))
        item = Item.query.filter_by(name=request.form.get('offerproduct')).first().id
        addOffer(owner_id=current_user.id, item_id=item, amount=amount, offer_desc=desc)
        print("Offer created!")
        flash('Order created')
    except Exception as e:
        print(f"[!] An error occured during offer insert. Error: {e}")
    return redirect(url_for('main.market'))

#DATABASE SETUP ENDPOINTS
@main.route('/setup')
def setup():
    return render_template('setup.html')
@main.route('/setup', methods=['POST'])
def setup_post():
    try:
        scrapped_products = ['carrot', 'onion', 'tomatoes', 'pumpkin', 'celeriac', 'pears', 'potatoes']
        scrapped_unit = "kilogram"   
        scrapped_items = get_current_prices(scrapped_products=scrapped_products, scrapped_unit=scrapped_unit)
        for scrapped_item in scrapped_items:
            addItem(item_name=scrapped_item.name, item_value=scrapped_item.value*100)
    except Exception as e:
        print(f"[!]An error occured: {e}")
        return redirect(url_for('main.setup'))
    return redirect(url_for('main.setup'))

#DASHBOARD
@main.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", name=current_user.name)
