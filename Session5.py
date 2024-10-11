import numpy as np
step = (np.pi * 2) / 1000
x = np.arange(0, 2 * np.pi, step)
def main():
    sin_ar = np.sin(x)
    for i in range(len(x)):
        print(f"X Value:{x[i]} Sin(x) Value: {np.sin(x[i])}")
if __name__ == "__main__":
    main()
#THIS TOOK ME SO LONG HOLY FUCK
#I WILL NEVER USE NON NUMPY SINS TO DO AYNTHING




    
