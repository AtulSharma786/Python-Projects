class Dad:
    basketball = 2


class Son(Dad):
    dance = 1
    basketball = 7

    def isdance(self):
        return f"Yes i dance {self.dance} no of dance."


class Grandson(Son):
    dance = 6


darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball)
