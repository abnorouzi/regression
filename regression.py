xi = []
yi = []
count = 0

while True:
    x = input("plz enter x coordinate (Enter n or N to quit): ")
    if x == 'n' or x == 'N':
        break
    else:
        xi.append(int(x))
        y = input("plz enter y coordinate : ")
        yi.append(int(y))
        count = count + 1


def calculate_reg():
    sx = 0
    sy = 0
    sx2 = 0
    sxy = 0
    for i in xi:
        sx = i + sx
        sx2 += i * i
    for i in yi:
        sy = i + sy
    for i in range(len(xi)):
        sxy += xi[i] * yi[i]
    down = (count * sx2) - (sx * sx)
    a1 = ((count * sxy) - (sx * sy)) / down
    b1 = ((sx2 * sy) - (sx * sxy)) / down
    print("sx = ", sx)
    print("sx2 = ", sx2)
    print("sxy = ", sxy)
    print("sy = ", sy)
    return a1, b1


a, b = calculate_reg()
print(f"amount of a = {a} and b = {b}")
xn = int(input("enter a x coordinate to predict : "))
yn = (a * xn) + b
print(f"predicted point for y is : {yn}")
