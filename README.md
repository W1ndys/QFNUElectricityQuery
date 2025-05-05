# QFNUElectricityQuery

曲阜师范大学新校区电费查询脚本

## 使用方法

1. 安装依赖

```bash
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
source venv/bin/activate
# 安装依赖
pip install -r requirements.txt
```

2. 配置环境变量

在脚本目录下创建.env 文件，并添加以下内容：

```bash
OPEN_ID=你的openID
FEISHU_BOT_URL=你的飞书机器人URL
FEISHU_BOT_SECRET=你的飞书机器人密钥
```

3. 运行脚本

```bash
python BalanceAlertManager.py
```

每次运行脚本时，会检查当前余额是否低于 30 元，如果低于 30 元，则发送提醒。你可以部署在服务器上，每天定时运行。

如果你想调整提醒的阈值，可以修改 BalanceAlertManager.py 中的 threshold 变量。

```python
class BalanceAlertManager:
    def __init__(self, balance):
        # 阈值
        self.threshold = 30
        self.balance = float(balance)
```

## openID 获取方法

1. 打开微信，进入“Qsd 学生公寓”公众号
2. 点击下方菜单栏
3. 点击右上角
4. 复制链接，得到一个形如`http://wechat.sdkdch.cn/h5/?openId=xxxxxxxxxxxxxxxxxx`的链接
5. 将链接中的`http://wechat.sdkdch.cn/h5/?openId=xxxxxxxxxxxxxxxxxx`中的`openId`后面的内容作为`OPEN_ID`的值
