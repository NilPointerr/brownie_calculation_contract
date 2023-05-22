from brownie import accounts, practice


def test_contract():
    # Arrange
    account = accounts[0]

    # Act
    cal = practice.deploy({"from": account})
    value = cal.viewAns()
    expected = 0

    # Assert
    assert value == expected
