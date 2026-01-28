#!/usr/bin/python3

# ==================
# CONSTANTES
# ==================

INGREDIENTS_BASE = {
        "oeuf" : 1,         # en unites
        "sucre" : 40,       # en grammes
        "beurre" : 37.5,    # en grammes
        "chocolat" : 50,    # en grammes
        "farine" : 10       # en grammes
}

TEMPS_CUISSON = 30          # en minutes
TEMPERATURE = 150           # en degres

# ====================
# FONCTIONS
# ====================
def affichage_recette(proportion):
    
    
    print(f"""
          
    
    Ingredients:
    
    Oeufs: {INGREDIENTS_BASE['oeuf']*proportion}    
    Chocolat: {INGREDIENTS_BASE['chocolat']*proportion}g
    Beurre: {INGREDIENTS_BASE['beurre']*proportion}g
    Sucre: {INGREDIENTS_BASE['sucre']*proportion}g
    Farine: {INGREDIENTS_BASE['farine']*proportion}g
    
    Prepartion:
    
    1. Prechauffer le four, chaleur tournante a {TEMPERATURE} degres
    2. Faire fondre le beurre et le chocolat a feu moyen dans une casserole
    3. Melanger le reste des ingedients
    4. Incorporer progressivent le melange fondu avec le reste (c'est important pour eviter de cuire les oeufs)
    5. Dans un moule chemise de papier cuisson, verser la pate
    6. Une fois le prechauffage fini, enfourner
    
    Cuisson:

    {TEMPS_CUISSON} minutes a {TEMPERATURE}*C
    """)    

def demande_proportion():
    while True:
    
        # Evite les quantite negatives et les chaines de caracteres
        try:
            proportion = int(input("Entrez la proportion souhaitez: "))
            
            if proportion <= 0:
                raise ValueError("La valeur doit etre positive")
            
            return proportion
        
        except ValueError as e:
            print(f"Erreur: {e}")
            
        except KeyboardInterrupt:
            print("Au revoir")
            exit(0)

# ==================
# EXECUTION
# ==================       
proportion = demande_proportion()
affichage_recette(proportion)


    