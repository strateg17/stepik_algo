import sys

def fractional_knapsack(capacity, values_and_weights):
  order = [(v / w, w) for v, w in values_and_weights]
  order.sort(reverse=True)
  
  acc = 0
  
  for v_per_w, w in order:
    if w <= capacity:
      acc += v_per_w * w
      capacity -= w
    else:
      acc += v_per_w * capacity
      break
      
  return acc


def main():
  reader = (tuple(map(int, line.split())) for line in sys.stdin)
  n, capacity = next(reader)
  values_and_weights = list(reader)
  assert len(values_and_weights) == n
  opt_value = fractional_knapsack(capacity, values_and_weights)
  print(f"{opt_value: .3f}")
  
  
def test():
  assert fractional_knapsack(0, [(60, 20)]) == 0.0
  assert fractional_knapsack(25, [(60, 20)]) == 60.0
  assert fractional_knapsack(25, [(60, 20), (0, 100)]) == 60.0
  assert fractional_knapsack(25, [(60, 20), (50, 50)]) == 60.0 + 5.0
  assert fractional_knapsack(50, [(60, 20), (100, 50), (120, 30)]) == 180
  
  from random import randint
  from timing import timed
  for attempt in range(100):
    n = randint(1, 1000)
    capacity = randint(0, 2 * 10**6)
    values_and_weights = []
    for i in range(n):
      values_and_weights.append((randint(0, 2 * 10**6), randint(1, 2 * 10**6)))
      t = timed(fractional_knapsack, capacity, values_and_weights)
      assert t < 5
      
      
if __name__ = __main__:
  test()
  main()
      
    
  
  
