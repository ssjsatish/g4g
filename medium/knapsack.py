from operator import itemgetter

def knapsack(W, items):
    my_items = sorted(items, key=itemgetter(1))
    best_values = [0]*(W+1)
    
    for w in range(1,W+1):
        best_item = None
        best_new_value = best_values[w]
        for i, (value, weight) in enumerate(my_items):
            if weight<=w:
                value_sum = value + best_values[w-weight]
                if value_sum>best_new_value:
                    best_item = i
                    best_new_value = value_sum
            else:
                break

        if best_item is not None:
            bi_weight = my_items[best_item][1]
            bi_value = my_items[best_item][0]

            for w2 in reversed(range(w,W+1)):
                new_value = best_values[w2-bi_weight] + bi_value 
                best_values[w2] = max(best_values[w2], new_value)
                    
            del my_items[best_item]
    
    return best_values[W]

for _ in range(int(input())):
    n = int(input())
    W = int(input())
    values = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    items = list(zip(values, weights))
  
    print(knapsack(W,items))
    