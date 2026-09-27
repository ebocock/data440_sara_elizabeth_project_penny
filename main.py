#imports
from src.datagen import more_decks
from src.datavis import display_heatmaps
#from src.record_storing import PATH_RESULTS_COUNTS
from src.gameplay import process_added_decks
    
# Main
def main():
    print('Welcome to the Project Penny Simulation')
    first_action = input('\t Type 0 to display the most up-to-date heatmaps,\n' \
    '\t Type 1 to generate more decks:')
    if first_action == '0':
        display_heatmaps()

    elif first_action == '1':
        n_decks = int(input('\t Enter the number of decks you would like to generate: '))
        filepath = more_decks(n_decks)
        process = input(f'\t You now have {n_decks} unprocessed decks.\n' \
                        '\t select 0 to process: ')
        if process == '0':
            process_added_decks(filepath)
            heatmap_q = input(f'\t Just processed {n_decks}, input 0 to display updated heatmaps: ')
            if heatmap_q == '0':
                display_heatmaps()

if __name__ == "__main__":
    main()
