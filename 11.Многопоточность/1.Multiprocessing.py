import multiprocessing


def input_to_list(text: str):
    lists = text[1:].replace("[", "").replace("]]", "").split("], ")
    return [list(map(int, lst.split())) for lst in lists]


def main():
    array_2d = input_to_list(input())
    with multiprocessing.Pool() as p:
        result = p.map(worker_function, array_2d)
    print(sum(result))


if __name__ == "__main__":
    main()
