from collections import deque

# Node class
class Employee:
    def __init__(self, name):
        self.name = name
        self.children = []   # subordinates


# BFS function
def bfs(root):
    queue = deque([root])

    while queue:
        employee = queue.popleft()
        print(employee.name, end=" ")

        for child in employee.children:
            queue.append(child)


# Creating hierarchy
ceo = Employee("CEO")

manager1 = Employee("Manager1")
manager2 = Employee("Manager2")

staff1 = Employee("Staff1")
staff2 = Employee("Staff2")
staff3 = Employee("Staff3")

# Building the hierarchy
ceo.children = [manager1, manager2]
manager1.children = [staff1, staff2]
manager2.children = [staff3]

print("Employee hierarchy (BFS Level Order):")
bfs(ceo)