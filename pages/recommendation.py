import reflex as rx
from state.recommendation_state import RecommendationState
from components.product_card import product_card

@rx.page(route="/recommendations", title="AI Recommendations")
def recommendation() -> rx.Component:
    """
    A dedicated page to display personalized products.
    Hooks directly into the RecommendationState.
    """
    return rx.container(
        rx.vstack(
            rx.heading("Your Personalized AI Recommendations", size="7", margin_bottom="1rem"),
            rx.text("Curated specifically for your preferences.", color="gray", margin_bottom="2rem"),
            
            rx.button("Fetch Fresh Recommendations", on_click=RecommendationState.fetch_general_recommendations, margin_bottom="2rem"),
            
            rx.cond(
                RecommendationState.is_loading,
                rx.spinner(size="3"),
                
                # Check if we have recommendations
                rx.cond(
                    RecommendationState.recommendations.length() > 0,
                    rx.grid(
                        rx.foreach(
                            RecommendationState.recommendations,
                            lambda p: product_card(p)
                        ),
                        columns="4",
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("No recommendations found or not fetched yet.", color="gray")
                )
            ),
            
            padding_top="3rem",
            padding_bottom="3rem",
            width="100%",
            align_items="center"
        ),
        size="3",
        margin="auto"
    )
