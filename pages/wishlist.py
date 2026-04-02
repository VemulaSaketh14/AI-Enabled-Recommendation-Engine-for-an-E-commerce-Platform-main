import reflex as rx
from components.navbar import navbar

@rx.page(route="/wishlist", title="Wishlist")
def wishlist() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.heading("My Wishlist", size="8", margin_top="3rem"),
            rx.text("Save your favorite AI recommendations here. (Coming Soon)", color="gray", margin_top="1rem"),
            size="3"
        )
    )
