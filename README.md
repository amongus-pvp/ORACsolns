# ORACsolns
ORAC solns in python
This is the site with all the problems:
https://orac2.info/hub/

Im going to organise this into the sets and then start uploading my solutions

This is being done in 2025 so all solutions read and write to console now (except for specific problems from selection exam sets but those will be dealt with later)

I'm uploading a lot of these as I solve them, and I am quite hesitant to upload problems unless the set they originate from has already been solved

✅ for completed
❌ for uncompleted

# Formatting
Almost every file will be a python file that scores 100/100 (or partial if specified) when submitted to the link given at the top of the code. <br>
My code is formatted in the following style for problems (in python) that use standard input and output:

```py
# hyperlink to problem if user wants to read, this will be a comment
import foo # make any neccesary imports, usually bisect, deque, sys
N = int(input()) # for singular integer inputs
A, B, C = map(int, input().split()) # for a constant number of spaced integers being given on a line of input
vals = list(map(int, input().split())) # for a dynamic number of spaced integers being given on a single line of input
x = []
for i in range(N):
    x.append(int(input())) # for dynamic number of integers that contribute to one array, inputted over N lines
st = input() # for taking in strings
stl = list(input()) # for a list of chars
# that is all for input


# here we calculate answer, this changes for every file
answer = 0

# ill change this variable according to my algorithm
print(answer) # finally outputting the answer
```

For older problems we may need to read from files, this is dealt with as follows:
```py
# this stuff goes before we take any input
import sys 
sys.stdin = open("filein.txt", "r")
sys.stdout = open("fileout.txt", "w")

# use input() and print() as normal now, they simply get redirected to the files instead of the console
```

Finally, since python isn't very good with recursion and there is a recursion limit of 999, for any recursive solutions I may include:
```py
import sys
sys.setrecursionlimit(10**7) # 10**9 maybe if the problem conditions are massive
```

**Rarely** ever will you see me using:
```py
def main():
    # code
    print("Here is the awesome answer")
if __name__ == "__main__":
    main()
```

# Solutions
I will be authoring my own written solutions for certain COMPLETED problemsets, these will be uploaded as pdfs, mostly as practise for my explanation skills. These will be kept under the /Editorials directory

# Completed Problems
Heres a table of every problem I have **uploaded**. These are numbered based on the hyperlink they have on ORAC, which comes in the form https://orac2.info/problem/X/ where `X` is the problem number. I'll also include the score I achieved on that problem incase I upload a partial solution.

Currently I have uploaded: `123` solutions,
`3` of these are partial solutions

