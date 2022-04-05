import math
def main():
    distance = float(input())
    speed = float(input())
    time_after_2km = (distance-2)/speed
    if distance <= 2:
        print(12000)
    else:
        print(round(12000 + 3500*math.ceil(distance-2) + 350*time_after_2km))

if __name__ == '__main__':
    main()
