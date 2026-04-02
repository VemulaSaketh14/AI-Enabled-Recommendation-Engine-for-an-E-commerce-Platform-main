import reflex as rx
from state.user_state import UserState
from components.navbar import navbar

@rx.page(route="/login", title="Log In")
def login() -> rx.Component:
    """Professional authentication login page."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                # Professional heading with gradient
                rx.heading(
                    "Log In to Your Account", 
                    size="8", 
                    margin_bottom="1rem",
                    bg_gradient="linear(to-r, #6366f1, #3b82f6)",
                    bg_clip="text",
                    color="white",
                    font_weight="bold"
                ),
                rx.text(
                    "Access your personalized AI recommendations.", 
                    color="rgb(156, 163, 175)", 
                    margin_bottom="3rem",
                    size="4"
                ),
                
                # Enhanced glassmorphism card
                rx.card(
                    rx.vstack(
                        # Professional inputs with dark glass effect
                        rx.input(
                            placeholder="Email Address", 
                            width="100%", 
                            size="3", 
                            on_change=UserState.set_email,
                            bg="rgba(255,255,255,0.1)",
                            color="white",
                            border="1px solid rgba(255,255,255,0.2)",
                            border_radius="1rem",
                            padding_x="1.5rem",
                            _focus={
                                "bg": "rgba(255,255,255,0.2)",
                                "border_color": "#3b82f6"
                            }
                        ),
                        rx.input(
                            placeholder="Password", 
                            type="password", 
                            width="100%", 
                            size="3", 
                            margin_bottom="1.5rem", 
                            on_change=UserState.set_password,
                            bg="rgba(255,255,255,0.1)",
                            color="white",
                            border="1px solid rgba(255,255,255,0.2)",
                            border_radius="1rem",
                            padding_x="1.5rem",
                            _focus={
                                "bg": "rgba(255,255,255,0.2)",
                                "border_color": "#3b82f6"
                            }
                        ),
                        
                        # Error message
                        rx.cond(
                            UserState.auth_error != "",
                            rx.text(UserState.auth_error, color="#f87171", size="2", margin_bottom="1rem")
                        ),
                        
                        # Professional login button
                        rx.button(
                            "🔐 Secure Login", 
                            on_click=UserState.login_with_firebase, 
                            width="100%", 
                            size="3",
                            bg="linear-gradient(135deg, #6366f1 0%, #3b82f6 100%)",
                            color="white",
                            border_radius="1.5rem",
                            box_shadow="0 10px 30px rgba(99, 102, 241, 0.4)",
                            font_weight="bold",
                            _hover={
                                "box_shadow": "0 15px 40px rgba(99, 102, 241, 0.5)",
                                "transform": "translateY(-2px)"
                            }
                        ),
                        
                        # Success state
                        rx.cond(
                            UserState.logged_in,
                            rx.callout(
                                "✅ Successfully Logged In! Redirecting...", 
                                icon="check_circle", 
                                color_scheme="green", 
                                margin_top="1.5rem", 
                                width="100%",
                                bg="rgba(34, 197, 94, 0.1)",
                                border="1px solid rgba(34, 197, 94, 0.2)"
                            ),
                            rx.hstack(
                                rx.text("Don't have an account?", color="rgb(156, 163, 175)", size="3"),
                                rx.link("Sign Up Here", href="/signup", color="#3b82f6", weight="bold", size="3")
                            )
                        ),
                        
                        align_items="center",
                        width="100%",
                        spacing="3"
                    ),
                    # Dark glassmorphism card
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
                
                padding_top="10vh",
                width="100%",
                align_items="center",
                spacing="4"
            ),
            size="4",
            center=True
        ),
        # Pure black background matching home page
        color_scheme="dark",
        bg="#000000",
        min_height="100vh"
    )