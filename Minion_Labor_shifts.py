def solution(data, n):
  iMap = {};
  for idx, val in enumerate(data):
    if val in iMap:
      iMap[val].append(idx)
    else:
      iMap[val] = [idx]
  ret = []
  for val in data:
    indices = iMap[val]
    if len(indices)<=n:
      ret.append(val)

  return ret