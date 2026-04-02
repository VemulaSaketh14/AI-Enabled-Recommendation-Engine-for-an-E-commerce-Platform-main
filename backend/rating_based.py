import pandas as pd

def get_rating_based_recommendations(top_n=10, min_reviews=0, data_path='cleaned_data.csv'):
    """
    Recommend top-rated products for new users based on global average ratings.
    Logic: Group by product -> Take average rating -> Sort descending.
    """
    # Load data
    data = pd.read_csv(data_path)
    
    # Check if necessary columns exist
    required_cols = ['ProdID', 'Rating']
    for col in required_cols:
        if col not in data.columns:
            return f"Required column '{col}' missing from the dataset."
            
    # Group by product
    # Calculate the average rating, and count the number of ratings
    # Also fetch first instance of category and brand for display
    agg_funcs = {
        'Rating': 'mean',
        "User's ID": 'count', # Use this as rating count
        'Category': 'first',
        'Brand': 'first',
        'ImageURL': 'first'
    }
    
    product_stats = data.groupby('ProdID').agg(agg_funcs).rename(columns={"User's ID": 'Rating Count'})
    
    # Optional filtering to ignore products with very few reviews (less reliable ratings)
    if min_reviews > 0:
        product_stats = product_stats[product_stats['Rating Count'] >= min_reviews]
        
    # Sort descending by average rating
    # Secondary sort by 'Rating Count' to break ties
    sorted_products = product_stats.sort_values(by=['Rating', 'Rating Count'], ascending=[False, False])
    
    # Get top_n products
    top_products = sorted_products.head(top_n).reset_index()
    
    return top_products[['ProdID', 'Rating', 'Rating Count', 'Category', 'Brand', 'ImageURL']]

if __name__ == "__main__":
    print("Finding generic top-rated recommendations for a new user...")
    # Using min_reviews=2 as a generic threshold so we don't just get obscure 1-rating 5-star items
    recommendations = get_rating_based_recommendations(top_n=5, min_reviews=2)
    print(recommendations)
