poids_cuit= int(input("Entrez le poids du produit après cuisson (en gramme): "))
calories_total= int(input("Entrez les calories totales du produit cru: "))
glucides_total= int(input("Entrez la quantité de glucide total du produit cru (en gramme): "))
lipides_total= int(input("Entrez la quantité de lipide total du produit cru (en gramme): "))
proteines_total= int(input("Entrez la quantité de proteine total du produit cru (en gramme): "))

# Calories et macronutriments au 100g cuit
diviseur = poids_cuit/100
calories = round(calories_total / diviseur)
glucides = round(glucides_total / diviseur)
lipides = round(lipides_total / diviseur)
proteines = round(proteines_total  / diviseur)
print(f"""
      Macronutriments pour 100g cuit
      =============================
      Calories: {calories} kcal
      Glucides: {glucides}g
      Lipides: {lipides}g
      Proteines: {proteines}g
      """)