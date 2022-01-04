frase = 'curso em video python'
print(frase[3])#so uma letra
print(frase[3:13])#da letra 3 a letra 13
print(frase[:13])#do comeso ate o 13
print(frase[1:15:2])#pular de dois em dois do 1 ao 15
print(frase[::2])#nao sei o inicio e nem o fim e pula e, dois em dois

print("""hwpuihfwcjkedhnrowicfhowçiejhnr
fçwefhwoiufhnwfowe
woeicfnoiencw""") #com asparas triplas eu posso escrerver textos

print(frase.count('o'))# contar quantas vezes tem a letra no variavel
print(frase.upper())# deixa tuo maiusculo
print(frase.upper().count('o'))#cntar essa letra maiusculas
print(len(frase))#ver quantas letras tem a estring
print(len(frase.strip()))#nao conta os espaços indesejaveis
print(frase.replace('python', 'whattzap'))

frase.replace('python','whattzap')#isso nao modifica a estring 
print(frase)

#para salvar o resultado

frase2= frase.replace('python','whattzap')#assim salva a modificaçao
print(frase2)

print('curso' in frase)#para testa se tem essa paavra dentro da frase
print(frase.find('video'))#mostra a posicao
print(frase.lower().find('video'))#buscas em minusculo
print(frase.upper().find('video'))##uscar em maiusculo
print(frase.split())# trsforma a frase em listas

dividido = frase.split()#trsformo em variavl a lista
print(dividido)

print(dividido[0])#primeiro item da lista
print(dividido[2][3])

