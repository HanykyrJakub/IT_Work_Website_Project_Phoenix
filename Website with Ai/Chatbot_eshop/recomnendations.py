import pandas as pd

def load_data():
    df = pd.read_csv('/test/')
    return df

def get_recommendations(user_id):
    df  = load_data()

    user_purchases = df[df['user_id'] == user_id]

    if user_purchases.empty:
        return []

    purchased_categories = user_purchases['product_id'].unique()

    all_products_in_categories = df[df['category'].isin(purchased_categories)]
    recommended_products = all_products_in_categories[~all_products_in_categories['product_id'].isin(user_purchases['product_id'])]

    similar_users = df[df['category'].isin(purchased_categories) & (df['user_id'] != user_id)]

    most_common_products = similar_users['product_id'].value_counts().head(5).index
    common_products_df = df[df['product_id'].isin(most_common_products)]

    final_recommendations = pd.concat([recommended_products, common_products_df]).drop_duplicates()

    return final_recommendations[['product_id','product_name']].drop_duplicates().to_dict(orient='records')