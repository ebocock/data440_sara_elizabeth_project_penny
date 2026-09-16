# This file will generate an array for each deck and store the card decks
from pathlib import Path
import numpy as np
import json
import datetime as dt


PATH_DECKS = Path('data/decks/')
PATH_SEED_LOG = Path('data/seed.json')
SEED_BASE = 1693

def make_decks(seed: int, 
               n_cards: int
              ) -> np.ndarray:
    '''
    This code makes one deck and shuffles it.
    '''
    rng = np.random.default_rng(seed)
    num_each_card = n_cards/2

    unshuffled = np.concatenate([np.zeros(num_each_card, dtype=int), np.ones(num_each_card, dtype=int)])
    shuffled = rng.shuffle(unshuffled)
    return shuffled



'''
def get_next_seed() -> int:
    #
    #Read the last seed used, increment by 1,
    #and update seed.json.
    #
    # Ensure the parent directory(ies) exists
    PATH_SEED_LOG.parent.mkdir(parents=True, exist_ok=True)

    # Determine the next seed
    if not PATH_SEED_LOG.exists():
        print(f'No seed log found, starting with {SEED_BASE}')
        seed = SEED_BASE
    else:
        with PATH_SEED_LOG.open('r') as f:
            seed_log = json.load(f)
        seed = seed_log['seed'] + 1
    
    # Update the log
    seed_log = {
        'seed': seed,
        'seed_time': str(dt.now())
    }
    with PATH_SEED_LOG.open('w') as f:
        json.dump(seed_log, f)
    
    return seed

def save_decks(decks: np.ndarray, 
               seed: int
              ) -> Path:
    #
    This doesn't actually save anything,
    it is just a demo of how I might construct
    the filename.
    #
    PATH_DECKS.mkdir(parents=True, exist_ok=True)

    n_decks = decks.shape[0]
    n_cards = decks.shape[1]

    filename = PATH_DECKS / f'decks_{n_decks}x{n_cards}_seed_{seed}.something'
    print(f'I might save this file like: {filename}')
    return filename
'''