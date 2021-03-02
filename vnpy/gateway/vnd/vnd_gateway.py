from datetime import datetime
from typing import List
from vnpy.trader.constant import (
    Direction,
    Offset,
    Exchange,
    OrderType,
    Product,
    Status,
    OptionType,
)
from vnpy.trader.gateway import BaseGateway
from vnpy.trader.object import (
    BarData,
    HistoryRequest,
    TickData,
    OrderData,
    TradeData,
    PositionData,
    AccountData,
    ContractData,
    OrderRequest,
    CancelRequest,
    SubscribeRequest,
)


class VndGateway(BaseGateway):
    _session = None

    def connect(self, setting: dict) -> None:
        return super().connect(setting)

    def close(self) -> None:
        return super().close()

    def subscribe(self, req: SubscribeRequest) -> None:
        return super().subscribe(req)

    def send_order(self, req: OrderRequest) -> str:
        return super().send_order(req)

    def cancel_order(self, req: CancelRequest) -> None:
        return super().cancel_order(req)

    def query_account(self) -> AccountData:
        return super().query_account()

    def query_position(self) -> PositionData:
        return super().query_position()

    def query_history(self, req: HistoryRequest) -> List[BarData]:
        return super().query_history(req)


class VndDataSubscriber:
    __process = None
    __gateway: VndGateway

    def __init__(self, gateway: VndGateway) -> None:
        self.__process = None

    def start(self) -> None:
        pass

    def get_tick(self, symbol: str) -> TickData:
        dt = datetime.utcnow()
        return TickData(self.__gateway.gateway_name, symbol, Exchange.HSX, dt)

    def get_bar(self, resolution) -> BarData:
        return BarData

    def fetch_data(self):
        bar = self.get_bar()
        self.__gateway.on_tick(bar)