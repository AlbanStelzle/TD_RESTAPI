from pydantic import BaseModel, validator
from immat_parser import immatParser


class ModelEgg(BaseModel):
    origine: str
    couleur: str
    immatriculation: str

    @validator("couleur")
    def validate_couleur(cls, couleur):
        if couleur not in ["gris", "brun", "blanc"]:
            raise ValueError("Couleur invalide")

        return couleur

    @validator("immatriculation")
    def validate_immatriculation(cls, immatriculation: str):
        check = immatParser(immatriculation)
        if check:
            return immatriculation
        raise ValueError("Immatriculation invalide")
