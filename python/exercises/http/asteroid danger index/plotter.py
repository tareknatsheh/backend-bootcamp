import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class ScatterPlot:
    """For creating new separate scatter plots"""
    def __init__(self, x: list, y: list, title_text: str, x_label: str, y_label: str) -> None:
        if len(x) != len(y):
            raise Exception(f"Error: x, y sizes mismatch!\nx has {len(x)} but y has {len(y)}")
        self.x = x
        self.y = y
        self.fig, self.ax = plt.subplots()
        self.ax.scatter(self.x, self.y)
        self.ax.set_title(title_text)
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        plt.tight_layout()
    
class InteractiveBarsPlot:
    """Arguments:
    danger_index_update_func: which is a function that is expected to return the updated
        list of danger indicies when executed. It takes three arguments: A, B, and C
    asteroid_name: list of asteroid names
    """
    def __init__(self, danger_index_update_func, asteroid_names):
        self.danger_index_update_func = danger_index_update_func
        self.asteroid_names = asteroid_names

        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.bars = self.ax.bar(asteroid_names, danger_index_update_func(1, 1, 1))

        plt.xticks(rotation=45)
        plt.tight_layout()

        self.ax.set_xlabel("Astroid name")
        self.ax.set_ylabel("Danger Index")

        # make some room at the bottom for the sliders
        self.fig.subplots_adjust(bottom=0.4)

        ax_A_parameter = self.fig.add_axes(rect=(0.25, 0.1, 0.65, 0.03))
        self.A_slider = Slider(
            ax=ax_A_parameter,
            label='A paramter',
            valmin=1,
            valmax=100000,
            valinit=1,
            valstep=10000
        )
        ax_B_parameter = self.fig.add_axes(rect=(0.25, 0.06, 0.65, 0.03))
        self.B_slider = Slider(
            ax=ax_B_parameter,
            label='B paramter',
            valmin=1,
            valmax=100000,
            valinit=1,
            valstep=10000
        )
        ax_C_parameter = self.fig.add_axes(rect=(0.25, 0.02, 0.65, 0.03))
        self.C_slider = Slider(
            ax=ax_C_parameter,
            label='C paramter',
            valmin=1,
            valmax=10,
            valinit=1,
        )

        self.A_slider.on_changed(self.update)
        self.B_slider.on_changed(self.update)
        self.C_slider.on_changed(self.update)

    # called anytime a slider value changes
    def update(self, val):
        """Update the heights of the bars in the bar chart"""
        for bar, new_y in zip(self.bars, self.danger_index_update_func(self.A_slider.val, self.B_slider.val, self.C_slider.val)):
            bar.set_height(new_y)  # Update the height of each bar

        self.fig.canvas.draw()

def show_plots():
    plt.show()