import argparse
import random
import sys


def random_string():
    """
    generate a randome word key
    """
    word_length = random.randint(1, 15)
    word = ""
    for _ in range(word_length):
        word += chr(random.randint(97, 122))

    return(word)


def random_int():
    return random.randint(-10000, 10000)


def random_float():
    return 10000 * (random.random() - 0.5)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key_type",
                        help="type of key/values pairs to generate",
                        choices=["int", "float", "string"],
                        required=True
                        )
    parser.add_argument("--value_type",
                        help="type of key/values pairs to generate",
                        choices=["int", "float", "string"],
                        )
    parser.add_argument("-N,", "--number",
                        help="number key/value pairs to generate",
                        default="10000",
                        )
    parser.add_argument("--sorted",
                        help="sort generate key/value pairs",
                        default="False",
                        choices=["True", "False"]
                        )
    parser.add_argument("--outfile",
                        help="name of file to write to",
                        required=True
                        )

    args = parser.parse_args()
    if args.value_type is None:
        args.value_type = args.key_type
    selection = {"key": eval("random_"+args.key_type),
                 "value": eval("random_"+args.value_type)}
    try:
        with open(args.outfile, 'w') as fh:
            kv_pairs = []
            for _ in range(int(args.number)):
                kv_pairs.append([selection["key"](), selection["value"]()])
            if eval(args.sorted):
                kv_pairs.sort(key = lambda x: x[0])
            lines = [str(kv[0])+" "+str(kv[1])+"\n" for kv in kv_pairs]
            fh.writelines(lines)
    except PermissionError:
        print("gen_data: cannot write over", args.outfile, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
