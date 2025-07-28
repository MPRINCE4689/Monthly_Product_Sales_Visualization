
# Monthly Product Sales Visualization
# This script creates bar charts, line charts, and pie charts using matplotlib

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set style for better looking plots
plt.style.use('default')

# Read the data
df = pd.read_csv('monthly_product_sales.csv')

print("Data loaded successfully!")
print(f"Shape: {df.shape}")
print("\nFirst few rows:")
print(df.head())

# Create figure with subplots
fig = plt.figure(figsize=(15, 12))

# 1. BAR CHART: Sales by Product
plt.subplot(2, 2, 1)
product_sales = df.groupby('Product')['Units_Sold'].sum()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
bars = plt.bar(product_sales.index, product_sales.values, color=colors)
plt.title('Total Sales by Product', fontsize=14, fontweight='bold')
plt.xlabel('Products', fontweight='bold')
plt.ylabel('Units Sold', fontweight='bold')
plt.xticks(rotation=45, ha='right')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# 2. LINE CHART: Monthly Revenue Trend
plt.subplot(2, 2, 2)
monthly_revenue = df.groupby('Month')['Revenue'].sum()
# Reorder months properly
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
monthly_revenue_ordered = monthly_revenue.reindex(month_order)

plt.plot(range(len(monthly_revenue_ordered)), monthly_revenue_ordered.values, 
         marker='o', linewidth=3, markersize=8, color='#E74C3C')
plt.title('Monthly Revenue Trend', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontweight='bold')
plt.ylabel('Revenue ($)', fontweight='bold')
plt.xticks(range(len(month_order)), [m[:3] for m in month_order], rotation=45)
plt.grid(True, alpha=0.3)

# Format y-axis to show values in thousands
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# Add trend line
z = np.polyfit(range(len(monthly_revenue_ordered)), monthly_revenue_ordered.values, 1)
p = np.poly1d(z)
plt.plot(range(len(monthly_revenue_ordered)), p(range(len(monthly_revenue_ordered))), 
         "--", alpha=0.7, color='gray', label='Trend')
plt.legend()

# 3. PIE CHART: Product Category Contribution
plt.subplot(2, 2, 3)
category_revenue = df.groupby('Category')['Revenue'].sum()
colors_pie = ['#FF6B6B', '#4ECDC4']
wedges, texts, autotexts = plt.pie(category_revenue.values, 
                                  labels=category_revenue.index,
                                  autopct='%1.1f%%',
                                  colors=colors_pie,
                                  explode=(0.05, 0.05),
                                  shadow=True,
                                  startangle=90)

plt.title('Revenue by Product Category', fontsize=14, fontweight='bold')

# Enhance the pie chart text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

# 4. BONUS: Horizontal Bar Chart showing top products by revenue
plt.subplot(2, 2, 4)
product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=True)
bars_h = plt.barh(product_revenue.index, product_revenue.values, color=colors)
plt.title('Revenue by Product', fontsize=14, fontweight='bold')
plt.xlabel('Revenue ($)', fontweight='bold')
plt.ylabel('Products', fontweight='bold')

# Format x-axis to show values in thousands
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# Add value labels on bars
for i, (bar, value) in enumerate(zip(bars_h, product_revenue.values)):
    plt.text(value + max(product_revenue.values) * 0.01, bar.get_y() + bar.get_height()/2,
             f'${value/1000:.0f}K',
             va='center', fontweight='bold')

plt.grid(axis='x', alpha=0.3)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()

# Print some interesting insights
print("\n" + "="*50)
print("DATA INSIGHTS")
print("="*50)

print(f"\n📊 SALES SUMMARY:")
print(f"Total Revenue: ${df['Revenue'].sum():,}")
print(f"Total Units Sold: {df['Units_Sold'].sum():,}")
print(f"Average Revenue per Unit: ${df['Revenue'].sum() / df['Units_Sold'].sum():.2f}")

print(f"\n🏆 TOP PERFORMERS:")
top_product = df.groupby('Product')['Revenue'].sum().idxmax()
top_revenue = df.groupby('Product')['Revenue'].sum().max()
print(f"Best Product by Revenue: {top_product} (${top_revenue:,})")

best_month = monthly_revenue_ordered.idxmax()
best_month_revenue = monthly_revenue_ordered.max()
print(f"Best Month by Revenue: {best_month} (${best_month_revenue:,})")

print(f"\n📈 CATEGORY BREAKDOWN:")
for category, revenue in df.groupby('Category')['Revenue'].sum().items():
    percentage = (revenue / df['Revenue'].sum()) * 100
    print(f"{category}: ${revenue:,} ({percentage:.1f}%)")
