import os
import json
import logging
import argparse
import hashlib
import multiprocessing as mp
import time

from tqdm import tqdm
from matplotlib import pyplot as plt


logging.basicConfig(level=logging.INFO)


def check_number_card(tested_part: int, hash: str, last_digits: str, bins: list) -> str | None:
    """
    Checks the card number with the specified number to match the hash.
    args:
        tested_part: generated part for testing
        hash: input hash of number
        last_digits: last 4 digits of card's number
        bins: bins
    return:
        number of card if it matches with hash OR None if not
    """
    for bin in bins:
        card_number = f'{bin}{tested_part:06d}{last_digits}'
        if hashlib.sha256(card_number.encode()).hexdigest() == hash:
            logging.info(f"Match found: {card_number}")
            return card_number
    return None