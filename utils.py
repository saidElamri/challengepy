# utils.py

def associer_produits(prd, prix):
    """Associer chaque produit à son prix avec zip"""
    return list(zip(prd, prix))

def filtrer(liste):
    """Filtrer les produits dont le prix >= 30"""
    return [item for item in liste if item[1] >= 30]

def transformer(liste):
    """Transformer en chaînes avec f-string"""
    return [f"{p} coûte {x} DH" for p, x in liste]

def trier(liste):
    """Trier par ordre croissant des prix"""
    return sorted(liste, key=lambda item: item[1])

def en_tuple(liste):
    """Convertir en tuple"""
    return tuple(liste)

def produit_extremes(liste):
    """Retourner le moins cher et le plus cher"""
    moins_cher = min(liste, key=lambda x: x[1])
    plus_cher = max(liste, key=lambda x: x[1])
    return moins_cher, plus_cher

def transformer_luxe(liste):
    """Ajouter (LUXE) si prix > 1000"""
    return list(map(lambda item: f"{item[0]} coûte {item[1]} DH (LUXE)" if item[1] > 1000 
                    else f"{item[0]} coûte {item[1]} DH", liste))