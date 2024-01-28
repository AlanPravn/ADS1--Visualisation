# Import modules
import pandas as pd
import matplotlib.pyplot as plt

# Define all functions
def plot_scatter_chart(data):
    """
    Plot a scatter chart showing the relationship between salary, job category, and experience level.

    Parameters:
    - data (pd.DataFrame): The input DataFrame containing salary, job category, and experience level information.
    """
    plt.figure(figsize=(8, 6))
    colors = {'Mid-level': 'orange', 'Senior': 'blue'}

    for experience_level, group in data.groupby('experience_level'):
        plt.scatter(group['salary_in_usd'], group['job_category'],
                    label=experience_level, alpha=0.7, color=colors.get(experience_level, 'gray'))

    plt.title('Relationship between Salary, Job Category, and Experience Level')
    plt.xlabel('Salary (USD)')
    plt.ylabel('Job Category')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Bar chart to show Average Salary by Job Category
def plot_bar_chart(data):
    avg_salary_per_category = data.groupby('job_category')['salary_in_usd'].mean()

    plt.figure(figsize=(10, 6))
    plt.bar(avg_salary_per_category.index, avg_salary_per_category, color='green')
    plt.title('Average Salary by Job Category')
    plt.xlabel('Job Category')
    plt.ylabel('Average Salary (USD)')

    for i, salary in enumerate(avg_salary_per_category):
        plt.text(i, salary + 1000, f'{salary:.2f}', ha='center', color='black')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Line chart to show Salary Trend Over Years
def plot_line_chart(data):
    plt.figure(figsize=(10, 6))
    for job_category, group in data.groupby('job_category'):
        plt.plot(group['work_year'], group['salary_in_usd'], marker='o', label=job_category)

    plt.title('Salary Trend Over Years by Job Category')
    plt.xlabel('Year')
    plt.ylabel('Salary (USD)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load the dataset
    data = pd.read_csv('data.csv')

    # Call functions to plot the charts
    plot_scatter_chart(data)
    plot_bar_chart(data)
    plot_line_chart(data)