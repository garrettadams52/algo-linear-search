from linear_search import linear_search
from linear_search import  global_linear_search

#print(linear_search(3, [1,2,3]) == 2)
#print(linear_search(4, [1,2,3]) == None)
#print(linear_search(13, [1,2,3]) == None)

#print(linear_search(3, [1,2,3]))
#print(linear_search(4, [1,2,3]))
#print(linear_search(13, [1,2,13]))

bananas_list = list('bananas')
# => ["b", "a", "n", "a", "n", "a", "s"]
print(global_linear_search("q", bananas_list))
# => [ 1, 3, 5 ]
