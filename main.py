import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Line Chart
def plot_line_chart():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title('Line Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

# Bar Chart
def plot_bar_chart():
    categories = ['A', 'B', 'C', 'D']
    values = [3, 7, 1, 5]
    plt.figure()
    plt.bar(categories, values, color='skyblue')
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

# Pie Chart
def plot_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    sizes = [20, 30, 10, 40]
    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart')
    plt.axis('equal')
    plt.show()

# Histogram
def plot_histogram():
    data = np.random.randn(1000)
    plt.figure()
    plt.hist(data, bins=30, color='green', edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Scatter Plot
def plot_scatter_plot():
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 6, 7, 9]
    plt.figure()
    plt.scatter(x, y, color='red')
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

# Box Plot
def plot_box_plot():
    data = [np.random.randn(100) for _ in range(4)]
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data)
    plt.title('Box Plot')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.show()

# Heatmap
def plot_heatmap():
    data = np.random.rand(10, 12)
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True, cmap='coolwarm')
    plt.title('Heatmap')
    plt.show()

# Main function to plot all charts
def main():
    plot_line_chart()
    plot_bar_chart()
    plot_pie_chart()
    plot_histogram()
    plot_scatter_plot()
    plot_box_plot()
    plot_heatmap()

if __name__ == "__main__":
    main()
