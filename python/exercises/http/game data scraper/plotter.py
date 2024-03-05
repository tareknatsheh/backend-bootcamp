import matplotlib.pyplot as plt


def plot_tags(data):
    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, subplot 1
    plt.bar(keys, values)
    plt.xlabel('Keys')
    plt.ylabel('Values')
    plt.title('Dictionary Data Bar Plot')

    plt.subplot(1, 2, 2)  # 1 row, 2 columns, subplot 2
    plt.pie(values, labels=keys, autopct='%1.1f%%', startangle=140)
    plt.title('The most appeared game titles', y=1.09)
    plt.axis('equal') 

    plt.tight_layout() 

    plt.show()

def plot_stat_of_tag(user_input, data):
    if user_input in data:
        # Extract keys and values
        keys = list(data.keys())
        values = list(data.values())

        # Explode the slice corresponding to 'b'
        explode = [0.1 if k == user_input else 0 for k in keys]

        # Plotting a pie chart
        plt.figure(figsize=(5, 5))
        plt.pie(values, labels=keys, autopct='%1.1f%%', startangle=140, explode=explode)
        plt.title('Dictionary Data Pie Chart', y=1.05)
        plt.axis('equal')

        plt.show()
    else:
        print(f"This tag: {user_input} is not one of the top 10 tags")
    pass