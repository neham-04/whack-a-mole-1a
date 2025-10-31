from algo import coin_change


def test_coin_change_example():
    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins, amount) == 3
 
def test_coin_change_no_solution():
    coins = [2]
    amount = 3
    assert coin_change(coins, amount) == -1

def test_coin_change_exact_solution():
    coins = [1, 3, 4]
    amount = 6
    assert coin_change(coins, amount) == 2