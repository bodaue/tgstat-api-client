class TGStatError(Exception):
    """
    Base exception for all TGStat errors.
    """
    pass


class ChatNotFound(TGStatError):
    pass
