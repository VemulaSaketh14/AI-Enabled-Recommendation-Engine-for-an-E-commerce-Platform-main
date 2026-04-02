import reflex as rx
from components.navbar import navbar
from state.cart_state import CartState
from state.recommendation_state import RecommendationState
from components.product_card import product_card
class ProductDetailState(rx.State):
    """Local state for product details. Typically queries ID from URL Params."""
    current_product: dict = {
        "ProdID": 999, 
        "Brand": "Loading...", 
        "Category": "...", 
        "Price": "0.00", 
        "ImageURL": "/placeholder.jpg", 
        "Description": "Please wait while we fetch product details."
    }

    def load_product(self):
        try:
            if not self.pid:
                return
            target_id = int(self.pid)
            import pandas as pd
            import os
            if os.path.exists('cleaned_data.csv'):
                df = pd.read_csv('cleaned_data.csv')
                match = df[df['ProdID'] == target_id]
                if not match.empty:
                    item = match.iloc[0].fillna('').to_dict()
                    if "ImageURL" in item and item["ImageURL"]:
                        item["ImageURL"] = str(item["ImageURL"]).split(" | ")[0]
                    else:
                        item["ImageURL"] = "/placeholder.jpg"
                    
                    item["Price"] = f"{(int(item['ProdID']) % 2500) + 499}.00"
                    
                    if "Rating" in item and item["Rating"] != "":
                        try:
                            item["Rating"] = f"{float(item['Rating']):.1f}"
                        except:
                            item["Rating"] = "N/A"
                            
                    if not item.get("Description"):
                        item["Description"] = "No detailed description available for this product."
                    self.current_product = item
                    return
        except Exception as e:
            print(f"Error loading product detail: {e}")
            
        self.current_product = {
            "ProdID": 999, 
            "Brand": "Product Not Found", 
            "Category": "N/A", 
            "Price": "0.00", 
            "ImageURL": "/placeholder.jpg", 
            "Description": "Could not locate this product in the dataset."
        }

@rx.page(route="/product/[pid]", title="Product Detail", on_load=ProductDetailState.load_product)
def product_detail() -> rx.Component:
    """Dynamic routing page for individual product inspection."""
    return rx.box(
        navbar(),
        rx.container(
            rx.hstack(
                rx.image(
                    src=ProductDetailState.current_product["ImageURL"], 
                    height="400px", 
                    width="400px", 
                    object_fit="cover", 
                    border_radius="xl",
                    shadow="lg",
                    fallback="https://via.placeholder.com/400"
                ),
                
                rx.vstack(
                    rx.heading(ProductDetailState.current_product["Brand"], size="8"),
                    rx.badge(ProductDetailState.current_product["Category"], color_scheme="indigo", size="2", margin_bottom="1rem"),
                    rx.text(f"₹{ProductDetailState.current_product['Price']}", size="7", font_weight="bold", color="green", margin_bottom="1rem"),
                    rx.text(ProductDetailState.current_product["Description"], color="gray", size="4", margin_bottom="2rem"),
                    
                    rx.button(
                        rx.icon(tag="shopping-cart"),
                        " Add to Cart", 
                        size="4", 
                        color_scheme="orange", 
                        on_click=lambda: CartState.add_to_cart(ProductDetailState.current_product)
                    ),
                    rx.link(rx.button("Buy Now", size="4", color_scheme="green", variant="solid", margin_top="1rem"), href="/checkout"),
                    
                    align_items="start",
                    width="100%",
                    padding_left="3rem"
                ),
                width="100%",
                margin_top="5rem",
                align_items="start"
            ),
            
            rx.divider(margin_top="4rem", margin_bottom="2rem"),
            
            rx.vstack(
                rx.heading("Recommendation as per your history", size="6", margin_bottom="1rem", text_align="center"),
                rx.button(
                    "View Related Recommendations",
                    on_click=lambda: RecommendationState.fetch_recommendations(ProductDetailState.current_product["ProdID"].to(int)),
                    size="3",
                    color_scheme="indigo",
                    margin_bottom="2rem"
                ),
                rx.cond(
                    RecommendationState.is_loading,
                    rx.spinner(size="3"),
                    rx.grid(
                        rx.foreach(RecommendationState.recommendations, lambda p: product_card(p)),
                        columns="4",
                        spacing="4",
                        width="100%"
                    )
                ),
                align_items="center",
                width="100%",
                padding_bottom="4rem"
            ),
            
            size="4"
        )
    )
