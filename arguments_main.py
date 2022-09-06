# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
""" Define function greet in main.py; 3 arguments:
    A name (str)
    greeting (str). Default = 'Hello, <name>!.
return string, <name> in greeting template is replaced by real name."""


def greet(name, greet="Hello, <name>!"):
    greeting = list(str(greet))
    # vervang het gedeelte <name> door de echte naam
    greeting[greeting.index("<"):greeting.index(">") + 1] = name
    personal_greet = "".join(greeting)
    print(personal_greet)
    return personal_greet


"""Part 2: Force.   Lees de opgegeven instructies eerst !!!
Write a function force that takes two arguments:
    mass (float)     body (str), with 'earth' as its default.
Support all 11 bodies listed on the reference website given (lowercase).
Round the gravity factor to 1 decimal"""


def force(mass, body="earth"):
    planet_gravity = {"sun": 274,
                      "jupiter": 24.9,
                      "neptune": 11.2,
                      "saturn": 10.4,
                      "earth": 9.8,
                      "uranus": 8.9,
                      "venus": 8.9,
                      "mars": 3.7,
                      "mercury": 3.7,
                      "moon": 1.6,
                      "pluto": 0.6}
    gravity = planet_gravity[body]
    force = mass * gravity
    return force


"""Part 3: Gravity. pull = G × ((m1×m2)/d2)
Write a function pull that takes three arguments:
    m1 An object's mass in kg (float)
    m2 Another object's mass in kg (float)
    d Their distance in meters (float)
return the gravitional pull that these two objects have on each other. """


def pull(m1, m2, d):
    G = 6.674 * (10 ** (-11))
    d2 = d ** 2
    gravitational_pull = G * ((m1 * m2)/d2)
    return gravitational_pull


if __name__ == "__main__":
    print(greet("Bob", "Leuke dag verder <name> !!!"))
    print(force(10))
    print(pull(800, 1500, 3))
