import reflex as rx

config = rx.Config(
    app_name="AI_Enabled_Recommendation_Engine_for_an_E_commerce_Platform",
    api_url="https://ai-enabled-recommendation-engine-for-an-e-commerce-platform-blu.reflex.run",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)