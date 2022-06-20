from mastodon import Mastodon
import pokebase as pb
import random as rand
import schedule
import time

#Start up Mastodon

mastodon = Mastodon(
	access_token = 'token.secret',
	api_base_url = 'https://tavern.antinet.work'
)

#Define Pokemon of the Day Function

def pkmn_otd(self):
	
	#Pick a random pokemon id
	
	pokemon_id = rand.randint(1,151)
	
	#Get that pokemon's name
	
	pokemon_name = pb.pokemon(pokemon_id)
	
	#Pull that pokemons sprite and get the image data for mastodon
	
	pokemon_sr = pb.SpriteResource('pokemon', pokemon_id)
	pokemon_img = pokemon_sr.img_data
	
	#create a media post to obtain media_id
	
	img_dict = Mastodon.media_post(media_file = pokemon_img, mime_type = '.jpeg')
	
	pokemon_text = (('~~~ ')+(pokemon_name)+(' is the Pokemon of the Day!~~~'))
	
	mastodon.post_status(pokemon_text)
	
	
pkmn_otd()
