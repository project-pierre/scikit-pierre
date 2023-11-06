from copy import deepcopy

from pandas import DataFrame

from ..models.item import ItemsInMemory


class BaseTradeOff:
    """
    Tradeoff superclass. To be used for all Tradeoff classes.
    """
    def __init__(self, users_preferences: DataFrame, candidate_items: DataFrame, item_set: DataFrame):
        """
        :param users_preferences: A Pandas Dataframe with three columns [USER_ID, ITEM_ID, TRANSACTION_VALUE]
        :param candidate_items: A Pandas Dataframe with three columns [USER_ID, ITEM_ID, PREDICTED_VALUE]
        :param item_set: A Pandas Dataframe with at least two columns [ITEM_ID, CLASSES]
        """
        # Verifying if all columns are present in the user model and the candidate items.
        if {'USER_ID', 'ITEM_ID', 'TRANSACTION_VALUE'}.issubset(set(users_preferences.columns)) or \
                {'USER_ID', 'ITEM_ID', 'TRANSACTION_VALUE'}.issubset(set(candidate_items.columns)):
            self.users_preferences = deepcopy(users_preferences)
            self.candidate_items = deepcopy(candidate_items)
        else:
            raise Exception("Some column is missing.")

        if set(users_preferences['ITEM_ID'].unique().tolist() +
               candidate_items['ITEM_ID'].unique().tolist()).issubset(set(item_set['ITEM_ID'].unique().tolist())):
            self.item_set = deepcopy(item_set)
        else:
            raise Exception("Some wrong information in the ITEM ID.")

        self._item_in_memory = ItemsInMemory(data=self.item_set)

        self.environment = {}

    def env(self, environment: dict):
        self.environment = environment

    def fit(self):
        if not self.environment:
            raise Exception("The configuration need to be set!")