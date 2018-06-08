class Mandelbrot:
    def __init__(self):
        pass

    def calc_mandelbrot(self,Cr,Ci,escape_num,iterations=50):
        Zr = 0
        Zi = 0
        Tr = 0
        Ti = 0
        n = 0

        while( n < iterations and (Tr+Ti) <= escape_num ):
            n += 1
            Zi = 2 * Zr * Zi + Ci
            Zr = Tr - Ti + Cr
            Tr = Zr**2
            Ti = Zi**2

        for a in range(4):
            Zi = 2 * Zr * Zi + Ci
            Zr = Tr - Ti + Cr
            Tr = Zr**2
            Ti = Zi**2

        return [n,Tr,Ti]
