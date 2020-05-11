def _make_multiplier_of(i, x):
    def _multiplier(n):
        return x * n

    a = _multiplier(i)
    return a


def _main():
    a = _make_multiplier_of(2, 3)
    return a


if __name__ == '__main__':
    print(_main())