| Problem #  | Problem Name | Score /100 |
| ------------- | ------------- | ------------- |
| 3  | Vases  | 100 |
| 6 | Superphone | 100 |
| 10 | Travelling Salesperson | 100 |
| 13 | Cookies | 100 |
| 21 | Chocolate Shop | 100 |
| 23 | Snap Dragons II | 100 |
| 27 | Ruckus League | 100 |
| 33 | Air Drop | 100 |
| 34 | Wetlands | 100 |
| 39 | Nomnomnom | 100 |
| 50 | Medusa's Snakes | 100 |
| 56 | Treasure Hunt | 100 |
| 57 | Oil | 100 |
| 62 | No (One) Left | 100 |
| 70 | Safe Cracking | 100 |
| 72 | Chimera | 100 |
| 74 | Ants | 100 |
| 88 | Taxis | 100 |
| 90 | Mouse Hunt | 100 |
| 98 | Chimpanzee | 100 |
| 99 | Curry | 100 |
| 103 | Night Walk | 100 |
| 104 | Mansion | 100 |
| 106 | Evading Capture | 100 |
| 107 | Choreography | 100 |
| 112 | RPS | 100 |
| 121 | Fashion Statement | 100 |
| 122 | Snake Charmer | 100 |
| 139 | Sculpture II | 100 |
| 141 | Magic Squares | 100 |
| 147 | Lollipops, Sweets and Chocolates II | 100 |
| 149 | Atlantis Rising | 100 |
| 158 | Frog | 100 |
| 165 | Hiring Monks | 100 |
| 167 | Conveyor Belts | 100 |
| 169 | Bookshop | 100 |
| 172 | Artclass | 100 |
| 175 | Cute Numbers | 100 |
| 176 | Lab Session | 100 |
| 179 | Powers Of Two | 100 |
| 199 | Corey's Party | 100 |
| 203 | Pygmy Hippos | 100 |
| 204 | Missing Mango | 100 |
| 209 | Baubles | 100 |
| 210 | Ladybugs II | 100 |
| 211 | Ghost Encounters | 100 |
| 212 | Ninjas | 100 |
| 216 | Tennis Robot | 100 |
| 220 | Archery | 100 |
| 221 | Atlantis: The Beginning | 100 |
| 225 | Tag | 100 |
| 226 | Heatwave | 100 | 
| 240 | Farmer Drama | 100 |
| 244 | Wet Chairs | 100 |
| 246 | Tickets | 100 |
| 247 | Snap Dragons | 100 |
| 250 | Cabinet Shuffle | 100 |
| 257 | Invasion | 100 |
| 260 | Chocolate II (C++) | 100 |
| 261 | Settling Debts | 100 |
| 262 | Pirates | 100 |
| 265 | Street Construction | 100 |
| 267 | Landmark | 100 |
| 268 | Aliens | 100 |
| 272 | Restaurants | 100 |
| 274 | Snap Dragons III: Binary Snap | 100 |
| 283 | Posters | 100 |
| 288 | Crowd Surfing | 100 |
| 294 | Sculpture | 100 |
| 295 | Save-It | 100 |
| 300 | Sleight of Hand | 100 |
| 301 | Carmen Sanfrancisco | 100 |
| 303 | NORT | 100 |
| 304 | Spies V: Voices in the Dark | 100 |
| 308 | Chimera II | 100 |
| 309 | Ladybugs | 100 |
| 319 | Russian Dolls | 100 |
| 321 | Castle Cavalry | 100 |
| 324 | Counting to Infinity | 100 |
| 325 | Encyclopedia | 100 |
| 328 | A Dish Best Served Cold | 100 |
| 329 | Mixed Fraction | 100 |
| 330 | Sitting or Standing? | 100 |
| 331 | The Tremendous Tak-Tak Tree | 100 |
| 332 | Addition | 100 |
| 333 | Friendlist | 100 |
| 334 | Triple Hunting | 100 |
| 336 | A Mindbending Scenario | 100 |
| 338 | Dictionary | 100 |
| 340 | Drought | 100 |
| 378 | Giant Hippos | 100 |
| 800 | Genius | 100 |
| 982 | Culture | 100 |
| 1097 | Melody | 100 |
| 1098 | Robot Vacuum | 100 |
| 1099 | Art Class II | 100 |
| 1100 | Laser Cutter | 100 |
| 1101 | Space Mission | 100 |
| 1102 | Social Distancing | 100 |
| 1193 | Election II | 100 |
| 1194 | Beautiful Buildings | 100 |
| 1195 | Level Ground | 100 |
| 1196 | TSP | 100 |
| 1197 | Composing Pyramids | 100 |
| 1198 | Spaceship Shuffle | 100 |
| 1215 | Sewers | 100 |
| 1216 | Ecofriendly Trip (C++) | 100 | 
| 1222 | Chocolate Bar | 100 |
| 1297 | Making Bank | 100 |
| 1298 | Wheeling And Dealing | 100 |
| 1299 | TeleTrip | 100 |
| 1300 | Yet Another Lights Problem | 100 |
| 1301 | Shoptimality | 100 |
| 1302 | Distincto's Raffle | 100 |
| 1415 | Palindrome | 100 |
| 1461 | Backpacking | 100 |
| 1462 | Atlantis III: Twin Rivers | 50 |
| 1463 | Javelin | 100 |
| 1464 | Subbookkeeper | 100 |
| 1465 | Shopping Spree | 100 |
| 1466 | Tennis Robot II | 100 |
| 1537 | Tree Dash (C++) | 35 |
| 1538 | Arrayser (C++) | 53.44 |


# TODO

Add links to problems in every file ✅ <br>
Write editorials for one set at the minimum (2023 most likely) ❌<br>
Finish all AIO problems and upload them (I have roughly 17 left to solve) ❌<br>
