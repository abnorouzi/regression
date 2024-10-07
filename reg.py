import numpy as np
import matplotlib.pyplot as plt

xi = [-9, -8, -2, -1, 0, 1, 2, 3, 4, 5]
yi = [449, 335, 25, 15, 7, 9, 27, 43, 77, 107]


class Regression:

    def make_arrays(self, deg, x, y):
        coe_array = []
        res_array = []
        p = (deg * 2) + 1
        for i in range(deg + 1):
            p = p - 1
            jp = p
            for j in range(deg + 1):
                coe_array.append(self.s_pow(x, jp))
                jp = jp - 1
        d = deg
        for i in range(deg + 1):
            res_array.append(self.s_mul(self.power(x, d), y))
            d = d - 1
        coe_array = np.array(coe_array).reshape((deg + 1, deg + 1))
        res_array = np.array(res_array)
        return coe_array, res_array

    def power(self, arr, p):
        arr2 = []
        for i in range(len(arr)):
            arr2.append(pow(arr[i], p))
        return arr2

    def s_pow(self, arr, d):
        s = 0
        arr2 = []
        for i in range(len(arr)):
            arr2.append(pow(arr[i], d))
            s += arr2[i]
        return s

    def s_mul(self, arr1, arr2):
        s = 0
        for i in range(len(arr1)):
            s += arr1[i] * arr2[i]
        return s

    def predict(self, d, x):
        k = np.linalg.solve(self.make_arrays(d, xi, yi)[0], self.make_arrays(d, xi, yi)[1])
        i = s = 0
        h = d
        while i <= h:
            s += k[i] * pow(x, d)
            d -= 1
            i += 1
        return s

y = []

r = Regression()
for i in xi:
    y.append(r.predict(2, i))
y_fit = np.array(y)

plt.scatter(xi, yi, color='blue', label='real points')
plt.plot(xi, y_fit, color='red', label='predicted points')
plt.title('Polynomial Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()
