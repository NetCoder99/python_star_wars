import json
from typing import List
from datetime import datetime

from models.json.abstract_loader import loadFromJson
from utilities.getJsonValue import json_helpers

class people_json(loadFromJson):
    name: str = None
    height: str = None
    mass: str = None
    hair_color: str = None
    skin_color: str = None
    eye_color: str = None
    birth_year: str = None
    gender: str = None
    homeworld: str = None
    films: List[str] = None
    species: List[str] = None
    vehicles: List[str] = None
    starships: List[str] = None
    created: datetime = None
    edited: datetime = None
    url: str = None
    desc: List[str] = None

    def __init__(self, 
        name: str = None,
        height: str = None,
        mass: str = None,
        hair_color: str = None,
        skin_color: str = None,
        eye_color: str = None,
        birth_year: str = None,
        gender: str = None,
        homeworld: str = None,
        films: List[str] = None,
        species: List[str] = None,
        vehicles: List[str] = None,
        starships: List[str] = None,
        created: datetime = None,
        edited: datetime = None,
        url: str = None,
        desc: List[str] = None
    ):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.films = films
        self.species = species
        self.vehicles = vehicles
        self.starships = starships
        self.created = created
        self.edited = edited
        self.url = url
        self.desc = desc
   
    @classmethod
    def fromJson(cls, json_str):
        try:
            return cls (
                name       = json_helpers.getJsonValue(json_str,'name'),
                height     = json_helpers.getJsonValue(json_str,'height'),
                mass       = json_helpers.getJsonValue(json_str,'mass'),
                hair_color = json_helpers.getJsonValue(json_str,'hair_color'),
                skin_color = json_helpers.getJsonValue(json_str,'skin_color'),
                eye_color  = json_helpers.getJsonValue(json_str,'eye_color'),
                birth_year = json_helpers.getJsonValue(json_str,'birth_year'),
                gender     = json_helpers.getJsonValue(json_str,'gender'),
                homeworld  = json_helpers.getJsonValue(json_str,'homeworld'),
                films      = json_helpers.getJsonValue(json_str,'films'),
                species    = json_helpers.getJsonValue(json_str,'species'),
                vehicles   = json_helpers.getJsonValue(json_str,'vehicles'),
                starships  = json_helpers.getJsonValue(json_str,'starships'),
                created    = json_helpers.getJsonValue(json_str,'created'),
                edited     = json_helpers.getJsonValue(json_str,'edited'),
                url        = json_helpers.getJsonValue(json_str,'url'),
                desc       = json_helpers.getJsonValue(json_str,'desc')
            )
        except Exception as ex:
            print(f'ex:{ex}')
            raise ex

    def toCsv(self):
        return '"{}","{}","{}","{}","{}","{}","{}","{}"'.format(
            self.name,
            self.height,
            self.mass,
            self.hair_color,
            self.skin_color,
            self.eye_color,
            self.birth_year,
            self.gender,
            self.homeworld,
            self.films,
            self.species,
            self.vehicles,
            self.starships,
            self.created,
            self.edited,
            self.url,
            self.desc
        )

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)

    def toJsonDb(self):
        return "'{" + '"' + self.__class__.__name__ + '":' + \
                 json.dumps(self, default=lambda o: o.__dict__, indent=2).replace("'", '"') + "}'" 

