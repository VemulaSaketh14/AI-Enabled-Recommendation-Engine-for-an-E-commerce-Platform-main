import reflex as rx
from state.user_state import UserState
from state.recommendation_state import RecommendationState
from components.navbar import navbar
from components.product_card import product_card

@rx.page(route="/", title="Home - AI Store")
def home() -> rx.Component:
    """The landing page. Shows different headings based on user type."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                # Enhanced hero with gradient text effect
                rx.heading(
                    "Welcome to Your AI-Powered Store!", 
                    size="9", 
                    margin_top="3rem", 
                    margin_bottom="1rem", 
                    text_align="center",
                    bg_gradient="linear(to-r, #6366f1, #3b82f6)",
                    bg_clip="text",
                    font_weight="bold",
                    color="white"
                ),
                rx.text(
                    "Discover products perfectly tailored for you using Machine Learning.", 
                    size="4", 
                    color="rgb(156, 163, 175)",  # Light gray for dark bg
                    margin_bottom="3rem", 
                    text_align="center"
                ),
                
                # Dynamic heading based on UserState - KEPT EXACT SAME LOGIC
                rx.cond(
                    UserState.is_new_user,
                    # If new user or not logged in -> rating based heading
                    rx.heading("Top Rated Products Just For You", size="6", margin_bottom="1rem", color="white"),
                    # If existing logged in user -> Collaborative heading
                    rx.heading("People like you also liked", size="6", margin_bottom="1rem", color="white") 
                ),
                
                # Glassmorphism button for dark theme
                rx.button(
                    "Load My Recommendations", 
                    on_click=RecommendationState.fetch_general_recommendations, 
                    size="3", 
                    bg="rgba(255,255,255,0.1)",
                    color="white",
                    border="1px solid rgba(255,255,255,0.2)",
                    border_radius="1.5rem",
                    padding_x="2rem",
                    box_shadow="0 8px 32px rgba(0,0,0,0.4)",
                    backdrop_blur="20px",
                    _hover={
                        "bg": "rgba(255,255,255,0.25)",
                        "box_shadow": "0 12px 40px rgba(0,0,0,0.5)"
                    },
                    margin_bottom="2rem"
                ),
                
                # Loading & Products Grid - ALL FEATURES PRESERVED
                rx.cond(
                    RecommendationState.is_loading,
                    rx.center(
                        rx.vstack(
                            rx.spinner(size="3", color="white"),
                            rx.text("Loading your personalized recommendations...", size="4", color="rgb(156, 163, 175)"),
                            spacing="3"
                        ),
                        margin_y="4rem"
                    ),
                    rx.cond(
                        RecommendationState.recommendations,
                        rx.grid(
                            rx.foreach(RecommendationState.recommendations, lambda p: product_card(p)),
                            columns="repeat(auto-fit, minmax(280px, 1fr))",
                            spacing="4",
                            width="100%"
                        ),
                        rx.center(
                            rx.vstack(
                                rx.heading("No recommendations yet!", size="6", color="rgb(156, 163, 175)"),
                                rx.text("Click 'Load My Recommendations' to get started!", size="4", color="rgb(148, 163, 184)"),
                                spacing="3"
                            ),
                            margin_y="4rem"
                        )
                    )
                ),
                
                padding_bottom="4rem",
                width="100%",
                align_items="center",
                spacing="4",
                padding_x="2rem"
            ),
            size="4",
            center=True,
            # Dark glass container for black background
            bg="rgba(30, 41, 59, 0.6)",  # Dark slate glass
            border_radius="2rem",
            margin="2rem",
            backdrop_blur="30px",
            border="1px solid rgba(255,255,255,0.1)",
            box_shadow="0 25px 80px rgba(0,0,0,0.6)"
        ),
        # PURE BLACK BACKGROUND
        color_scheme="dark",
        bg="#000000",  # Pure black
        min_height="100vh"
    )