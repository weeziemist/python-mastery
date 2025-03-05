
def portfolio_cost(filename):
    result = 0

    with open(filename, 'r') as f:
        for line in f:
            row = line.split()

            try:
                num_shares = int(row[1])
                price = float(row[2])
                result += price * num_shares
            except ValueError as e:
                print(f"Couldn't parse: {line!r}")
                print(f"Reason: {e}")
    
    return result

if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio.dat'))
