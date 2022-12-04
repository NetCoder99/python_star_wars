import json
from typing import List
from datetime import datetime
from jsonpath_ng.ext import parse

from models.json.abstract_loader import loadFromJson

class film_json(loadFromJson):
    title: str = None
    episode_id: str = None
    opening_crawl: str = None
    director: str = None
    producer: str = None
    release_date: str = None
    characters: List[str] = None
    planets: List[str] = None
    starships: List[str] = None
    vehicles: List[str] = None
    species: List[str] = None
    created: datetime = None
    edited: datetime = None
    url: str = None
    desc: str = None

    def __init__(self, 
        title: str = None,
        episode_id: str = None,
        opening_crawl: str = None,
        director: str = None,
        producer: str = None,
        release_date: str = None,
        characters: List[str] = None,
        planets: List[str] = None,
        starships: List[str] = None,
        vehicles: List[str] = None,
        species: List[str] = None,
        created: datetime = None,
        edited: datetime = None,
        url: str = None,
        desc: str = None,
    ):
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl = opening_crawl
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.characters = characters
        self.planets = planets
        self.starships = starships
        self.vehicles = vehicles
        self.species = species
        self.created = created
        self.edited = edited
        self.url = url
        self.desc = desc
   
    @classmethod
    def fromJson(cls, json_str):
        try:
            json_exp = parse("$.film")
            json_match = json_exp.find(json_str)[0]
            return cls (
                title = json_match.value['title'],
                episode_id = json_match.value['episode_id'],
                opening_crawl = json_match.value['opening_crawl'],
                director = json_match.value['director'],
                producer = json_match.value['producer'],
                release_date = json_match.value['release_date'],
                characters = json_match.value['characters'],
                planets = json_match.value['planets'],
                starships = json_match.value['starships'],
                vehicles = json_match.value['vehicles'],
                species = json_match.value['species'],
                created = json_match.value['created'],
                edited = json_match.value['edited'],
                url = json_match.value['url'],
                desc = json_match.value['desc']
            )
        except Exception as ex:
            print(f'ex:{ex}')
            return None

    def setTitle(self, title: str):
        self.title = title
        return self

    def toCsv(self):
        return '"{}","{}","{}","{}","{}","{}","{}","{}"'.format(
            self.title,
            self.episode_id,
            self.opening_crawl,
            self.director,
            self.producer,
            self.release_date,
            self.characters,
            self.planets,
            self.starships,
            self.vehicles,
            self.species,
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