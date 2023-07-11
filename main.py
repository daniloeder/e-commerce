import data
import analysis
import visuals
import recommendation

# Generate the dataset
data_gen = data.DataGenerator()
df = data_gen.generate_data()

# Perform some data analysis
analyzer = analysis.Analyzer(df)
print(analyzer.summary())
top_selling_products = analyzer.top_selling_products()
top_stores = analyzer.top_stores()
customer_spending = analyzer.customer_spending('Customer 1')
sales_by_product = analyzer.sales_by_product('Product 1')

# Create and save some plots
visualizer = visuals.Visualizer(analyzer)
visualizer.plot_top_selling_products()
visualizer.plot_top_stores()

# Generate recommendation
recommender = recommendation.Recommender(df)
recs = recommender.recommend_products('Customer 1')
print(f'Recommended products for Customer 1: {recs}')
