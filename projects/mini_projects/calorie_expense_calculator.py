from enum import Enum

height = None
weight = None
age = None
sex = None

class Sex(Enum):
    MAN = "homme"
    WOMAN = "femme"

    
def activity():
    print("Choissisez une activité")
    print("----------------------------")
    print("1. Course a pied")
    print("2. Velo")
    print("3. Rameur")
    
def choice_activity():
    while True:
        rep = int(input("Votre choix (entrez le numero correspondant): "))
        if rep >= 1 and rep <=3:
            return rep
        else:
            print("Veuillez entrez un choix valide")
            
"""def verif_metrics(rep, interval_min, interval_max):
    while True:
        if rep >= interval_min and rep <= interval_max:
            return rep
        else:
            print(f"Veuillez entrez une valeur comprise entre {interval_min} et {interval_max}") 
"""
            
def input_metrics():
    while True:
        rep = int(input("Entrez votre taille en cm: "))
        
        if rep >= 1 and rep <= 250:
            height = rep
            rep = int(input("Entrez votre poids en kg: "))
            
            if rep >= 1 and rep <= 200:
                weight = rep
                rep = int(input("Entrez votre age en année: "))
                
                if rep >=1 and rep <= 125:
                    age = rep
                    rep=int(input("Entrez votre sexe (femme/homme): "))
                    
                    if rep.lower() == 'femme':
                        sex = "femme"
                    elif rep.lower() == "homme":
                        sex = "homme"
                    else:
                        print("Entrez un sexe valide (Homme ou Femme)")
                        
                else:
                    print("Veuillez entrez un age valide (compris entre 1 et 125)")
                
            else:
                print(f"Veuillez entrez un poids valide (comprise entre 1 et 200)")
                
        else:
            print(f"Veuillez entrez une taille valide (comprise entre 1 et 250)") 
        
        
    
def main():
    print(f"""-----------------------------
        --Calorie expenditure calculator
        -----------------------------------""")
    activity()
    choice = choice_activity()
    
if __name__ == "__main__":
    main()