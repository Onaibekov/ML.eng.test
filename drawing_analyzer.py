import os
import pandas as pd
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self):
        self.plot_dir = "plots"
        os.makedirs(self.plot_dir, exist_ok=True)

    def draw_plots(self, data_plots):
        data = pd.read_json(data_plots)

        columns_to_compare = [
            "mean",
            "max",
            "min",
            "floor_mean",
            "floor_max",
            "floor_min",
            "ceiling_mean",
            "ceiling_max",
            "ceiling_min"
        ]

        for column in columns_to_compare:
            plt.figure(figsize=(10, 6))
            plt.scatter(data["gt_corners"], data[column], label=column)
            plt.xlabel("Ground Truth Corners")
            plt.ylabel(f"Deviation for {column} (degrees)")
            plt.legend()
            plt.title(f"Comparison of Ground Truth Corners vs {column}")
            plt.grid()
            plot_path = os.path.join(self.plot_dir, f"{column}_vs_gt_corners.png")
            plt.savefig(plot_path)
            plt.close()

        return [os.path.join(self.plot_dir, f"{column}_vs_gt_corners.png") for column in columns_to_compare]


if __name__ == "__main__":
    data_file = "/Users/onaybekov/Documents/DocuSketch/deviation.json"
    plotter = Plotter()
    plot_paths = plotter.draw_plots(data_file)
    print("Plots saved to:", plot_paths)
