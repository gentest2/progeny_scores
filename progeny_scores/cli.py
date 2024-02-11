import argparse
from tabulate import tabulate
from progeny_scores.analysis import get_progeny_scores

def main():
    parser = argparse.ArgumentParser(description='Get PROGENy scores for a given dataset.')
    parser.add_argument('slug', type=str, help='Slug name of the collection.')

    args = parser.parse_args()
    scores_df = get_progeny_scores(args.slug)

    print(tabulate(scores_df, headers='keys', tablefmt='psql'))

if __name__ == '__main__':
    main()
