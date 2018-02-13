def get_input():
    done = False
    while not done:
        try:
            points = int(input('How many points does the post have?: '))
            if points > 0:
                ratio = int(input('What is the percentage of users who upvoted the post?: '))
                done = True
            else:
                print('Reddit does not currently display percentages for zero or negative scores.')
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
