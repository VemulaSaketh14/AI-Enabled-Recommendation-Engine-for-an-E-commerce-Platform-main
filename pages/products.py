import reflex as rx
from components.navbar import navbar
from components.product_card import product_card
import pandas as pd
import os

class ProductsState(rx.State):
    """Local state for fetching global catalog of products."""
    all_products: list[dict] = []
    
    def fetch_products(self):
        try:
            if os.path.exists('cleaned_data.csv'):
                data = pd.read_csv('cleaned_data.csv')
                # Drop duplicates to display a clean catalog of unique items. Capped at 24 to save memory layout locally
                unique_products = data.drop_duplicates(subset=['ProdID']).head(24).fillna('')
                if "ImageURL" in unique_products.columns:
                    unique_products["ImageURL"] = unique_products["ImageURL"].apply(lambda x: str(x).split(" | ")[0] if pd.notnull(x) and str(x) != "" else "/placeholder.jpg")
                if "ProdID" in unique_products.columns:
                    unique_products["Price"] = unique_products["ProdID"].astype(int).apply(lambda x: f"{(x % 2500) + 499}.00")
                if "Rating" in unique_products.columns:
                    unique_products["Rating"] = unique_products["Rating"].apply(lambda x: f"{float(x):.1f}" if pd.notnull(x) and str(x) != "" else "N/A")
                self.all_products = unique_products.to_dict('records')
        except Exception as e:
            print(f"Error fetching products: {e}")

@rx.page(route="/products", title="Catalog - AI Store", on_load=ProductsState.fetch_products)
def products() -> rx.Component:
    """The generic catalog page showing all products."""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("All Products", size="8", margin_top="3rem", margin_bottom="2rem"),
                
                rx.cond(
                    ProductsState.all_products.length() > 0,
                    rx.grid(
                        rx.foreach(ProductsState.all_products, lambda p: product_card(p)),
                        columns="4",
                        spacing="5",
                        width="100%"
                    ),
                    rx.spinner(size="3")
                ),
                
                padding_bottom="5rem",
                width="100%"
            ),
            size="4"
        )
    )
