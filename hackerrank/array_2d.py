# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# author : Gokul656

def calc_sum(arr, i, j):
    print(arr[i][j:j+3], [arr[i+1][j+1]], arr[i+2][j:j+3])
    return sum(arr[i][j:j+3] + [arr[i+1][j+1]] + arr[i+2][j:j+3])


def main():
    """
    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    """

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_val = float('-inf')
    times = len(arr) // 2 + 1
    for i in range(times):
        for j in range(times):
            max_val = max(max_val, calc_sum(arr, i, j))
    print(max_val)


if __name__ == "__main__":
    main()
