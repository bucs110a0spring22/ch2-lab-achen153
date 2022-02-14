import random

#Part A
weeks = 16
classes = 3
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))

classes_per_week = 3
print("Classes per week:", classes_per_week, type(classes_per_week))

cost_per_class = cost_per_week / classes_per_week
print("Cost per class", cost_per_class, type(cost_per_class))

#Part B
my_list = ["strawberry", "blueberry", "raspberry", "blackberry", "cranberry"]
print("Random berry is", random.choice(my_list))