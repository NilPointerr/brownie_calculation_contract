from brownie import accounts, config, practice, network
import os
from dotenv import load_dotenv

load_dotenv()


def deploy_calculation_contract():
    # account = get_account()
    # SET ACCOUNT
    account1 = accounts.load("nilesh-account")
    print(account1)

    # DEPLOY CONTRACT
    simple_calculation = practice.deploy({"from": account1})
    print(simple_calculation)

    # INTERACT WITH CALUCALTE FUNCTION FROM CONTRACT
    multiplication = simple_calculation.calculate(25, 25, "*", {"from": account1})
    print(multiplication)
    multiplication.wait(1)

    # PRINT OUTPUT OF CALCULATE FUNCTION
    updated_ans = simple_calculation.viewAns()
    print(updated_ans)

    # infura = accounts.add(os.getenv("WEB3_INFURA_PROJECT_ID"))
    # print("*************************************************************************")
    # print(infura)


def get_account():
    if network.show_active() == "developement":
        return accounts[0]
    else:
        print("it's else part")
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_calculation_contract()
