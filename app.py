import reflex as rx

# Import Application States to ensure they register
from state.user_state import UserState
from state.cart_state import CartState
from state.recommendation_state import RecommendationState

# Import pages (as we build them)
import pages.recommendation
import pages.profile
import pages.home
import pages.login
import pages.signup
import pages.products
import pages.product_detail
import pages.cart
import pages.checkout
import pages.payment
import pages.wishlist
import pages.orders

# Create main Reflex App
app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="blue",
    )
)
