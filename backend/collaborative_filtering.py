import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_collaborative_recommendations(user_id, top_n=5, data_path='cleaned_data.csv'):
    """
    Recommend products based on similar users' preferences (collaborative filtering).
    """
    # Load data
    data = pd.read_csv(data_path)
    
    # Check if user exists
    if user_id not in data["User's ID"].values:
        return f"User ID {user_id} not found in the dataset."
    
    # 1. Create user-item matrix
    # pivot_table handles duplicates by default with mean aggregation
    user_item_matrix = data.pivot_table(
        index="User's ID", 
        columns="ProdID", 
        values="Rating", 
        fill_value=0
    )
    
    # 2. Apply cosine similarity between users
    user_similarity = cosine_similarity(user_item_matrix)
    user_similarity_df = pd.DataFrame(
        user_similarity, 
        index=user_item_matrix.index, 
        columns=user_item_matrix.index
    )
    
    # 3. Find similar users
    # Get similarity scores for the target user (drop self)
    sim_scores = user_similarity_df[user_id].drop(user_id)
    
    # Get top similar users based on similarity score
    similar_users = sim_scores.sort_values(ascending=False).head(top_n).index
    
    # 4. Recommend products they liked
    # Get items rated by the target user
    user_rated_products = user_item_matrix.loc[user_id]
    # Identify items the target user hasn't interacted with yet (Rating == 0)
    unrated_products = user_rated_products[user_rated_products == 0].index
    
    # Look at ratings from similar users for these unrated products
    similar_users_ratings = user_item_matrix.loc[similar_users, unrated_products]
    
    # Average rating from similar users (ignoring unrated 0 items)
    similar_users_ratings = similar_users_ratings.replace(0, np.nan)
    avg_ratings = similar_users_ratings.mean().fillna(0)
    
    # Get top predicted product IDs
    recommended_product_ids = avg_ratings.sort_values(ascending=False).head(top_n).index.tolist()
    
    # Get product details for the recommended IDs
    products = data.drop_duplicates(subset=['ProdID']).set_index('ProdID')
    recommended_products = products.loc[recommended_product_ids][['Tags', 'Category', 'Brand', 'ImageURL', 'Rating']].reset_index()
    
    return recommended_products

if __name__ == "__main__":
    # Test function with a sample user ID 
    user_to_test = 1705  # Using sample ID extracted earlier
    print(f"Finding collaborative recommendations for User {user_to_test}...")
    try:
        recommendations = get_collaborative_recommendations(user_id=user_to_test, top_n=5)
        print(recommendations)
    except Exception as e:
        print(f"Error executing collaborative filtering: {e}")
