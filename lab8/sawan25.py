import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [45000, 52000, 48000, 61000, 58000, 65000, 62000, 70000, 68000, 75000, 72000, 80000]

highest_sale = max(sales)
lowest_sale = min(sales)
highest_month = months[sales.index(highest_sale)]
lowest_month = months[sales.index(lowest_sale)]

print(f"Highest Sales: {highest_month} (₹{highest_sale})")
print(f"Lowest Sales: {lowest_month} (₹{lowest_sale})")

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(months, sales, marker='o', color='b', linewidth=2)
plt.title('Monthly Sales Revenue (Line Chart)')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(months, sales, color='orange')
plt.title('Monthly Sales Revenue (Bar Chart)')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
