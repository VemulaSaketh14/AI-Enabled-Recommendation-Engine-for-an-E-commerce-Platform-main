import reflex as rx

def product_card(product: dict) -> rx.Component:
    """
    A reusable product card component.
    Expects a dictionary representing a product from our dataset.
    """
    # Safe fallback values for UI
    img_url = rx.cond(product.contains("ImageURL"), product["ImageURL"], "/placeholder.jpg")
    brand = rx.cond(product.contains("Brand"), product["Brand"], "Brand")
    category = rx.cond(product.contains("Category"), product["Category"], "Category")
    
    return rx.card(
        rx.vstack(
            rx.image(
                src=img_url, 
                height="150px", 
                width="100%", 
                object_fit="cover",
                fallback="https://via.placeholder.com/150"
            ),
            rx.box(
                rx.text(brand, font_weight="bold", font_size="lg", no_of_lines=1),
                rx.text(category, color="gray", font_size="sm", no_of_lines=1),
                margin_top="1rem"
            ),
            rx.hstack(
                # Use dataset rating if available
                rx.badge("★ ", product.get("Rating", "N/A"), color_scheme="green"),
                rx.spacer(),
                rx.text(f"₹{product['Price']}", font_weight="bold", color="blue.600"),
                width="100%",
                padding_top="0.5rem"
            ),
            rx.link(
                rx.button("View Detail", width="100%", margin_top="1rem"),
                href=f"/product/{product['ProdID']}"
            ),
            
            align_items="start",
            height="100%",
            justify_content="space-between"
        ),
        shadow="sm",
        _hover={"shadow": "md", "transform": "translateY(-2px)", "transition": "all 0.2s"},
        overflow="hidden",
        border_radius="md",
        width="100%"
    )
