#make a csv file with random names and locations and keep ID and x and y coords
import csv
import random
import string
import itertools
import pandas as pd
npoints = 10083
adjectives = [
    "Mystical", "Enchanted", "Ancient", "Forbidden", "Whispering", "Celestial",
    "Arcane", "Hidden", "Ethereal", "Shrouded", "Legendary", "Forgotten",
    "Timeless", "Spectral", "Shadowy", "Luminous", "Serene", "Abyssal",
    "Haunted", "Secluded", "Sacred", "Chimerical", "Decayed", "Pristine",
    "Tempestuous", "Eldritch", "Crystalline", "Malevolent", "Hallowed",
    "Bizarre", "Vibrant", "Untamed", "Frozen", "Dusky", "Lush", "Dazzling",
    "Sanguine", "Tranquil", "Gleaming", "Ravaged", "Desolate", "Flourishing",
    "Baleful", "Phantasmal", "Turbulent", "Verdant", "Fabled", "Labyrinthine",
    "Opulent", "Parched", "Twinkling", "Vast", "Dreamlike", "Primeval",
    "Gloomy", "Inviting", "Volcanic", "Nocturnal", "Sunken", "Tumultuous",
    "Roaring", "Sublime", "Bleak", "Iridescent", "Rustic", "Murmuring",
    "Sinister", "Majestic", "Lurking", "Brilliant", "Azure", "Barren",
    "Swirling", "Heaving", "Glistening", "Cavernous", "Winding", "Whispered",
    "Forsaken", "Resplendent", "Idyllic", "Brooding", "Mirrored", "Stormy",
    "Perilous", "Wistful", "Tenebrous", "Humming", "Infinite", "Wraithlike",
    "Looming", "Nautical", "Intertwined", "Blazing", "Exotic", "Bewitched",
    "Drifting", "Silvered", "Hazy", "Uncharted", "Stony", "Venerable",
    "Ephemeral", "Insidious", "Tangled", "Shimmering", "Searing", "Imposing",
    "Gargantuan", "Quaint", "Foggy", "Glacial", "Stark", "Obsidian", "Titanic",
    "Mysterious", "Unforgiving", "Charmed", "Serpentine", "Rugged", "Moaning",
    "Bountiful", "Lethal", "Thorny", "Flickering", "Starlit", "Magnificent",
    "Placid", "Overgrown", "Moldering", "Painted", "Contorted", "Sweltering",
    "Moonlit", "Shattered", "Bejeweled", "Derelict", "Tidal", "Dwindling",
    "Quivering", "Frigid", "Enigmatic", "Tempered", "Zephyrous", "Rhapsodic",
    "Inverted", "Scalding", "Lavish", "Scorched", "Flourishing", "Petrified",
    "Subterranean", "Radiant", "Bubbling", "Pallid", "Monolithic", "Fragrant",
    "Watery", "Harmonious", "Delirious", "Hollow", "Divine", "Stealthy",
    "Glassy", "Reverberating", "Spacious", "Withered", "Crumbling", "Arctic",
    "Cascading", "Swollen", "Golden", "Dismal", "Warped", "Infested", "Soaring",
    "Cobalt", "Gilded", "Coiling", "Reflective", "Misty", "Ominous", "Sandy",
    "Exquisite", "Undulating", "Portentous", "Luxuriant", "Dilapidated",
    "Colossal", "Smoldering", "Whispering", "Smoky", "Sparkling", "Pulsing",
    "Gritty", "Meandering", "Precarious", "Asymmetrical", "Subterranean",
]

