import sys
import re
import json
import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

config = {}

if __name__ == "__main__":
    with open("./config/config.json", "r") as read_file:
        config = json.load(read_file)

    word_dictionary = {}
    with open(config["data_file_path"], "r") as read_file:
        word_dictionary = json.load(read_file)

    search = input("Type your search query (separate words by commas or spaces): ")
    series_weight_dictionary = {}
    word_means = {}
    # Adding weights
    for word in search.split(" "):
        word = re.sub(r"[,.!?(\[.*?\])(\n)(\")]", "", word.lower())
        if word not in word_dictionary["word_map"]: continue
        # meaning = dictionary.meaning(word)
        # if "Adverb" in meaning or "Adjective" in meaning or "Verb" in meaning:
        #     continue
        mean = 0
        size = len(word_dictionary["word_map"][word])
        for series in word_dictionary["word_map"][word]:
            # f(n) = (n^{0.5}) * (10 / (m + 3)^{0.5})
            weight = float(word_dictionary["word_map"][word][series]**0.5) * (10 / math.pow(size + 3, 0.5))
            mean += weight / size
            if series in series_weight_dictionary:
                series_weight_dictionary[series] = series_weight_dictionary[series] + weight
            else:
                series_weight_dictionary[series] = weight
        word_means[word] = mean
    # Creating and adding negative weights
    for word in word_means:
        for series in series_weight_dictionary:
            if series not in word_dictionary["word_map"][word]:
                weight = -word_means[word]
                series_weight_dictionary[series] = series_weight_dictionary[series] + weight

    if config["verbose"]: print(word_means)
    list_of_series = sorted(series_weight_dictionary.items(), key=lambda kv: (kv[1], kv[0]))
    list_of_series.reverse()
    
    data_x = []
    data_y = []
    headers_arr = ["#", config["keyword_name"]]
    if config["show_weights"]: headers_arr.append("Total Weight")
    if config["show_word_count"]: headers_arr.append("Count")

    arr = []
    for i in range(1, min(config["number_of_results"] + 1, len(list_of_series)), 1):
        arr.append([i, list_of_series[i - 1][0]])
        if config["show_weights"]: arr[i - 1].append(list_of_series[i - 1][1])
        if config["show_word_count"]: arr[i - 1].append(word_dictionary['series_count'][list_of_series[i - 1][0]])

    print(tabulate(arr, headers=headers_arr))