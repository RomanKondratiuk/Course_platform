import export as export
import stripe
import os
from materials.models import Course

API_KEY = os.getenv('STRIPE_SECRET_API_KEY')


# def get_link_of_payment():
#     """ The function for creating link for make a courses payment"""
#
#     stripe.api_key = API_KEY
#
#     product = stripe.Product.create(
#         name='Course_1'
#     )
#
#     price = stripe.Price.create(
#         currency="usd",
#         unit_amount=1000,
#         # product_data={"name": product.id},
#         product=product.id,
#     )
#
#     session = stripe.checkout.Session.create(
#         success_url="https://127.0.0.1.8000/",
#         line_items=[{"price": price.id, "quantity": 1}],
#         mode="payment",
#     )
#
#     return session.url

def get_session(instance):
    """ The function for creating link for make a courses payment """
    # title_product = f"{instance.paid_lesson}" if instance.paid_lesson else ''
    stripe.api_key = API_KEY

    product = stripe.Product.create(
        name=f'{instance.name}'
    )

    price = stripe.Price.create(
        unit_amount=instance.price_amount,
        currency='usd',
        product=f'{product.id}',
    )

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[
            {
                'price': f'{price.id}',
                'quantity': 1,
            }
        ],
        mode='payment',
        # customer_email=f'{instance.user.email}'

    )
    return session.url
