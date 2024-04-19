import logging


def log(msg, error=None) -> None:
    """
    Logs the information. Raises error if message is error.

    Args:
        msg: str, information of log; verbose when error.
    Returns:
        None
    """
    logging.error(msg)
    if error is not None:
        raise error(msg)