
'''
@Autor :     Yuri Domingos ( ID : 21711 )
Data   : 6 - 11 - 2020
UCAN   : Universidade Catolica de Angola
Objectivo : Resolver o classico problema dos canibais

'''


estadoInicial = [3,3,0,0,0]

Operadores = [(1,0),(1,1),(2,0),(0,2)]

fronteira= []

visitados = []



def Barco_Movement(nState , numberMissionario=0, numberCanibais=0) :


    if numberMissionario + numberCanibais > 2 :

        return

    if nState [-1] == 0 :
    

        missionario_Origem  = 0
        Canibal_Origem  = 1
        missionario_Destino = 2
        Canibal_Destino = 3

    else :
    
      missionario_Origem = 2
      Canibal_Origem = 3
      missionario_Destino = 0
      Canibal_Destino = 1
        

    if nState[ missionario_Origem ] == 0 and nState[Canibal_Origem ] == 0 :
                
        return

      # Atualizando a posicao do barco em relacao a margem 

    nState[-1] = 1-nState[-1]

      
    for i in range(min( numberMissionario, nState[ missionario_Origem])) :
            
         nState [missionario_Origem  ] -= 1
         nState [missionario_Destino ] += 1

     


    for i in range(min(numberCanibais ,nState [Canibal_Origem])) :

       nState [Canibal_Origem ] -= 1
       nState [Canibal_Destino] += 1

    # done
    # 
    return nState      

    

def proximoElemento(estado):

    proximoElemento = []

    for (i,j) in Operadores :

        receive = Barco_Movement(estado[:],i,j)

        if   receive == None : continue

        if (  receive [0] <  receive [1] and receive [0] > 0 ) or ( receive [2] <receive [3] and  receive [2] > 0 ) : continue

        if  receive in visitados : continue

        proximoElemento.append(receive)

    return proximoElemento
    

def VizinhosNaoVisitados(ElementoPorAnalisar):
    
    receive = proximoElemento (ElementoPorAnalisar)

    if len(receive) > 0 :

        return receive[0]

    else :
        return -1


def VerificaObjectivo(estado):
    
    if estado[2] >=3 and estado[3] >= 3 :

        return True
    else :

        return False


def dfs(estadoInicial) :

    fronteira.append(estadoInicial)
  

    while len(fronteira) != 0 :

        ElementoAnalisar = fronteira[len(fronteira)-1]

      

        if VerificaObjectivo(ElementoAnalisar) : break

         
        values = VizinhosNaoVisitados( ElementoAnalisar)

        if  values == -1 :

            fronteira.pop()
        else :

            visitados.append(values)
            fronteira.append(values)
    

    else :
    
        
        print("Error ! Not found")
        
    print(visitados)     

    return fronteira


main_Operations = dfs(estadoInicial)

#print(main_Operations)


for i in range(1, len(main_Operations)):
    
    missionario_Destino = abs(main_Operations[i][0]-main_Operations [i-1][0])
    Canibal_Destino     = abs(main_Operations [i][1]-main_Operations [i-1][1])

    barco = main_Operations [i][4]-main_Operations [i-1][4]

    if barco == 1 :
        String_format = "->"
    else :
        String_format = "<-"
    
    print(main_Operations[i-1],"({},{},{}".format(missionario_Destino,Canibal_Destino,String_format))
      





      
