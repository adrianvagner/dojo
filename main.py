from  transforma_romano  import  romano
from  transforma_indo  import  indoara


num = int(input("Digite um número: "))


romano = romano().transformaRomano(num)

print(romano)

indoara = indoara().transformaIndoAra(str(romano))

print("Transformando em ROMANO");


print("NÚMERO EM ROMANO: " + romano);


print("Transformando em INDO-ARÁBICO");


print("NÚMERO EM INDO-ARÁBICO: " + str(indoara));