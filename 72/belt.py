from audioop import reverse


scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score, scores=scores, belts=belts):
    if user_score < 10:
        return None

    for score, belt in zip(reversed(scores), reversed(belts)):
        if user_score >= score:
            return belt
