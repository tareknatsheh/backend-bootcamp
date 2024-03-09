import matplotlib.pyplot as plt

class ScatterPlot:
    """For creating new separate scatter plots"""
    def __init__(self, x: list, y: list, title_text: str, x_label: str, y_label: str) -> None:
        if len(x) != len(y):
            raise Exception(f"Error: x, y sizes mismatch!\nx has {len(x)} but y has {len(y)}")
        self.x = x
        self.y = y
        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y)
        ax.set_title(title_text)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        plt.tight_layout()

def show_plots():
    plt.show()

# def plot_scatter(x: list, y: list, title: str, x_label: str, y_label: str) -> None:
    
#     plt.scatter(x, y)
#     plt.title(title)
#     plt.xlabel(x_label)
#     plt.ylabel(y_label)
#     plt.show()
#     pass