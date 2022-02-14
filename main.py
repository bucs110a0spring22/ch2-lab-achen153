import random


my_list = ["strawberry", "blueberry", "raspberry", "blackberry", "cranberry"]
print(random.choice(my_list))


#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))


#Part B
weeks = 16
classes = 3
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))

classes_per_week = 3
print("Class per week:", classes_per_week, type(classes_per_week))

cost_per_class = cost_per_week / classes_per_week
print("Cost per class", cost_per_class, type(cost_per_class))

cost_per_week = 125
print("Cost per week:", cost_per_week, type(cost_per_class))