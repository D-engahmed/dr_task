import numpy as np
import matplotlib.pyplot as plt
def create_data():
    theta = np.linspace(0, 2 * np.pi, 1000)
    return theta

def rose(leav_lenth,num_leavs):
    theta = create_data()
    rose_eq = leav_lenth * np.sin(num_leavs * theta)
    return rose_eq
def cardioid():
    theta = create_data()
    r = 2*(1-np.cos(theta))
    return r
def butterfly():
    theta = create_data()
    r = (np.exp(np.sin(theta)))-(2*np.cos(4*theta))+(np.sin((2*theta-np.pi)/24)**5)
    return r

def visualise_photo(func,curve_nam ,eq) :
    theta = create_data()
    plt.polar(theta, func, 'r')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    mess = curve_nam+"\n by Ahmed abdallh elkossairy \n" +eq
    plt.title(mess)

    plt.show()
    return visualise_photo()

print(" \t\t ** wellcome in valentine ** \n")
name = input("inter your name :- ")
chose =int(input(f"""   HI {name}  
       chose on of this curves
       1- rose 
       2-butterfly 
       3-heart
        to exit clk 0 """))
if chose == 1:
    eq=" r *sin(n * theta)"
    leav_lenth = float(input("inter leaver length (r) :- "))
    num_leavs = float(input("inter integer number ( number of leavers (n)) :- "))

    func = rose(leav_lenth,num_leavs)
    visualise_photo(func,"rose",eq)
elif chose == 2 :
    eq="(exp(sin(theta)))-(2cos(4*theta))+(sin((2*theta-pi)/24)**5)"
    func = butterfly()
    visualise_photo(func, "butterfly", eq)

elif chose == 3 :
    eq = "2(1-np.cos(theta))"
    func = cardioid()
    visualise_photo(func, "heart", eq)
elif chose == 0:
    exit()
else:
    print("pleas refresh follow the orders")
    exit()





