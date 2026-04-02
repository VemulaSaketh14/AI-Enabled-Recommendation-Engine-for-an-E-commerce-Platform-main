import reflex as rx
from state.user_state import UserState

@rx.page(route="/profile", title="User Profile")
def profile() -> rx.Component:
    """
    Professional user profile with black theme.
    """
    return rx.container(
        rx.vstack(
            # Professional profile heading with purple gradient
            rx.heading(
                "👤 User Profile", 
                size="8", 
                margin_bottom="2rem",
                bg_gradient="linear(to-r, #8b5cf6, #7c3aed)",  # Professional purple gradient
                bg_clip="text",
                color="white",
                font_weight="bold"
            ),
            
            rx.cond(
                UserState.logged_in,
                # Logged in profile card - dark glassmorphism
                rx.card(
                    rx.vstack(
                        # Enhanced avatar with glow
                        rx.avatar(
                            fallback="U", 
                            size="8",  # Larger avatar
                            margin_bottom="1.5rem",
                            box_shadow="0 10px 30px rgba(139, 92, 246, 0.4)",
                            bg_gradient="linear(to-br, #8b5cf6, #7c3aed)"
                        ),
                        
                        # User ID row
                        rx.hstack(
                            rx.text("Internal User ID:", font_weight="bold", color="rgb(219, 234, 254)", size="3"),
                            rx.text(UserState.user_id.to_string(), color="white", size="3"),
                            spacing="2",
                            width="100%",
                            margin_bottom="1rem"
                        ),
                        
                        # Firebase UID row
                        rx.hstack(
                            rx.text("Firebase UID:", font_weight="bold", color="rgb(219, 234, 254)", size="3"),
                            rx.text(UserState.firebase_uid, color="white", size="3"),
                            spacing="2",
                            width="100%",
                            margin_bottom="1.5rem"
                        ),
                        
                        # Status badge
                        rx.hstack(
                            rx.text("Status:", font_weight="bold", color="rgb(219, 234, 254)", size="3"),
                            rx.badge(
                                rx.cond(UserState.is_new_user, "New User", "Returning User"), 
                                color_scheme=rx.cond(UserState.is_new_user, "green", "blue"),
                                size="2",
                                padding_x="1.5rem"
                            ),
                            spacing="3",
                            width="100%",
                            margin_bottom="2rem"
                        ),
                        
                        rx.divider(color="rgba(255,255,255,0.2)", margin_y="2rem"),
                        
                        # Logout button
                        rx.button(
                            "🚪 Log Out", 
                            on_click=UserState.logout, 
                            color_scheme="red",
                            size="3",
                            width="100%",
                            bg="linear-gradient(135deg, #ef4444, #dc2626)",
                            color="white",
                            border_radius="1.5rem",
                            box_shadow="0 10px 30px rgba(239, 68, 68, 0.4)",
                            font_weight="bold",
                            _hover={
                                "box_shadow": "0 15px 40px rgba(239, 68, 68, 0.5)",
                                "transform": "translateY(-2px)"
                            }
                        ),
                        
                        align_items="start",
                        width="100%",
                        spacing="3"
                    ),
                    # Dark glassmorphism matching suite
                    width="100%",
                    max_width="450px",
                    padding="3rem",
                    shadow="lg",
                    border_radius="2.5rem",
                    bg="rgba(30, 41, 59, 0.8)",
                    backdrop_blur="30px",
                    border="1px solid rgba(255,255,255,0.1)",
                    box_shadow="0 25px 80px rgba(0,0,0,0.6)"
                ),
                
                # Not logged in state
                rx.card(
                    rx.vstack(
                        rx.heading("🔒 Please Log In", size="6", color="rgb(156, 163, 175)", margin_bottom="1rem"),
                        rx.text("Access your profile and order history.", color="rgb(148, 163, 184)", size="3"),
                        rx.link(
                            rx.button(
                                "Go to Login", 
                                size="3",
                                bg="linear-gradient(135deg, #6366f1, #3b82f6)",
                                color="white",
                                border_radius="1.5rem",
                                box_shadow="0 10px 30px rgba(99, 102, 241, 0.4)"
                            ), 
                            href="/login",
                            _hover={"text_decoration": "none"}
                        ),
                        spacing="3",
                        align_items="center"
                    ),
                    width="100%",
                    max_width="400px",
                    padding="2.5rem",
                    bg="rgba(30, 41, 59, 0.6)",
                    border_radius="2rem",
                    border="1px solid rgba(255,255,255,0.1)"
                )
            ),
            
            padding_top="4rem",
            align_items="center",
            width="100%",
            spacing="4"
        ),
        size="4",
        center=True,
        # Pure black background
        color_scheme="dark",
        bg="#000000",
        min_height="100vh"
    )