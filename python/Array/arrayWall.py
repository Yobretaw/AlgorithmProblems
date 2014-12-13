def calcVolume(land, len):
  leftMax = 0
  rightMax = 0

  left = 0
  right = len - 1
  volume = 0

  while left < right:
    if land[left] > leftMax:
      leftMax = land[left]
    if land[right] > rightMax:
      rightMax = land[right]

    if leftMax >= rightMax:
      volume += rightMax - land[right]
      right -= 1
    else:
      volume += leftMax - land[left]
      left += 1

  return volume

def main():
  land = [2, 5, 1, 2, 3, 4, 7, 7, 6]
  print calcVolume(land, len(land))

main()
