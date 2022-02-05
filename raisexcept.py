# handling error


# raise error

try:
    a = 18
    b = 0

    c = a / b
    print('result:', str(c))

except Exception as e:
    raise

finally:
    print('Done')