import numpy as np
import math
def main():
    step = (np.pi * 2) / 1000
    x = np.arange(0, 2 * np.pi, step)
    sin_ar = np.sin(x)
    print(f"Sin(X):{sin_ar} X: {x}")
if __name__ == "__main__":
    main()
#THIS TOOK ME SO LONG HOLY FUCK
#I WILL NEVER USE NON NUMPY SINS TO DO AYNTHING



    
