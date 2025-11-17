"""
There's a problem with input validation. We want the user to be able
to enter floating-point numbers for mass 1, mass 2, and r.

Fix this program so that it responds appropriately for each individual input
provided by the user. You will need to convert inputs to floats, and respond
with an appropriate message if the user enters a value which cannot be
converted to a float.

Remember that if the user enters an integer it can be converted to a
float with float(). E.g., float(1) => 1.0.
"""

G = 6.67430 * 10 ** -11


def calc_force(m1, m2, r):
    """Given masses in kg, and distance in meters, returns gravitational
    force in Newtons. """
    return G * (m1 * m2) / r ** 2


if __name__ == '__main__':
    while True:
        m_01 = input("Enter the mass of body 01 in kg: ")
        try:
            m_01 = float(m_01)
            if m_01 > 0:
                break
            else:
                print("Mass must be > 0!")
        except ValueError:
            print("Please provide a number!")

    while True:    
        m_02 = input("Enter the mass of body 02 in kg: ")
        try:
            m_02 = float(m_02)
            if m_02 > 0:
                break
            else:
                print("Mass must be > 0!")
        except ValueError:
            print("Please provide a number!")

    while True:    
        d = input("Enter the distance between the centers of the bodies in"
                  "m: ")
        try:
            d = float(d)
            if d > 0:
                break
            else:
                print("Distance must be > 0!")
        except ValueError:
            print("Please provide a number!")

    f = calc_force(m_01, m_02, d)
    print(f"The gravitational force is {f:,.4f} Newtons")
