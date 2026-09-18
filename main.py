from src.datagen import generate_decks


def main():
    # Small test
    n_cards = 10
    n_decks = 3

    # Generate decks
    decks, seed, filepath = generate_decks(
        n_cards=n_cards,
        n_decks=n_decks
    )

    # Print results
    print(f"Seed: {seed}")
    print(f"Saved to: {filepath}")
    print("\nGenerated decks:")

    for i, deck in enumerate(decks):
        print(f"Deck {i + 1}: {deck}")


if __name__ == "__main__":
    main()