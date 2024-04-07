def find_cost(coefficients: list[float], data: list[list[int]]):
    error_sum = 0
    for item in data:
        diff = item[0] * coefficients[0] + item[1] * coefficients[1] + item[2] * coefficients[2] + coefficients[3]
        error = item[-1] - diff
        error_sum += error
    return error_sum


def train(data: list[list[int]], lr: float, epochs: int) -> list[float]:
    coefficients: list[float] = [0.0, 0.0, 0.0, 0.0]
    for _ in range(epochs):
        for index, point in enumerate(coefficients):
            cost = find_cost(coefficients, data)
            new_coefficient = coefficients
            new_coefficient[index] += H
            cost_h = find_cost(new_coefficient, data)
            slope = (cost_h - cost) / H
            coefficients[index] -= slope * LR
        print(find_cost(coefficients, data))

    return coefficients


def main() -> None:
    trained_coefficients = train(DATASET, LR, EPOCHS)
    print(trained_coefficients)
    input_data = []
    for input_num in range(3):
        input_val = -float("inf")
        match input_num:
            case 0:
                input_val = float(input("Input Study Hours: "))
            case 1:
                input_val = float(input("\rInput Sleep Hours: "))
            case 2:
                input_val = float(input("\rInput ECA Hours: "))
        input_data.append(input_val)

    print(input_data[0] * trained_coefficients[0] + input_data[1] * trained_coefficients[1] + input_data[2] *
      trained_coefficients[2] + trained_coefficients[3])

if __name__ == '__main__':
    # Initialize Constants
    DATASET = [
        [5, 7, 2, 80],
        [3, 6, 1, 75],
        [6, 8, 3, 85],
        [4, 7, 2, 78],
        [7, 9, 4, 90]
    ]

    LR = 0.001
    EPOCHS = 10000
    H = 0.00001
    main()
