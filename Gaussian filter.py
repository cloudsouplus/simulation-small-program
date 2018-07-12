import xlrd

data = xlrd.open_workbook('0316.xlsx')

def extend(coeffs):
    new_coeffs = [0] * (len(coeffs)+2)
    for i, coeff in enumerate(coeffs):
        new_coeffs[i] += 0.25*coeff
        new_coeffs[i+1] += 0.5*coeff
        new_coeffs[i+2] += 0.25*coeff
    return new_coeffs
In [13]:
mylist = [1]
for i in range(5):
    mylist = extend(mylist)
print(mylist)

In [14]:
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline  
In [19]:
index = [i-5 for i in range(11)]
plt.bar(index, mylist)