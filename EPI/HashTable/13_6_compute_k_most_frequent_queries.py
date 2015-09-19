import os
import math
import sys
from collections import defaultdict, Counter
from heapq import *

"""
    You are given a log file containing search queries. Each query is a string,
    and queries are separated by newlines. Diverse applications, such as auto-
    completion and trend analysis, require computing the most frequent queries.
    In the abstract, you are to solve the following problem.

    Given an array of strings, compute the k strings that appear most frequently
    in the array.
"""
def compute_k_most_frequence_strings(arr, k):
    """
        Brute-force algorithm
    """
    if len(arr) < k:
        return arr

    c = Counter(arr)
    return c.most_common(k)

def compute_k_most_frequence_strings_2(arr, k):
    """
        Use heap
    """
    if len(arr) < k:
        return arr

    d = defaultdict(int)

    idx = 0
    while len(d) < k and idx < len(arr):
        d[arr[idx]] += 1
        idx += 1

    h = [None] * k
    j = 0
    for k, v in d.iteritems():
        h[j] = (v, k)
        j += 1

    heapify(h)
    appeared_key = {}
    for v in h:
        appeared_key[v[1]] = 1
    for i in range(idx, len(arr)):
        d[arr[i]] += 1
        # update the smallest in the heap before poping it
        if h[0][1] == arr[i]:
            h[0] = (d[arr[i]], arr[i])
            heapify(h)
        if d[arr[i]] > h[0][0] and not arr[i] in appeared_key:
            appeared_key.pop(heappop(h)[1])
            heappush(h, (d[arr[i]], arr[i]))
            appeared_key[arr[i]] = 1
    res = []
    for v in h:
        res.append((v[1], d[v[1]]))
    return res[::-1]


s = """
Like shrimp and tuna, salmon is very popular with Americans. Diners love it even as sushi. But in sushi's birthplace, Japan, raw salmon wasn't always on the menu. Jess Jiang of our Planet Money podcast has the story of salmon sushi's rocky start.
JESS JIANG, BYLINE: Shimao Ishikawa has been a sushi chef for over 40 years. He works at a sushi restaurant in Manhattan called Jewel Bako. Ishikawa's served and eaten all the hard-core things, like sea urchin, poisonous blowfish. But in all his years as a sushi chef, he's never taken a single bite of one of his best sellers, raw salmon.
SHIMAO ISHIKAWA: I will not eat salmon, no.
JIANG: Wait, never?
ISHIKAWA: Yeah, I never eat salmon, you know.
JIANG: Can we get you to try it today?
ISHIKAWA: (Laughter) Tomorrow, manana.
JIANG: Ishikawa's aversion is not unusual among the Japanese because for much of sushi's history, salmon was a fish you did not eat raw. Then 30 years ago, a group launched a plan to change that, a group halfway around the world.
BJORN EIRIK OLSEN: Hello, Bjorn Eirik here.
JIANG: Bjorn Eirik Olsen's from Norway. He says in the '80s, the country had a problem; they had too much salmon. The government hired Bjorn to sell it to the country that's famous for eating fish. Bjorn figured, easy. He went to Tokyo, got a bunch of Japanese fish industry executives together, and he unveiled the next big thing, salmon sushi.
OLSEN: And they say, it's impossible. We Japanese do not eat salmon roll. They say, it doesn't taste good. They say the color is wrong also; it should be redder. It has a smell. And they say that the head has the wrong shape.
JIANG: Basically, people in Japan thought it was gross. Bjorn's big challenge was this. He needed to change the perception of an entire country, change that visceral reaction. The salmon people in Japan were used to eating had parasites, so they always cooked it. Bjorn says Norwegian salmon's different. Parasites aren't a problem. But he couldn't run an ad that said, don't worry; our salmon is parasite free.
OLSEN: We didn't want to mention it at all because if you say that my fish has no poison and you say it's no parasite; it's no bad things in it.
JIANG: Yeah, the first thing they'll think of is - is there - there's poison?
OLSEN: Yeah, yeah, yeah.
JIANG: Instead, Bjorn made ads that focused on the pure, fresh Norwegian waters. That did not work. And back in Norway, the salmon industry was getting desperate. The glut of salmon had gotten so bad, they started filling industrial freezers with tons and tons of salmon. Bjorn says there was a lot of pressure for him to give up the dream of salmon sushi. But he wouldn't. He thought all he needed was one big sale. He went to a company called Nishi Rei. He'd been talking to them for a few years. Everybody in Japan knows them. They sell frozen food - dumplings, chicken nuggets, squid. Bjorn told them, I will sell you 5,000 tons of salmon for cheap. All you have to do is sell it in the grocery stores as sushi; just try it. Nishi Rei said yes. Bjorn had his deal.
OLSEN: It was a day of happiness. I remember that, and there was a feeling of making history.
JIANG: Once Nishi Rei started selling salmon for sushi, it somehow seemed more normal. Tadashi Ono grew up in Tokyo. He says he remembers trying salmon sushi in the early days.
JIANG: Salmon sushi started showing up all over Japan, especially at the cheap sushi restaurants, the ones with the conveyor belts. Bjorn realized salmon sushi had become a thing when a few years later, he was walking around Tokyo and he noticed the little plastic sushi replicas in the restaurant windows.
OLSEN: And then suddenly, I saw there was salmon now, plastic copies in the sushi shops. I could see it around in Tokyo. And then I thought, this is really a breakthrough.
JIANG: Japan helped out Norway's fish problem, but Bjorn says Norway actually helped out Japan, too. Salmon is one of the reasons sushi got big around the world. It's mild. It's fatty. Kids like it. It's a gateway fish. Jess Jiang, NPR News.
"""
s = s.replace(',', '')
s = s.replace('.', '')
print compute_k_most_frequence_strings(s.split(), 3)
print compute_k_most_frequence_strings_2(s.split(), 3)
