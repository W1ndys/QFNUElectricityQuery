"""
低余额提醒
当余额低于30元时，发送提醒
"""

import ElectricityQuery
import feishu
import os
from dotenv import load_dotenv

load_dotenv()


class BalanceAlertManager:
    def __init__(self, balance):
        # 阈值
        self.threshold = 30
        self.balance = float(balance)

    def check_balance(self):
        if self.balance < self.threshold:
            return True
        else:
            return False


if __name__ == "__main__":
    OPEN_ID = os.getenv("OPEN_ID")
    eq = ElectricityQuery.ElectricityQuery(OPEN_ID)
    balance = eq.get_balance()
    balance_alert_manager = BalanceAlertManager(balance)
    if balance_alert_manager.check_balance():
        print(f"余额低于{balance_alert_manager.threshold}元，发送提醒")
        feishu.feishu(
            f"宿舍电费余额低于{balance_alert_manager.threshold}元",
            f"余额为{balance}元",
        )
    else:
        print(f"余额高于{balance_alert_manager.threshold}元（{balance}元），不发送提醒")
        # feishu.feishu(
        #     f"宿舍电费余额高于{balance_alert_manager.threshold}元",
        #     f"余额为{balance}元",
        # )
