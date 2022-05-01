#Q2.py
sum = 0.005
up = pow(1 + sum, 365)
down = pow(1 - sum, 365)
print("向: {:.2f}向下: {:.2f}".format(up, down))