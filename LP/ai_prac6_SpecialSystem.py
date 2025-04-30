rules = {
    "rule1": {
        "condition": lambda data: data["attendance"] >= 7.5 and data["creative"] >= 7,
        "output": "Excellent Employee!"
    },
    "rule2": {
        "condition": lambda data: data["attendance"] >= 5 and data["creative"] >= 6,
        "output": "Average Employee"
    },
    "rule3": {
        "condition": lambda data: data["attendance"] < 5 and data["creative"] < 5,
        "output": "Poor"
    }
}

def evaluate(data):
    for rule in rules.values():
        if rule['condition'](data):
            return rule['output']
    return "Need more details"

# Input from user
data = {
    "attendance": float(input("Enter attendance (e.g. 7.5): ")),
    "creative": float(input("Enter creativity score (e.g. 6.5): "))
}

# Evaluate and print performance
perf = evaluate(data)
print("\nPerformance:", perf)
