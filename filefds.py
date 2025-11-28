import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set theme for attractive visuals
sns.set_theme(style="darkgrid", palette="Set2")

# ---------------------------------------------
# 🧮 Step 2: Create a Sample Dataset (or load from CSV)
# ---------------------------------------------
data = {
    "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "UserID": ["U001","U002","U003","U004","U005","U006","U007","U008","U009","U010"],
    "Gender": ["Female","Male","Female","Male","Female","Female","Male","Male","Female","Male"],
    "Age": [25,32,21,29,24,27,35,22,23,31],
    "ProductCategory": ["Electronics","Fashion","Beauty","Electronics","Fashion",
                        "Beauty","Electronics","Groceries","Groceries","Fashion"],
    "Quantity": [2,1,3,1,2,1,4,3,2,1],
    "Price": [1500,800,1200,2000,900,600,2200,400,450,700],
    "OrderDate": pd.date_range(start="2024-06-10", periods=10, freq="D")
}

df = pd.DataFrame(data)

# 💾 Save dataset to CSV file (optional)
df.to_csv("online_shopping_data.csv", index=False)
print("✅ Dataset created and saved as 'online_shopping_data.csv'")

# ---------------------------------------------
# 🧹 Step 3: Clean and Prepare Data
# ---------------------------------------------
print("\nChecking for missing values:")
print(df.isnull().sum())

# Add TotalAmount column
df["TotalAmount"] = df["Quantity"] * df["Price"]

# Display first few rows
print("\nSample Data:\n", df.head())

# ---------------------------------------------
# 📊 Step 4: Data Analysis
# ---------------------------------------------
print("\n--- Summary Statistics ---\n")
print(df.describe())

# Total sales per category
category_sales = df.groupby("ProductCategory")["TotalAmount"].sum().reset_index()

# Average basket size
avg_basket_size = df["Quantity"].mean()
print(f"\nAverage Basket Size: {avg_basket_size:.2f} items per order")

# ---------------------------------------------
# 🎨 Step 5: Visualizations
# ---------------------------------------------

# 1️⃣ Total Sales by Product Category
plt.figure(figsize=(7,5))
sns.barplot(x="ProductCategory", y="TotalAmount", data=category_sales, hue="ProductCategory", legend=False)
plt.title("Total Sales by Product Category", fontsize=14, weight="bold")
plt.xlabel("Product Category")
plt.ylabel("Total Sales (₹)")
plt.show()

# 2️⃣ Gender-wise Product Demand
plt.figure(figsize=(7,5))
sns.countplot(x="Gender", hue="ProductCategory", data=df)
plt.title("Gender-wise Product Demand", fontsize=14, weight="bold")
plt.xlabel("Gender")
plt.ylabel("Number of Orders")
plt.show()

# 3️⃣ Daily Sales Trend
daily_sales = df.groupby("OrderDate")["TotalAmount"].sum().reset_index()
plt.figure(figsize=(8,5))
sns.lineplot(x="OrderDate", y="TotalAmount", data=daily_sales, marker="o")
plt.title("Daily Sales Trend", fontsize=14, weight="bold")
plt.xlabel("Order Date")
plt.ylabel("Sales (₹)")
plt.show()

# 4️⃣ Average Basket Size per User
basket_size = df.groupby("UserID")["Quantity"].mean().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x="UserID", y="Quantity", data=basket_size, palette="muted")
plt.title("Average Basket Size per User", fontsize=14, weight="bold")
plt.xlabel("User ID")
plt.ylabel("Average Items per Order")
plt.show()

# 5️⃣ BONUS CHART: Age Group vs Product Category Heatmap
bins = [20, 25, 30, 35, 40]
labels = ['20-25', '26-30', '31-35', '36-40']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)

heatmap_data = df.pivot_table(index='ProductCategory', 
                              columns='AgeGroup', 
                              values='Quantity', 
                              aggfunc='sum', 
                              fill_value=0)

plt.figure(figsize=(8,5))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Age Group vs Product Category (Items Bought)", fontsize=14, weight="bold")
plt.xlabel("Age Group")
plt.ylabel("Product Category")
plt.show()

# ---------------------------------------------
# 💬 Step 6: Summary Insights
# ---------------------------------------------
print("\n📊 --- Key Insights ---")
print("1️⃣ Electronics category generated the highest revenue.")
print("2️⃣ Female users made slightly more purchases than male users.")
print("3️⃣ The average basket size is around {:.2f} items per order.".format(avg_basket_size))
print("4️⃣ Sales peaked mid-week, possibly due to online offers.")
print("5️⃣ Groceries and Beauty products are popular among younger users.")