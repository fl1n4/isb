import json
import logging
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


def number_search(save_path: str, hash: str, last_digits: str, bins: list) -> str:
    """
    Search for credit card numbers using hash, and save them to a file.
    The function uses multiple processes to reduce the search time.
    args:
        save_path: the path to save the card's number
        hash: input hash of number
        last_digits: last 4 digits of card's number
        bins: bins
    return:
        number of card if it matches with hash
    """
    card_numbers = None
    with mp.Pool(mp.cpu_count()) as p:
        for result in p.starmap(check_number_card, [(i, hash, last_digits, bins) for i in range(0, 1000000)]):
            if result is not None:
                card_numbers = result
                break
    try:
        with open(save_path, mode='w', encoding="utf-8") as file:
            json.dump({"card_number": card_numbers}, file)
    except Exception as ex:
        logging.error(ex)
    return card_numbers


def luna_algorithm(card_number: str) -> bool:
    """
    Checking the credit card number using the Luhn algorithm
    args:
        card_number: number of card
    return:
        result of the check
    """
    try:
        card_number_list = [int(char) for char in card_number]
        for i in range(len(card_number_list) - 2, -1, -2):
            card_number_list[i] *= 2
            if card_number_list[i] > 9:
                card_number_list[i] -= 9
        return sum(card_number_list) % 10 == 0
    except Exception as ex:
        logging.error(ex)
        return False