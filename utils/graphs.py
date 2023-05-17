import os

import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image


def generate_graphs(data: pd.DataFrame, data_type: str = "sales") -> list[str]:
    """
    Generates graphs from the given data.
    """
    if not os.path.exists("./graphs"):
        os.mkdir("./graphs")
    if data_type == "sales":
        # * Total sales per region
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(
            [r["name"] for r in data["region_sales"]],
            [r["total_sales"] for r in data["region_sales"]],
        )
        ax.set_title("Total de vendas por região")
        ax.set_xlabel("Região")
        ax.set_ylabel("Total de vendas")

        # * Percentage of sales per region
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.pie(
            [r["total_sales"] for r in data["region_sales"]],
            labels=[r["name"] for r in data["region_sales"]],
            autopct="%1.1f%%",
        )
        ax.set_title("Total de vendas por região")

        # * Most sold product per region
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(
            [f"{r['name']}/{r['most_sold_product']}" for r in data["region_sales"]],
            [r["most_sold_product_total_sales"] for r in data["region_sales"]],
        )
        ax.set_title("Produtos mais vendidos por região")
        ax.set_xlabel("Região")
        ax.set_ylabel("Total de vendas")

        # * Average ticket per region
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(
            [r["name"] for r in data["region_sales"]],
            [r["average_ticket"] for r in data["region_sales"]],
        )
        ax.set_title("Ticket médio por região")
        ax.set_xlabel("Região")
        ax.set_ylabel("Ticket médio")

        # * Save all graphs and combine them into a single PDF file
        figs = [plt.figure(n) for n in plt.get_fignums()]
        [fig.savefig(f"./graphs/{n}.png") for n, fig in enumerate(figs)]
        [plt.close(fig) for fig in figs]
        images = [Image.open(f"./graphs/{n}.png") for n in range(len(figs))]
        images[0].save(
            f"./graphs/{data_type}.pdf",
            resolution=100,
            save_all=True,
            append_images=images[1:],
        )
