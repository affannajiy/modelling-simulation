# Gaussian Calculation
# Input
x = float(input("Enter x: "))
mu = float(input("Enter mu: "))
sd = float(input("Enter sd: "))

# Calculation
z = (x - mu) / sd

# Output
print(f"Z: {z:.4f}")