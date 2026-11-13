import math

def box_muller_transform(u1, u2):
    """
    Transforms two independent uniform random variables U(0,1) 
    into two independent standard normal random variables N(0,1).
    """
    # 1. Compute magnitude component
    magnitude = math.sqrt(-2 * math.log(u1))
    
    # 2. Compute angular component
    angle = 2 * math.pi * u2
    
    # 3. Project onto Cartesian coordinates
    z1 = magnitude * math.cos(angle)
    z2 = magnitude * math.sin(angle)
    
    return z1, z2

# Inputs
u1_val = float(input("Enter U1: "))
u2_val = float(input("Enter U2: "))

# Computation
z1_res, z2_res = box_muller_transform(u1_val, u2_val)

# Output Results
print(f"Given U1 = {u1_val} and U2 = {u2_val}:")
print(f"Z1 = {z1_res:.4f}")
print(f"Z2 = {z2_res:.4f}")