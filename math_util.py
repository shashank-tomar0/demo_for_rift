def add(a, b):
    return a + b

ad = add

__all__ = ['add', 'ad']

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from test import test_add
    test_add()
