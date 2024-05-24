def read_input_sequences(input_file):
    input_sequences = []
    with open(input_file, 'r') as file:
        for line in file:
            input_sequences.append(line.strip())
    return input_sequences


def read_expected_outputs(expected_output_file):
    expected_outputs = []
    with open(expected_output_file, 'r') as file:
        for line in file:
            expected_outputs.append(line.strip())
    return expected_outputs


def sort_sequence(sequence):
    numbers = [int(x) for x in sequence.split()[1:]]
    request = sequence[0]

    if request == 'A':
        numbers.sort()
    elif request == 'D':
        numbers.sort(reverse=True)

    return ' '.join(str(number) for number in numbers)


def main():
    input_file = "input.txt"
    expected_output_file = "expected_output.txt"
    test_log_file = "test_log.txt"
    input_sequences = read_input_sequences(input_file)
    expected_outputs = read_expected_outputs(expected_output_file)

    with open(test_log_file, 'w') as file:
        for i, expected_output in enumerate(expected_outputs):
            if i >= len(input_sequences):
                break

            input_sequence = input_sequences[i]
            observed_output = sort_sequence(input_sequence)
            verdict = "PASS" if expected_output == observed_output else "FAIL"

            file.write(
                f"Test case {i + 1}: Expected output: {expected_output}, Observed output: {observed_output}, Verdict: {verdict}\n")


if __name__ == '__main__':
    main()
