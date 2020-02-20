#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if n == 0:
      return 1
    elif n<0:
      return 0
    elif cache and cache[n] > 0:
      return cache[n]
    else:
      if cache is None:
        cache = {}
        # print(cache)
      value = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
      cache[n] = value
      return value
    
print(eating_cookies(900, {})/1000000000000)


# else:
#       if cache is None:
#         cache = { i:0 for i in range(n+1)}
#         print(cache)
#       value = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
#       cache[n] = value
#       return value
    
#1 (1,1,1,1,1) 
#2 (1,1,1,2)
#3 (1,1,2,1)
#4 (1,2,1,1)
#5 (1,2,2)
#6 (1,1,3)
#7 (1,3,1)
#
#8 (2,1,1,1)
#9 (2,1,2)
#10 (2,2,1)
#11 (2,3)
# 
#12 (3,1,1)
#13 (3,2)
# 
# 
# 
# 
#  
  
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')