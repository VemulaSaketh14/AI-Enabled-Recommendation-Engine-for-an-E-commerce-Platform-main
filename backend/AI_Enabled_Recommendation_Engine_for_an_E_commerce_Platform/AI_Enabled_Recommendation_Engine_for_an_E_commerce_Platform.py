"""Main Application Entry Point."""

import reflex as rx

# Application State Imports
from state.user_state import UserState
from state.cart_state import CartState
from state.recommendation_state import RecommendationState

# Import all pages to ensure their routes are registered via their decorators
import pages.home
import pages.login
import pages.signup
import pages.products
import pages.product_detail
import pages.cart
import pages.checkout
import pages.payment
import pages.recommendation
import pages.profile
import pages.wishlist
import pages.orders

app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="blue",
    )
)
