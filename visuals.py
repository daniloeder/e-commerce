import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def plot_top_selling_products(self):
        data = self.analyzer.top_selling_products()
        self._plot(data, 'Top Selling Products', 'Total Sales')

    def plot_top_stores(self):
        data = self.analyzer.top_stores()
        self._plot(data, 'Top Stores', 'Total Sales')

    def _plot(self, data, title, ylabel):
        plt.figure(figsize=(10, 6))
        data.plot(kind='bar')
        plt.title(title)
        plt.ylabel(ylabel)
        plt.tight_layout()
        plt.savefig(f'{title.replace(" ", "_").lower()}.png')
