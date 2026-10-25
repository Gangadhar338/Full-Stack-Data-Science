import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 150, 135, 180]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(months, sales, marker="o")
ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (units)")
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig("monthly_sales.png", dpi=150)
print("Saved monthly_sales.png")
