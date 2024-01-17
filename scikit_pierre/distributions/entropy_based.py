from collections import Counter
from math import log2


def global_local_entropy_based(items: dict) -> dict:
    """
    The Global and Local Entropy Based - (GLEB). The reference for this implementation are from:

    - <In process>

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    numerator = {}
    denominator = {}

    def global_entropy():
        genre_list = [
            category
            for index, item in items.items()
            for category, genre_value in item.classes.items()
        ]

        n = len(genre_list)
        total = dict(Counter(genre_list))
        return {t: total[t] / n for t in dict(total)}

    def compute():
        for index, item in items.items():
            for category, genre_value in item.classes.items():
                ent = -(genre_global[category] * genre_value)*log2(genre_global[category] * genre_value)
                numerator[category] = numerator.get(category, 0) + item.score * ent
                denominator[category] = denominator.get(category, 0) + item.score

    def genre(g):
        if (g in denominator.keys() and denominator[g] > 0.0) and (g in numerator.keys() and numerator[g] > 0.0):
            return numerator[g] / denominator[g]
        else:
            return 0.00001

    genre_global = global_entropy()
    compute()
    distribution = {g: genre(g) for g in numerator}
    return distribution


def global_local_entropy_based_with_probability_property(items: dict) -> dict:
    """
    The Global and Local Entropy Based with Probability Property - (GLEB_P).
    The reference for this implementation are from:

    - <In process>

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    distribution = global_local_entropy_based(items)
    total = sum(distribution.values())
    final_distribution = {g: value / total for g, value in distribution.items()}
    return final_distribution


# ############################################################################################### #
# ######################################### Unrevised ########################################### #
# ############################################################################################### #