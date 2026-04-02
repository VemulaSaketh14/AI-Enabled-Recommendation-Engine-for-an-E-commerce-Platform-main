import reflex as rx
from components.navbar import navbar
from state.cart_state import CartState

@rx.page(route="/payment", title="Razorpay Demo")
def payment() -> rx.Component:
    """Professional Razorpay payment demo with black theme."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                # Payment heading with gold gradient
                rx.heading(
                    "💳 Razorpay Payment Gateway", 
                    size="8", 
                    margin_top="3rem", 
                    margin_bottom="1.5rem",
                    bg_gradient="linear(to-r, #eab308, #ca8a04)",
                    bg_clip="text",
                    color="white",
                    font_weight="bold"
                ),
                
                # Total amount display
                rx.card(
                    rx.text(
                        f"Total Amount Due: ${CartState.total_price}", 
                        size="6", 
                        font_weight="bold", 
                        color="white",
                        bg_gradient="linear(to-r, #eab308, #f59e0b)",
                        bg_clip="text",
                        text_align="center"
                    ),
                    padding="1.5rem 2rem",
                    width="100%",
                    max_width="300px",
                    bg="rgba(234, 179, 8, 0.2)",
                    border="1px solid rgba(234, 179, 8, 0.3)",
                    border_radius="1.5rem",
                    margin_bottom="2rem",
                    box_shadow="0 10px 30px rgba(234, 179, 8, 0.2)"
                ),
                
                # Payment processing card
                rx.card(
                    rx.vstack(
                        # FIXED: Valid icon + correct size type
                        rx.icon(tag="shield_check", size=8, color="#10b981", margin_bottom="1.5rem"),
                        
                        rx.heading(
                            "Processing Secure Payment...", 
                            size="5", 
                            color="white",
                            margin_bottom="1rem",
                            text_align="center"
                        ),
                        
                        rx.text(
                            "Your transaction is being processed safely with Razorpay.", 
                            color="rgb(156, 163, 175)", 
                            size="3",
                            text_align="center",
                            margin_bottom="2rem"
                        ),
                        
                        # Simulate payment success
                        rx.link(
                            rx.button(
                                "✅ Complete Payment", 
                                color_scheme="green",
                                size="3",
                                on_click=CartState.clear_cart,
                                width="100%",
                                bg="linear-gradient(135deg, #10b981 0%, #059669 100%)",
                                color="white",
                                border_radius="1.5rem",
                                box_shadow="0 10px 30px rgba(16, 185, 129, 0.4)",
                                font_weight="bold",
                                _hover={
                                    "box_shadow": "0 15px 40px rgba(16, 185, 129, 0.5)",
                                    "transform": "translateY(-2px)"
                                }
                            ),
                            href="/",
                            width="100%",
                            _hover={"text_decoration": "none"}
                        ),
                        
                        width="100%",
                        align_items="center",
                        spacing="4"
                    ),
                    # Dark glassmorphism
                    padding="3rem",
                    width="100%",
                    max_width="450px",
                    shadow="lg",
                    border_radius="2.5rem",
                    bg="rgba(30, 41, 59, 0.8)",
                    backdrop_blur="30px",
                    border="1px solid rgba(255,255,255,0.1)",
                    box_shadow="0 25px 80px rgba(0,0,0,0.6)"
                ),
                
                width="100%",
                align_items="center",
                spacing="4"
            ),
            size="4",
            center=True
        ),
        # Pure black background
        color_scheme="dark",
        bg="#000000",
        min_height="100vh"
    )