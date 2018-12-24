from abc import ABCMeta, abstractmethod

from common.exceptions import LogicError
from plenum.common.request import Request
from plenum.server.database_manager import DatabaseManager
from stp_core.common.log import getlogger

logger = getlogger()


class RequestHandler(metaclass=ABCMeta):
    def __init__(self, database_manager: DatabaseManager, txn_type, ledger_id):
        self.database_manager = database_manager
        self.txn_type = txn_type
        self.ledger_id = ledger_id

    @abstractmethod
    def static_validation(self, request: Request):
        """
        Does static validation like presence of required fields,
        properly formed request, etc
        """

    @abstractmethod
    def dynamic_validation(self, request: Request):
        """
        Does dynamic validation (state based validation) on request.
        Raises exception if request is invalid.
        """

    @property
    def state(self):
        return self.database_manager.get_database(self.ledger_id).state \
            if self.ledger_id else None

    @property
    def ledger(self):
        return self.database_manager.get_database(self.ledger_id).ledger \
            if self.ledger_id else None

    def _validate_type(self, request: Request):
        if request.txn_type != self.txn_type:
            raise LogicError
