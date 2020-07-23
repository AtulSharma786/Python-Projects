import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="please tell me")

    parser.add_argument('--y', type=float, default=3.0, help="please tell me")

    parser.add_argument('--0', type=str, default="add", help="please tell me")

    args = parser.parse_args()
    sys.std
