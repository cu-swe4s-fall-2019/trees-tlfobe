import binary_tree
import sys
import argparse
sys.path.insert(1, "hash-tables-tlfobe")  # noqa: E402
sys.path.insert(1, "avl_tree")  # noqa: E402
import hash_tables
import avl


def get_key_value_pairs_from_file(file):
    keys = []
    values = []
    with open(file, "r") as fh:
        for line in fh:
            values = line.rstrip().split(' ')
            keys.append(values[0])
            values.append(values[1])

    return(keys, values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_struct",
                        help="type of data structure to use for storing data",
                        choices=["hash", "AVL", "tree"],
                        required=True
                        )
    parser.add_argument("--data_file",
                        help="data file to pull keys/value pairs from",
                        required=True,
                        )
    parser.add_argument("--n_values",
                        help="number of hash values to pull" +
                        " from the data file",
                        default="10000",
                        )

    args = parser.parse_args()

    str_to_data_strct_map = {"hash": hash_tables.ChainedHash,
                             "AVL": avl.AVL, "tree": binary_tree.BinaryTree}

    data_struct = str_to_data_strct_map[args.data_struct]

    # Load in Data

    key, values = get_key_value_pairs_from_file(args.data_file)

    # Time it takes to insert

    # Time it takes to search subset of data

    # Time it takes to search for not in database


if __name__ == "__main__":
    main()
