import argparse
import random
import math

def get_parsed_args():
    parser = argparse.ArgumentParser(
                    prog='Infinite Math',
                    description='Endless practice for mental math nerds.',
                    epilog='Good luck!')
    parser.add_argument("--addition", nargs=2, type=int, action='store')
    parser.add_argument("--subtraction", nargs=2, type=int, action='store')
    parser.add_argument("--multi", nargs=2, type=int, action='store')
    parser.add_argument("--divide", nargs=2, type=int, action='store')
    return parser.parse_args()

def ndigits_to_max_int(digits):
    return int(math.pow(10, digits) - 1)

def ndigits_to_random_int(digits):
    return random.randint(1, ndigits_to_max_int(digits))

def ndigits_to_random_tuple(digit_sequence):
    return tuple([ndigits_to_random_int(d) for d in digit_sequence])

def operators_from_args(args):
    d = dict()
    if hasattr(args, "addition"): 
        d["addition"] = args.addition
    if hasattr(args, "subtraction"): 
        d["subtraction"] = args.subtraction
    if hasattr(args, "multi"): 
        d["multi"] = args.multi
    if hasattr(args, "divide"): 
        d["divide"] = args.divide
    return d

def generate_question(addition=None, subtraction=None, multi=None, divide=None):
    candidates = []
    if addition is not None:
        question = ndigits_to_random_tuple(addition)
        answer = question[0] + question[1]
        question_str = "{} + {}".format(question[0], question[1])
        candidates.append((question_str, answer))
    if subtraction is not None:
        question = ndigits_to_random_tuple(subtraction)
        answer = question[0] - question[1]
        question_str = "{} - {}".format(question[0], question[1])
        candidates.append((question_str, answer))
    if multi is not None:
        question = ndigits_to_random_tuple(multi)
        answer = question[0] * question[1]
        question_str = "{} * {}".format(question[0], question[1])
        candidates.append((question_str, answer))
    if divide is not None:
        question = ndigits_to_random_tuple(divide)
        answer = question[0] // question[1]
        question_str = "{} / {}".format(question[0], question[1])
        candidates.append((question_str, answer))
    return random.choice(candidates)


def main():
    random.seed() 
    args = get_parsed_args()
    print("Infinite Math Practice")
    print("Ctrl + C to exit")
    operators = operators_from_args(args) 
    while True:
        question_str, answer = generate_question(**operators)
        ans = input(question_str + ": ")
        if ans != str(answer):
            print("incorrect. answer: {}".format(answer))

if __name__ == "__main__":
    main()
