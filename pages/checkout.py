import reflex as rx
from components.navbar import navbar

@rx.page(route="/checkout", title="Checkout")
def checkout() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "🛒 Secure Checkout", 
                    size="8", 
                    margin_top="3rem", 
                    margin_bottom="2rem",
                    bg_gradient="linear(to-r, #f59e0b, #d97706)",
                    bg_clip="text",
                    color="white",
                    font_weight="bold"
                ),
                
                rx.card(
                    rx.vstack(
                        # Full Name input - FIXED HEIGHT & PADDING
                        rx.input(
                            placeholder="👤 Full Name", 
                            width="100%", 
                            height="3.5rem",  # ✅ FIXED: Explicit height
                            size="3",
                            bg="rgba(255,255,255,0.18)",
                            color="white",
                            _placeholder={
                                "color": "rgb(171, 190, 209)"
                            },
                            border="2px solid rgba(255,255,255,0.25)",  # Thicker border
                            border_radius="12px",
                            padding_x="1.75rem",
                            padding_y="1rem",  # ✅ Balanced padding
                            font_size="16px",  # ✅ Standard font size
                            line_height="1.5",  # ✅ Proper line height
                            outline="none",
                            _focus={
                                "bg": "rgba(255,255,255,0.28)",
                                "border_color": "#f59e0b",
                                "box_shadow": "0 0 0 4px rgba(245, 158, 11, 0.15)"
                            },
                            margin_bottom="1.5rem"
                        ),
                        
                        # Phone input - FIXED HEIGHT & PADDING
                        rx.input(
                            placeholder="📱 Phone Number", 
                            width="100%", 
                            height="3.5rem",  # ✅ FIXED: Explicit height
                            size="3",
                            bg="rgba(255,255,255,0.18)",
                            color="white",
                            _placeholder={
                                "color": "rgb(171, 190, 209)"
                            },
                            border="2px solid rgba(255,255,255,0.25)",
                            border_radius="12px",
                            padding_x="1.75rem",
                            padding_y="1rem",
                            font_size="16px",
                            line_height="1.5",
                            outline="none",
                            _focus={
                                "bg": "rgba(255,255,255,0.28)",
                                "border_color": "#f59e0b",
                                "box_shadow": "0 0 0 4px rgba(245, 158, 11, 0.15)"
                            },
                            margin_bottom="1.5rem"
                        ),
                        
                        # Address textarea - FIXED HEIGHT
                        rx.text_area(
                            placeholder="📍 Delivery Address", 
                            width="100%", 
                            height="140px",  # ✅ FIXED: Explicit height
                            size="3",
                            bg="rgba(255,255,255,0.18)",
                            color="white",
                            _placeholder={
                                "color": "rgb(171, 190, 209)"
                            },
                            border="2px solid rgba(255,255,255,0.25)",
                            border_radius="12px",
                            padding="1.5rem",
                            rows="4",
                            font_size="16px",
                            line_height="1.6",
                            resize="vertical",
                            outline="none",
                            _focus={
                                "bg": "rgba(255,255,255,0.28)",
                                "border_color": "#f59e0b",
                                "box_shadow": "0 0 0 4px rgba(245, 158, 11, 0.15)"
                            },
                            margin_bottom="2.5rem"
                        ),
                        
                        # Checkout button
                        rx.link(
                            rx.button(
                                "💳 Proceed to Payment", 
                                size="3", 
                                width="100%",
                                height="3.75rem",  # ✅ Tall button
                                bg="linear-gradient(135deg, #f59e0b 0%, #d97706 100%)",
                                color="white",
                                border_radius="16px",
                                box_shadow="0 12px 35px rgba(245, 158, 11, 0.4)",
                                font_weight="bold",
                                font_size="1.1rem",
                                line_height="1.4",
                                _hover={
                                    "box_shadow": "0 18px 45px rgba(245, 158, 11, 0.5)",
                                    "transform": "translateY(-3px)"
                                }
                            ),
                            href="/payment",
                            width="100%",
                            _hover={"text_decoration": "none"}
                        ),
                        
                        width="100%",
                        spacing="4",
                        padding="1rem 0"
                    ),
                    padding="4rem",  # More card padding
                    width="100%",
                    max_width="550px",
                    shadow="lg",
                    border_radius="3rem",
                    bg="rgba(26, 32, 44, 0.95)",  # Darker card bg
                    backdrop_blur="50px",
                    border="1px solid rgba(255,255,255,0.2)",
                    box_shadow="0 35px 100px rgba(0,0,0,0.75)"
                ),
                
                width="100%",
                align_items="center",
                spacing="6"
            ),
            size="4",
            center=True
        ),
        color_scheme="dark",
        bg="#000000",
        min_height="100vh"
    )