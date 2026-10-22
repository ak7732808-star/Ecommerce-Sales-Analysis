import pandas as pd

df = pd.read_excel("Ecommerce_Sales_Analysis.xlsx", sheet_name="Sheet1")
# Total Revenue
total_revenue = df["Revenue"].sum()
print("Total Revenue:", total_revenue)

# Total Orders
total_orders = df["OrderID"].nunique()
print("Total Orders:", total_orders)

# Category-wise Revenue
category_sales = df.groupby("Category")["Revenue"].sum()
print("\nCategory-wise Revenue:")
print(category_sales)
print(df)

print(df.columns.tolist())

import matplotlib.pyplot as plt

# Category-wise Revenue Chart
category_sales = df.groupby("Category")["Revenue"].sum()

category_sales.plot(kind="bar")

plt.title("Category-wise Sales Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()

plt.show()

# Monthly Sales Analysis

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

df["Month"] = df["OrderDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\nMonthly Sales Revenue:")
print(monthly_sales)

# Monthly Sales Chart
monthly_sales.plot(kind="bar", title="Monthly Sales Revenue")

plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.show()

# Sales Insights

top_category = category_sales.idxmax()
top_city = df.groupby("City")["Revenue"].sum().idxmax()
top_product = df.groupby("ProductName")["Revenue"].sum().idxmax()

print("\n--- SALES INSIGHTS ---")
print("Highest Revenue Category:", top_category)
print("Highest Revenue City:", top_city)
print("Highest Revenue Product:", top_product)
print("Total Revenue:", df["Revenue"].sum())
print("Total Orders:", df["OrderID"].nunique())

# City-wise Revenue
city_sales = df.groupby("City")["Revenue"].sum()

print("\nCity-wise Revenue:")
print(city_sales)

# Product-wise Revenue
product_sales = df.groupby("ProductName")["Revenue"].sum()

print("\nProduct-wise Revenue:")
print(product_sales)

# City-wise Revenue Chart
city_sales.plot(kind="bar")

plt.title("City-wise Sales Revenue")
plt.xlabel("City")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.show()

# Product-wise Revenue Chart
product_sales.plot(kind="bar")

plt.title("Product-wise Sales Revenue")
plt.xlabel("Product Name")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()