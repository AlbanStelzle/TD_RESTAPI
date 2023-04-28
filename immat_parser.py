def immatParser(immat: str):
    # - possède une méthode publique `is_valid` qui retourne `True` si l'immatriculation est valide, `False` sinon.
    if len(immat) != 12:
        # Une immatriculation est valide si elle est composée de 12 caractères :
        return False
    if immat[2] != '-':
        # - un tiret
        return False

    weight = int(immat[:2])
    country_code = immat[3:5]
    farm_code = immat[5:8]
    day = int(immat[8:10])
    month = immat[10:]

    if weight % 5 != 0:
        # Vérifie si le poids est divisible par 5
        return False

    if country_code not in ["FR", "BE", "DE", "LU", "CH", "IT", "ES"]:
        # Vérifie si le code du pays est valide
        return False

    if farm_code == farm_code[::-1]:
        # Vérifie si c'est un palindrome
        return False

    if not (1 <= day <= 31):
        # - deux chiffres allant de O1 à 31 (jour de ponte)
        print(day)
        return False

    valid_months = ["JA", "FE", "MA", "AV", "MI", "JU", "JL", "AO", "SE", "OC", "NO", "DE"]

    if month not in valid_months:
        # - deux lettres indiquant le mois de ponte ("JA", "FE", "MA", "AV", "MI", "JU", "JL", "AO", "SE", "OC",
        # "NO", "DE")
        return False

    if day == valid_months.index(month) + 1:
        return False

    return True


def immat_parser():
    return None