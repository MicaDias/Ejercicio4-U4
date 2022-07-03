
class Fraccion:
    __numerador=None
    __denominador=None
    def __init__(self,numerador=0,denominador=0):
        self.__numerador=numerador
        self.__denominador=denominador
    def getDenominador(self):
        return self.__denominador
    def getNumerador(self):
        return self.__numerador
    def __add__(self,otro):
        resultado=None
        if type(otro)!=Fraccion:
            otro=Fraccion(otro,1)
        mult=self.__denominador*otro.getDenominador()
        dividir=mult/self.__denominador*self.__numerador
        dv=mult/otro.getDenominador()*otro.getNumerador()
        resultado=Fraccion(int(dividir+dv),int(mult))
        resultado.simplificar()
        return resultado

    def simplificar(self):
        divisor=None
        resto=None
        dividendo=None
       
        if abs(self.__numerador)>abs(self.__denominador):
            dividendo=abs(self.__numerador)
            divisor=abs(self.__denominador)
        else:
            divisor=abs(self.__numerador)
            dividendo=abs(self.__denominador)
       
        if divisor==0:
            divisor=1
        resto=dividendo%divisor
        
        while resto!=0:
            dividendo=divisor
            divisor=resto
            resto=dividendo%divisor
        
        self.__numerador=int(self.__numerador/divisor)
        

        self.__denominador=int(self.__denominador/divisor)
        if self.__denominador==0:
            self.__denominador=1
    def __sub__(self,otro):
        resultado=None
        if type(otro)!=Fraccion:
            otro=Fraccion(otro,1)
        mult=self.__denominador*otro.getDenominador()
        dividir=mult/self.__denominador*self.__numerador
        dv=mult/otro.getDenominador()*otro.getNumerador()
        resultado=Fraccion(int(dividir-dv),int(mult)) 
        resultado.simplificar()
        return resultado   
    def __str__(self):
        return'{}/{}'.format(self.__numerador,self.__denominador)
    def __mul__(self,otro):
        resultado=None
        if type(otro)!=Fraccion:
            otro=Fraccion(otro,1)
        mult=self.__numerador*otro.getNumerador()
        multD=self.__denominador*otro.getDenominador()
        resultado=Fraccion(mult,multD)
        resultado.simplificar()
        return resultado
    def __truediv__(self,otro):
        resultado=None
        if type(otro)!=Fraccion:
            otro=Fraccion(otro,1)
        mult=self.__numerador*otro.getDenominador()
        multD=self.__denominador*otro.getNumerador()
        resultado=Fraccion(mult,multD)
        resultado.simplificar()
        return resultado
    def __rtruediv__(self,otro):
        resultado=None
        if type(otro)!=Fraccion:
            otro=Fraccion(otro,1)
        mult=self.__numerador*otro.getDenominador()
        multD=self.__denominador*otro.getNumerador()
        resultado=Fraccion(multD,mult)
        resultado.simplificar()
        return resultado
    def __radd__(self,otro):
        resultado=None
        if type(otro)!=Fraccion:
            otro=Fraccion(otro,1)
        mult=self.__denominador*otro.getDenominador()
        dividir=mult/self.__denominador*self.__numerador
        dv=mult/otro.getDenominador()*otro.getNumerador()
        resultado=Fraccion(int(dividir+dv),int(mult))
        resultado.simplificar()
        return resultado
    def __rsub__(self,otro):
        resultado=None
        if type(otro)!=Fraccion:
            otro=Fraccion(otro,1)
        mult=self.__denominador*otro.getDenominador()
        dividir=mult/self.__denominador*self.__numerador
        dv=mult/otro.getDenominador()*otro.getNumerador()
        resultado=Fraccion(int(dv-dividir),int(mult)) 
        resultado.simplificar()
        return resultado   
    def __rmul__(self,otro):
        resultado=None
        if type(otro)!=Fraccion:
            otro=Fraccion(otro,1)
        mult=self.__numerador*otro.getNumerador()
        multD=self.__denominador*otro.getDenominador()
        resultado=Fraccion(mult,multD)
        resultado.simplificar()
        return resultado
