def get_input():
    while True:
        try:
            points = int(input('How many points does the post have?: '))
            ratio = int(input('What is the percentage of users who upvoted the post?: '))
            break
        except ValueError:
            print('Your values must be integers.')
    return points, ratio

def reddit_votes(points, ratio):
    votes = points / ((ratio / 50) - 1)
    upvotes = votes * (ratio / 100)
    downvotes = votes - upvotes
    return round(upvotes) + round(downvotes), round(upvotes), round(downvotes)

def print_output(votes, upvotes, downvotes):
    if votes == 1:
        print(votes, 'vote.')
    else:
        print(votes, 'votes.')

    if upvotes == 1:
        print(upvotes, 'upvote.')
    else:
        print(upvotes, 'upvotes.')

    if downvotes == 1:
        print(downvotes, 'downvote.')
    else:
        print(downvotes, 'downvotes.')

def main():
    points, ratio = get_input()
    total_votes, upvotes, downvotes = reddit_votes(points, ratio)
    print_output(total_votes, upvotes, downvotes)

main()
