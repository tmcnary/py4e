class CookieCounter:
    numCookie = 0
    calories = 0
    cookieType = ''
    def __init__(self, name):
        self.cookieType = name
        print(self.cookieType, 'built by constructor')
    def cookie(self):
        self.numCookie = self.numCookie + 1
        self.calories = self.calories + 150
        print(self.cookieType, self.numCookie, self.calories)

c = CookieCounter('Chocolate Chip')
o = CookieCounter('Oatmeal Rasin')

c.cookie()
c.cookie()
o.cookie()
o.cookie()