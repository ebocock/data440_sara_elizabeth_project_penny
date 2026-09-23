# This file will generate an array for each deck and store the card decks
from pathlib import Path
import numpy as np
import json
import datetime as dt


PATH_DECKS = Path('data/decks/')
PATH_SEED_LOG = Path('data/seed.json')
SEED_BASE = 1693

def make_decks(seed: int, 
               n_cards: int,
               n_decks: int
              ) -> np.ndarray:
    '''
    This code makes and shuffles the decks.
    '''
    rng = np.random.default_rng(seed)
    num_each_card = n_cards // 2

    decks = np.empty((n_decks, n_cards), dtype = np.int8)

    for i in range(n_decks):
        deck = np.concatenate([
            np.zeros(num_each_card, dtype = np.int8),
            np.ones(num_each_card, dtype = np.int8)
        ])
        rng.shuffle(deck)

        decks[i] = deck
    
    return decks


def get_next_seed() -> int:
    '''
    Read the last seed used, increment by 1,
    and update seed.json.
    '''
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
        'seed_time': str(dt.datetime.now())
    }
    with PATH_SEED_LOG.open('w') as f:
        json.dump(seed_log, f)
    
    return seed



def save_decks(decks: np.ndarray, 
               seed: int
              ) -> Path:
    '''
    Saves all decks from one simulation call to one file.
    '''
    PATH_DECKS.mkdir(parents=True, exist_ok=True)

    n_decks = decks.shape[0]
    n_cards = decks.shape[1]

    filename = PATH_DECKS / f'decks_{n_decks}x{n_cards}_seed_{seed}.npy'

    np.save(filename, decks)

    return filename


def generate_decks(n_cards: int, n_decks: int) -> tuple[np.ndarray, int, str]:
    seed = get_next_seed()

    decks = make_decks(
        seed = seed,
        n_decks = n_decks,
        n_cards = n_cards
    )

    filepath = save_decks(
        decks = decks,
        seed = seed
    )
    return decks, seed, filepath

def more_decks(n: int) -> str:
    print(f'Creating {n} more decks')
    decks, seed, filepath = generate_decks(52, n)
    print(f'{n} decks saved to {filepath}.')
    return filepath

def main():
    # Generates 1 million decks
    n_cards = 52
    n_decks = 100

    # Generate decks
    decks, seed, filepath = generate_decks(
        n_cards=n_cards,
        n_decks=n_decks
    )

    # Print results
    print(f"Seed: {seed}")
    print(f"Saved to: {filepath}")

if __name__ == "__main__":
    main()
