from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class Recommender:
    def __init__(self, df):
        self.df = df
        self.user_item_matrix = self._generate_user_item_matrix()
        self.similarity = self._calculate_similarity()

    def _generate_user_item_matrix(self):
        pivot_table = self.df.pivot_table(index='Customer', columns='Product', values='Quantity', fill_value=0)
        return pivot_table

    def _calculate_similarity(self):
        similarity = cosine_similarity(self.user_item_matrix)
        similarity_df = pd.DataFrame(similarity, index=self.user_item_matrix.index, columns=self.user_item_matrix.index)
        return similarity_df

    def recommend_products(self, customer_id, top_n=5):
        similar_customers = self.similarity[customer_id].sort_values(ascending=False)[1:].index
        recommended_products = []

        for customer in similar_customers:
            bought_products = self.df[self.df['Customer'] == customer]['Product'].unique()
            recommended_products.extend([product for product in bought_products if product not in self.df[self.df['Customer'] == customer_id]['Product'].unique()])

            if len(recommended_products) >= top_n:
                break

        return recommended_products[:top_n]
