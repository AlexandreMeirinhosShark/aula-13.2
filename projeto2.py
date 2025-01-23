from time import sleep                                                                                                                      
from random import choice, randint                                                                                                          
"""                                                                                                                                         
Eu fiz aqui um programa diferente                                                                                                           
Em vez de fazer no turtle, decidi fazer aqui mesmo                                                                                          
Quando o jogo finaliza, eu fiz com que desse erro intencionalmente                                                                          
Eu fiz um diálogo interessante.                                                                                                             
Se qiser, até pode jogá-lo sem problemas.                                                                                                   
"""                                                                                                                                         
                                                                                                                                            
def comp_print(text, skips=1):                                                                                                               
    for a in str(text):                                                                                                                     
        print(a, end="")                                                                                                                    
        sleep(0.05)                                                                                                                         
    if skips > 0:                                                                                                                           
        for b in range(int(skips)):                                                                                                         
            print()                                                                                                                         
                                                                                                                                            
                                                                                                                                            
comp_print("Olá, pequeno explorador. Parece que estás numa aventura para encontrar um tesouro...")                                          
comp_print("Para começares, tens que escolher dois caminhos, depois...", 2)                                                                 
comp_print('"Hmm. tenho que ver qual é o caminho certo..:"', 0)                                                                             
chose = (input()).lower()                                                                                                                   
if not (chose == "trás" or chose == "a trás" or chose == "atrás" or chose == "voltar"):                                                     
    if not(chose == "esquerda" or chose == "direita"):                                                                                      
        print("nao")                                                                                                                        
        yay = int("hello")                                                                                                                  
    if chose == "esquerda":                                                                                                                 
        comp_print("*tu vais para a esquerda*")                                                                                             
        comp_print("*encontras algo estranho*")                                                                                             
    elif chose == "direita":                                                                                                                
        comp_print("*tu vais para a direita*")                                                                                              
        comp_print("*sentes algo que te confunde...*")                                                                                      
    path = choice(["ponte perigosa", "floresta encantada"])                                                                                 
    comp_print(f"*foste para uma {path}.*", 2)                                                                                              
    if path == "ponte perigosa":                                                                                                            
        comp_print('"Acho que consigo passar por aqui."', 2)                                                                                
        prob = randint(1, 5)                                                                                                                
        if prob <= 2:                                                                                                                       
            comp_print("*caíste da ponte, morreste*")                                                                                       
            print('_______   _______  .        .')                                                                                          
            print('|            |     |\      /|')                                                                                          
            print('|---         |     | \    / |')                                                                                          
            print('|            |     |  \  /  |')                                                                                          
            print('|         ___|___  |   \/   |')                                                                                          
            yay = int("hello")                                                                                                              
        else:                                                                                                                               
            comp_print("*conseguiste passar, encontras algo invugar...*")                                                                   
    elif path == "floresta encantada":                                                                                                      
        comp_print("*encontras-te maravilhado pela paisagem bonita com fadas, animais e magia*")                                            
        comp_print("*de repente, és surpreendido por uma coisa*")                                                                           
    path2 = choice([" tesouro", "a criatura estranha"])                                                                                     
    comp_print(f"*encontras um{path2}*")                                                                                                    
    if path2 == " tesouro":                                                                                                                 
        print("*abres a arca*")                                                                                                             
        for i in range(randint(1, 20)):                                                                                                     
            comp_print(f"Encontraste uma moeda: {i+1}")                                                                                     
        comp_print('"Tantas moedas que encontrei..."')                                                                                      
        comp_print('"Acho que estou a ficar rico."')                                                                                        
        print('_______   _______  .        .')                                                                                              
        print('|            |     |\      /|')                                                                                              
        print('|---         |     | \    / |')                                                                                              
        print('|            |     |  \  /  |')                                                                                              
        print('|         ___|___  |   \/   |')                                                                                              
        yay = int("hello")                                                                                                                  
    elif path2 == "a criatura estranha":                                                                                                    
        comp_print("👹Olá.")                                                                                                                 
        comp_print('"Ah, que susto..."')                                                                                                    
        comp_print('"Quem és?"')                                                                                                            
        comp_print(f"👹Sou o guardião desta {path}.")                                                                                        
        comp_print('"Tenho que dair daq-"')                                                                                                 
        comp_print("👹Não não, menino. Tens que adivinhar o número secreto, depois eu deixo-te.")                                            
        rand = randint(1, 20)                                                                                                               
        guess = 0                                                                                                                           
        while not rand == guess:                                                                                                            
            try:                                                                                                                            
                guess = int(input("*escolhes um número*:"))                                                                                 
                if not 0 < guess < 21:                                                                                                      
                    comp_print("👹O número tem que ser entre 1 e 20.")                                                                       
                elif not rand == guess:                                                                                                     
                    comp_print(choice(["👹Não.", "👹Ainda não.", "👹Tenta outra vez...", "👹Errado."]), 2)                                      
            except ValueError:                                                                                                              
                comp_print("👹Acho que isso não é um número...")                                                                             
        comp_print("👹Acertaste!")                                                                                                           
        comp_print('"Finalmente. Eu posso sair daqui."')                                                                                    
        print('_______   _______  .        .')                                                                                              
        print('|            |     |\      /|')                                                                                              
        print('|---         |     | \    / |')                                                                                              
        print('|            |     |  \  /  |')                                                                                              
        print('|         ___|___  |   \/   |')                                                                                              
        yay = int("hello")                                                                                                                  
else:                                                                                                                                       
    comp_print('"Acho que é melhor voltar para casa."')                                                                                     
    comp_print('"O que mais vale estar em aventuras do que ficar em casa?"')                                                                
    comp_print('"Acho que é hora de sair daqui."')                                                                                          
    comp_print("Encontraste o fim secreto :) Muito bem!")                                                                                   
    print('_______   _______  .        .')                                                                                                  
    print('|            |     |\      /|')                                                                                                  
    print('|---         |     | \    / |')                                                                                                  
    print('|            |     |  \  /  |')                                                                                                  
    print('|         ___|___  |   \/   |')                                                                                                  
    yay = int("hello")                                                                                                                                                                                                         