locations = [
    "Abyss", "Acropolis", "Archipelago", "Atoll", "Badlands", "Barrow", "Basin",
    "Battleground", "Bayou", "Beach", "Bivouac", "Bog", "Borough", "Boutique",
    "Bunker", "Burrow", "Canyon", "Cape", "Castle", "Catacomb", "Cavern", "Chapel",
    "Chateau", "Citadel", "Cliff", "Cloister", "Colosseum", "Conclave", "Cove",
    "Crater", "Creek", "Crescent", "Dale", "Dell", "Den", "Depot", "Desert",
    "Domain", "Dome", "Dune", "Dungeon", "Enclave", "Estuary", "Expanse", "Falls",
    "Fen", "Fiefdom", "Field", "Fjord", "Flats", "Forest", "Forge", "Fort",
    "Frontier", "Frost", "Garden", "Garrison", "Gate", "Geyser", "Glade", "Glen",
    "Gorge", "Grove", "Guild", "Gulch", "Gulf", "Hamlet", "Harbor", "Haven",
    "Heath", "Hedge", "Highland", "Hill", "Hinterland", "Hold", "Hollow", "Isle",
    "Jungle", "Keep", "Kingdom", "Knoll", "Labyrinth", "Lake", "Landing", "Ledge",
    "Manor", "Maze", "Meadow", "Mesa", "Mire", "Monastery", "Monolith", "Monument",
    "Moor", "Mountain", "Necropolis", "Nook", "Oasis", "Obelisk", "Orchard",
    "Outpost", "Palace", "Pantry", "Paradise", "Park", "Pass", "Pasture", "Path",
    "Peak", "Peninsula", "Pit", "Plateau", "Plaza", "Pond", "Prairie", "Precinct",
    "Quarry", "Quarters", "Ranch", "Range", "Ravine", "Reef", "Refuge", "Reliquary",
    "Ridge", "River", "Road", "Rookery", "Ruins", "Sanctuary", "Sanctum", "Savanna",
    "Scar", "Sea", "Sect", "Sepulcher", "Shack", "Shambles", "Shrine", "Sierra",
    "Sound", "Spire", "Spring", "Square", "Steppes", "Stronghold", "Summit", "Swamp",
    "Tavern", "Temple", "Terrace", "Thicket", "Throne", "Tomb", "Tower", "Town",
    "Trail", "Tundra", "Vale", "Valley", "Vault", "Village", "Vista", "Volcano",
    "Ward", "Warren", "Waste", "Waterfall", "Waters", "Well", "Wetlands", "Wilds",
    "Woods", "Ziggurat"
]






  

# Function to generate anagrams
def generate_anagrams(source, number):
    anagrams = set()  # Use a set to avoid duplicates
    source_letters = list(source.replace(" ", ""))  # Remove spaces and make a list of letters

    # Keep generating anagrams until we reach the desired number
    while len(anagrams) < number:
        random.shuffle(source_letters)  # Randomly shuffle the letters
        anagrams.add(''.join(source_letters))  # Add the shuffled letters as a string to the set

    return list(anagrams)  # Convert the set to a list to return

# Generate 11,000 anagrams from "Salem Oregon"
anagrams = generate_anagrams("salem oregon", npoints)


# Create all possible combinations and format them as "<adjective> <location>"
all_combinations = [' '.join(comb) for comb in itertools.product(adjectives, locations)]

# Shuffle the list of combinations to ensure randomness
random.shuffle(all_combinations)

# Select the first npoints unique combinations
names = all_combinations[:npoints]

# create a list of random risk levels
riskLevels = ['You should be fine.', 'You might want to bring a friend.', 'You should bring a group.', 'You should bring a group and a guide.','You should bring a group, a guide, and a weapon.',  'You should bring a group, a guide, a weapon, and a healer.','This is probably your last adventure.']

# generate an array of random risk levels for each point
risks =  random.choices(riskLevels, k=npoints)


csv_file_path = 'Manholes-Salem.csv'

df = pd.read_csv(csv_file_path)

column_name = 'X' 
x_data = df[column_name].tolist()
column_name = 'Y' 
y_data = df[column_name].tolist()
column_name = 'UNITID' 
id_data = df[column_name].tolist()



 # Open a new CSV file for writing
with open('porthales.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['Code Name', 'Portal Destination', 'Risk Level', 'ID','X-coord','Y-coord'])

    # Write the data rows
    for values in zip(anagrams, names, risks, id_data, x_data, y_data):
        writer.writerow(values)

