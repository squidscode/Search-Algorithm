# Intelligent Keyword Search
## Purpose
Uses data gathered from **Configurable Web Crawler** to search for keywords and return a result that is most closely correlated to the search query. If you want to change the dataset or change the terminal output, you can change the ```config.json``` file located in the ```src/config``` directory.

To run the program, run the following command in the ```src``` directory: ```python -m search-algorithm```
<br><br>

**Here's an example of the program working:**
```
MacBook-Pro-4:src Siddhant$ python3 -m search_algorithm
Type your search query (separate words by commas or spaces): new york, central perk
  #  TV Shows
---  ----------------------------
  1  Friends
  2  Mad About You
  3  Nobody's Watching
  4  Make Room for Daddy
  5  The Killing
  6  Brooklyn South
  7  To Tell the Truth
  8  Futurama
  9  Tupu
 10  Central Park
 11  Central Park West
 12  Ugly Americans
 13  Tough Crowd with Colin Quinn
 14  Chappelle's Show
 15  When They See Us
 16  Life on Mars
 17  Forever
 18  The City
 19  Tosh.0
 20  Suburgatory
```

**Verbose output for the query above:**
```
MacBook-Pro-4:src Siddhant$ python3 -m search_algorithm
Type your search query (separate words by commas or spaces): new york, central perk
{'york': 0.38769689985092737, 'central': 0.5309173340848249, 'perk': 4.138605412657321}
  #  TV Shows                        Total Weight    Count
---  ----------------------------  --------------  -------
  1  Friends                              9.65659     1150
  2  Mad About You                        4.43313      619
  3  Nobody's Watching                    4.06736      611
  4  Make Room for Daddy                  3.09833      948
  5  The Killing                          2.41472      681
  6  Brooklyn South                       2.41472      999
  7  To Tell the Truth                   -2.26708      908
  8  Futurama                            -2.32662     1047
  9  Tupu                                -2.38765      426
 10  Central Park                        -2.38965     1268
 11  Central Park West                   -2.52837      355
 12  Ugly Americans                      -2.55292      574
 13  Tough Crowd with Colin Quinn        -2.55292      613
 14  Chappelle's Show                    -2.56099      705
 15  When They See Us                    -2.64698      751
 16  Life on Mars                        -2.71809     1626
 17  Forever                             -2.71809      700
 18  The City                            -2.76473     1989
 19  Tosh.0                              -2.76955      661
 20  Suburgatory                         -2.78795      697

```

## The Config File

The ```config.json``` file looks like this:
```
{"keyword_name": "TV Shows",
 "data_file_path": "./data/tvshows.json", 
 "verbose": false, 
 "show_weights": false, 
 "show_word_count": false,
 "number_of_results": 20}
```

```keyword_name``` -- describes the name of the keywords (ie. what the algorithm is **searching for**). The value will show up in the header of the table.

```data_file``` -- the location of the json dataset (you should create these using the **Configurable Web Crawler** program).

```verbose``` -- if true, shows the word-to-weight mapping in the terminal output.

```show_weights``` -- if true, shows the total weight of each of the keywords in the terminal output.

```show_word_count``` -- if true, shows the # of words in the dataset for each of the keywords.

```number_of_results``` -- describes the maximum number of keywords in the table output.
<br><br>

For example, if you wanted to search for video games, your ```config.json``` file will look like this:
```
{"keyword_name": "Video Games",
 "data_file_path": "./data/videogames.json", 
 "verbose": false, 
 "show_weights": false, 
 "show_word_count": false,
 "number_of_results": 20}
```

Here's the program being run with the configurations above:
```
MacBook-Pro-4:src Siddhant$ python3 -m search_algorithm
Type your search query (separate words by commas or spaces): sandbox, 3D, blocks  
  #  Video Games
---  ---------------------
  1  Puzzle League
  2  Boom Blox
  3  Lumines
  4  Pengo
  5  Audiosurf
  6  Mr. Driller
  7  Minecraft
  8  Mercenaries
  9  Disney Infinity
 10  Crackdown
 11  Pushmo
 12  Milon's Secret Castle
 13  Tetris
 14  Bit.Trip
 15  Arkanoid
 16  Sutte Hakkun
 17  Watch Dogs
 18  Total War
 19  Thief
 20  The Sims
```

## How it works

In order to determine the weight of each word, we use the following formula: 
```math
f(n, m) = (n^{0.5}) * (10 / (m + 3)^{0.5})
```

```n``` is the frequency that of the word for a particular keyword in the dataset (eg. if the word "office" occurs 5 times in the tv show, "The Office", then ```n = 5```).

```m``` is number of keywords the word occurs in (eg. if the word "office" is seen in 20 different tv shows, then ```m = 20```).

A negative weight is subtracted from keywords for each word in the search query if the keyword does not contain the word (this allows us to decrease the total weight of keywords that do not contain a *rare/infrequent* word).
<br><br>

These formulas were determined through fine-tuning and testing. We do not want a linear relationship between the freqency of the word and the the weight, because common words can often have high frequencies (and and artificially increase the weight of that word).