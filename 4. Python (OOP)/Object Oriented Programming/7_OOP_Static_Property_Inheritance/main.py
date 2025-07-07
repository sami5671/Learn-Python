"""- If Parent has static properties, child can access as it is like parent
- If Child has static properties, Parent can't access as it is like child
- How child can access parents static and non-static properties
"""

class Father:

    x = 10
    y = 20

    @staticmethod
    def addTwo():
        print(Father.x + Father.y)

class Son(Father):
    pass

Father.addTwo()
Son.addTwo()