def class_weighted_strategy(items: dict) -> dict:
    """
    The Class Weighted Strategy - (CWS). The reference for this implementation are from:

    - Silva et. al. (2021). https://doi.org/10.1016/j.eswa.2021.115112

    - Kaya and Bridge (2019). https://doi.org/10.1145/3298689.3347045

    - Steck (2018). https://doi.org/10.1145/3240323.3240372

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    numerator = {}
    denominator = {}

    def compute():
        for index, item in items.items():
            for genre, genre_value in item.classes.items():
                numerator[genre] = numerator.get(genre, 0) + item.score * genre_value
                denominator[genre] = denominator.get(genre, 0) + item.score

    def genre(g):
        if (g in denominator.keys() and denominator[g] > 0.0) and (g in numerator.keys() and numerator[g] > 0.0):
            return numerator[g] / denominator[g]
        else:
            return 0.00001

    compute()
    distribution = {g: genre(g) for g in numerator}
    return distribution


def weighted_probability_strategy(items: dict) -> dict:
    """
    The Weighted Probability Strategy - (WPS). The reference for this implementation are from:

    - Silva and Durão (2022). https://arxiv.org/abs/2204.03706

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    distribution = class_weighted_strategy(items)
    total = sum([value for g, value in distribution.items()])
    final_distribution = {g: value / total for g, value in distribution.items()}
    return final_distribution


# Time distribution
def time_weighted_genre(items: dict) -> dict:
    """
    The Time Weighted Genre Distribution - (TWGD). The reference for this implementation are from:

    - <In process>

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    numerator = {}
    denominator = {}

    def compute():
        for index, item in items.items():
            for genre, genre_value in item.genres.items():
                numerator[genre] = numerator.get(genre, 0.) + item.time * item.score * genre_value
                denominator[genre] = denominator.get(genre, 0.) + item.time * item.score

    compute()
    distribution = {g: numerator[g] / denominator[g] for g in numerator}
    return distribution


def time_weighted_probability_genre(items: dict) -> dict:
    """
    The Time Weighted Probability Genre Distribution - (TWPGD). The reference for this implementation are from:

    - <In process>

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    dist = time_weighted_genre(items)
    norm = sum(dist.values())
    distribution = {g: dist[g] / norm for g in dist}
    return distribution


def time_genre(items: dict) -> dict:
    """
    The Time Genre Distribution - (TGD). The reference for this implementation are from:

    - <In process>

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    numerator = {}
    denominator = {}

    def compute():
        for index, item in items.items():
            for genre, genre_value in item.genres.items():
                numerator[genre] = numerator.get(genre, 0.) + item.time * genre_value
                denominator[genre] = denominator.get(genre, 0.) + item.time

    compute()
    distribution = {g: numerator[g] / denominator[g] for g in numerator}
    return distribution


def time_probability_genre(items: dict) -> dict:
    """
    The Time Probability Genre Distribution - (TPGD). The reference for this implementation are from:

    - <In process>

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    dist = time_genre(items)
    norm = sum(dist.values())
    distribution = {g: dist[g] / norm for g in dist}
    return distribution


# Pure values
def pure_genre(items: dict) -> dict:
    """
    The Genre Distribution - (GD). The reference for this implementation are from:

    - <In process>

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    distribution = {}
    for index, item in items.items():
        for genre, genre_value in item.genres.items():
            distribution[genre] = distribution.get(genre, 0.) + genre_value
    return distribution


def probability_genre(items: dict) -> dict:
    """
    The Probability Genre Distribution - (PGD). The reference for this implementation are from:

    - <In process>

    :param items: A Dict of Item Class instances.
    :return: A Dict of genre and value.
    """
    dist = pure_genre(items)
    norm = sum(dist.values())
    distribution = {g: dist[g] / norm for g in dist}
    return distribution