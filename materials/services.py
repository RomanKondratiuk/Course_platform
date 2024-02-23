import export as export
import stripe
import os
from materials.models import Course

API_KEY = os.getenv('STRIPE_API_KEY')


def get_link_of_payment():
    """ The function for creating link for make a courses payment"""

    stripe.api_key = API_KEY

    product = stripe.Product.create(
        name=Course.title
    )

    price = stripe.Price.create(
        currency="usd",
        unit_amount=Course.price,
        recurring={"interval": "month"},
        product_data={"name": product.id},
    )

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price.id, "quantity": 1}],
        mode="payment",
    )

    return session.url

# def get_session(instance):
#     """ Функция возвращает сессию для оплаты """
#     title_product = f"{instance.paid_lesson}" if instance.paid_lesson else ''
#
#     product = stripe.Product.create(
#         name=f'{title_product}'
#     )
#
#     price = stripe.Price.create(
#         unit_amount=instance.payment_amount,
#         currency='usd',
#         product=f'{product.id}',
#     )
#
#     session = stripe.checkout.Session.create(
#         success_url="http://example.com/success",
#         line_items=[
#             {
#                 'price': f'{price.id}',
#                 'quantity': 1,
#             }
#         ],
#         mode='payment',
#         customer_email=f'{instance.user.email}'
#
#     )
#     return session
#
