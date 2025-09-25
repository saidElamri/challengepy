from data import produits, prix
import utils

# Étape 1
associes = utils.associer_produits(produits, prix)

# Étape 2
filtrés = utils.filtrer(associes)

# Étape 3
# (on garde la forme (produit, prix) pour trier correctement)
tries = utils.trier(filtrés)

# Étape 4 + 5
print("Liste triée :")
print(utils.transformer(tries))

# Étape 6
classement_tuple = utils.en_tuple(tries)
print("\nClassement final (tuple) :")
print(classement_tuple)

# Étape 7
moins_cher, plus_cher = utils.produit_extremes(tries)
print(f"\nProduit le moins cher : {moins_cher}")
print(f"Produit le plus cher : {plus_cher}")

# Étape 8 (bonus)
print("\nVersion avec LUXE si prix > 1000 :")
print(utils.transformer_luxe(tries))