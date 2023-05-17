from enum import Enum

import pandas as pd

DataTypes = Enum("DataTypes", ["sales", "inventory", "purchases", "production"])


def process_sales_data(file_path: str) -> dict:
    """
    Process the sales data from the given file
    path and returns a pandas DataFrame.
    """
    df = pd.read_excel(file_path, sheet_name="Orders")
    average_ticket = df["Sales"].mean().round(2)
    regions = df["Region"].unique()
    region_sales = []
    for region in regions:
        r = {}
        r["name"] = region
        r["total_sales"] = len(df[df["Region"] == region])
        r["average_ticket"] = df[df["Region"] == region]["Sales"].mean().round(2)
        r["most_sold_product"] = (
            df[df["Region"] == region]["Product Name"].value_counts().index[0]
        )
        r["most_sold_product_total_sales"] = df[df["Region"] == region][
            "Product Name"
        ].value_counts()[0]
        r["least_sold_product"] = (
            df[df["Region"] == region]["Product Name"].value_counts().index[-1]
        )
        r["most_sold_category"] = (
            df[df["Region"] == region]["Category"].value_counts().index[0]
        )
        region_sales.append(r)
    return {"average_ticket": average_ticket, "region_sales": region_sales}


def process_data(data_type: DataTypes, file_path: str) -> dict:
    """
    Process the data from the given file path and returns a pandas DataFrame.
    """
    if data_type == DataTypes.sales:
        return process_sales_data(file_path)
    elif data_type == DataTypes.inventory:
        return process_inventory_data(file_path)
    elif data_type == DataTypes.purchases:
        return process_purchases_data(file_path)
    elif data_type == DataTypes.production:
        return process_production_data(file_path)
    else:
        raise ValueError("Invalid data type.")
