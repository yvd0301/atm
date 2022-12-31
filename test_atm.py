import pytest
import atm


def test_should_not_access_pin_number():
    card = atm.Card()
    with pytest.raises(AttributeError):
        card.__pin_number


def test_correct_card_check_pin_number():
    card = atm.Card()
    assert card.check_pin(1234) == True


def test_wrong_card_check_pin_number():
    card = atm.Card()
    assert card.check_pin(1235) == False


def test_should_get_account_number_by_card():
    # Given
    account = atm.Account()
    account.set_account(1)
    card = atm.Card()
    card.connect_account(account)

    # When
    accounts = card.get_account_numbers()

    # Then
    assert accounts[0] == 1


def test_should_get_account_number_by_atm():
    # Given
    a = atm.Atm()
    card = atm.Card()
    a.insert_card(card)

    # When
    accounts = a.get_account_number(1234)

    # Then
    assert accounts[0] == 1


def test_should_select_account_using_card():
    # Given
    a = atm.Atm()
    card = atm.Card()
    a.insert_card(card)

    # When
    account = a.select_account(1)

    # Then
    assert account == 1


def test_connect_valid_account():
    account = atm.Account()
    card = atm.Card()
    card.connect_account(account)


def test_connect_invalid_account():
    account = atm.Atm()
    card = atm.Card()
    with pytest.raises(Exception):
        card.connect_account(account)


def test_open_account_with_no_balance():
    account = atm.Account()
    assert account.get_balance() == 0


def test_insert_valid_card():
    card = atm.Card()
    a = atm.Atm()
    a.insert_card(card)


def test_insert_invalid_card():
    account = atm.Account()
    a = atm.Atm()
    with pytest.raises(Exception):
        a.insert_card(account)


def test_intput_correct_pin():
    card = atm.Card()
    a = atm.Atm()
    a.insert_card(card)

    assert a.input_pin(1234) == True


def test_see_balance():

    card = atm.Card()
    a = atm.Atm()
    a.insert_card(card)

    assert a.see_balance(1234, 1) == 0


def test_can_deposit_by_atm():
    # Given
    card = atm.Card()
    a = atm.Atm()
    a.insert_card(card)

    # When
    a.deposit(1234,1, 100)

    # Then
    assert a.see_balance(1234, 1) == 100


def test_can_withdraw_by_atm():
    # Given
    card = atm.Card()
    a = atm.Atm()
    a.insert_card(card)
    a.deposit(1234,1, 100)

    # When
    a.withdraw(1234, 1, 100)

    # Then
    assert a.see_balance(1234, 1) == 0
