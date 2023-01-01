# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# author : Gokul656

def main():
    arr = list(input().split(" "))
    times = 4

    for i in range(times):
        arr.append(arr.pop(0))

    return arr


if __name__ == "__main__":
    main()
