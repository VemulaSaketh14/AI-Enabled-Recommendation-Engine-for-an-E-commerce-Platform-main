import reflex as rx
from state.user_state import UserState
from state.cart_state import CartState
from components.chatbot import chatbot

def navbar() -> rx.Component:
    """A responsive navigation bar for the e-commerce app."""
    return rx.box(
        rx.hstack(
            rx.link(rx.heading("AI Store", size="6", color="blue"), href="/", underline="none"),
            rx.spacer(),
            rx.hstack(
                rx.link("Home", href="/"),
                rx.link("Products", href="/products"),
                rx.link("Recommendations", href="/recommendations"),
                rx.cond(UserState.logged_in, rx.link("Profile", href="/profile")),
                spacing="5"
            ),
            rx.spacer(),
            rx.hstack(
                rx.link(
                    rx.button(
                        rx.icon(tag="shopping-cart"),
                        rx.badge(
                            CartState.cart_items.length(), 
                            color_scheme="red", 
                            variant="solid", 
                            radius="full",
                            position="absolute",
                            top="-0.5rem",
                            right="-0.5rem"
                        ),
                        variant="outline",
                        position="relative"
                    ),
                    href="/cart"
                ),
                rx.cond(
                    UserState.logged_in,
                    rx.button("Log Out", on_click=UserState.logout, color_scheme="red"),
                    rx.link(rx.button("Log In", color_scheme="blue"), href="/login")
                ),
                spacing="4",
                align_items="center"
            ),
            
            width="100%",
            padding="1rem 2rem",
            border_bottom="1px solid #eaeaea",
            justify_content="space-between",
            align_items="center",
            position="sticky",
            top="0",
            background_color="rgba(255, 255, 255, 0.9)",
            backdrop_filter="blur(10px)",
            z_index="1000"
        ),
        chatbot()
    )
