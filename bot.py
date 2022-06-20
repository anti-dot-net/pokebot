from mastodon import Mastodon
import pokebase as pb
import random as rand
import scehdule
import time

mastodon = Mastodon(
	access_token = 'token.secret'
	api_base_url = 'https://tavern.antinet.work'
)

def pkmn_otd():
	
	pokemon_id = rand.randint(1,151)
	pokemon_name = pb.pokemon(pokemon_id)
	pokemon_sr = pb.SpriteResource('pokemon', pokemon_id)
	pokepon_img = pokemon_sr.img_data
