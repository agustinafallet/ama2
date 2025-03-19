class PrismaTrapezoidal:
    def __init__(self,base_mayor,base_menor,lado,altura_trapecio,altura_prisma):
        if base_mayor<=0:
            raise ValueError("el dato debe ser positivo")
        else:
            self.__base_mayor=base_mayor
        if base_menor<=0:
            raise ValueError("el dato debe ser positivo")
        else:
            self.__base_menor=base_menor
        if lado<=0:
            raise ValueError("el dato debe ser positivo")
        else:
            self.__lado=lado
        if altura_trapecio<=0:
            raise ValueError("el dato debe ser positivo")
        else:
            self.__altura_trapecio=altura_trapecio
        if altura_prisma<=0:
            raise ValueError("el dato debe ser positivo")
        else:
            self.__altura_prisma=altura_prisma
    @property
    def base_mayor(self):
        return self.__base_mayor
    
    @property
    def base_menor(self):
        return self.__base_menor
    
    @property
    def lado(self):
        return self.__lado
    
    @property
    def altura_trapecio(self):
        return self.__altura_trapecio
    
    @property
    def altura_prisma(self):
        return self.__altura_prisma
    
    @base_mayor.setter
    def base_mayor(self,nueva_base_mayor):
        if self.base_mayor <=0:
            raise ValueError("El dato debe ser positivo")
        self.__base_mayor=nueva_base_mayor


    @base_menor.setter
    def base_menor(self,nueva_base_menor):
        if self.base_menor <=0:
            raise ValueError("El dato debe ser positivo")
        self.__base_menor=nueva_base_menor


    @lado.setter
    def lado(self,nueva_lado):
        if self.lado <=0:
            raise ValueError("El dato debe ser positivo")
        self.__lado=nueva_lado


    @altura_trapecio.setter
    def altura_trapecio(self,nueva_altura_trapecio):
        if self.altura_trapecio <=0:
            raise ValueError("El dato debe ser positivo")
        self.__altura_trapecio=nueva_altura_trapecio

    @altura_prisma.setter
    def altura_prisma(self,nueva_altura_prisma):
        if self.altura_prisma <=0:
            raise ValueError("El dato debe ser positivo")
        self.__altura_prisma=nueva_altura_prisma
    
    
    def area_superficial(self):
        pb=self.base_mayor+self.base_menor+(2*self.lado)
        area=(self.base_mayor+self.base_menor)*self.altura_trapecio+pb*self.altura_prisma
        return area

    def volumen(self):
        vol=((((self.base_mayor+self.base_menor)*self.altura_trapecio)/2)*self.altura_prisma)
        return vol

if __name__ == "__main__":
    prisma1= PrismaTrapezoidal(1,2,3,4,5)
    a=prisma1.area_superficial()
    vol=prisma1.volumen()
    print(vol,a)
    
    
    
    
    




    


















































# class PrismaTrapezoidal:
#     def __init__(self, base_mayor, base_menor, lado, altura_trapecio, altura_prisma):
#         if base_mayor <= 0 or base_menor <= 0 or lado <= 0 or altura_trapecio <= 0 or altura_prisma <= 0:
#             raise ValueError("Todos los valores deben ser positivos")
#         self.base_mayor = base_mayor
#         self.base_menor = base_menor
#         self.lado = lado
#         self.altura_trapecio = altura_trapecio
#         self.altura_prisma = altura_prisma
    
#     def volumen(self):
#         return (((self.base_mayor + self.base_menor) / 2) * self.altura_trapecio) * self.altura_prisma
    
#     def area_superficial(self):
#         return (self.base_mayor + self.base_menor) * self.altura_trapecio + (self.base_mayor + self.base_menor + 2 * self.lado) * self.altura_prisma