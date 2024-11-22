import matplotlib.pyplot as plt

print("Enter data for the pie chart.")
sizes = list(map(int, input("Enter sizes (comma-separated integers): ").split(",")))
labels = input("Enter labels (comma-separated): ").split(",")

if len(sizes) != len(labels):
    print("Error: The number of sizes must match the number of labels.")
else:
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    circle = plt.Circle((0, 0), 0.8, color="#ffffff", fc="white")
    plt.gca().add_artist(circle)
    plt.title("User-Input Donut Chart")
    plt.axis("equal")

    plt.savefig("../img/User_Donut_Chart.png")
    print("Chart saved as 'User_Donut_Chart.png'")
