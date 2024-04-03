import datetime

class Logger:
    """If a log file for today already exists, open it in append mode.
    Else, create a new log file for today, and open it in append mode.
    """
    DEBUG = False
    FORMAT = "{datetime:%Y-%m-%d %I:%M %p} | {type:} | {msg}\n"
    FILE = open(f"D:/Study Videos/SQA/Python/pythonSQAProject/SampleProject4/LogFiles/lo"
                f"g{datetime.datetime.now():%d-%m-%Y}.log", "a+") # logfile create in this path

    @classmethod
    def log(cls, msg, level):
        if not cls.DEBUG and level == "DEBUG":
            return
        cls.FILE.write(cls.FORMAT.format(
            type=level,
            msg=msg,
            datetime=datetime.datetime.now()
        ))

    @classmethod
    def info(cls, msg):
        """Log info"""
        cls.log(msg, "INFO")

    @classmethod
    def update(cls, msg):
        "Used to log whenever a state is updated"
        cls.log(msg, "UPDATE")

    @classmethod
    def exception(cls, msg):
        cls.log(msg, "EXCEPTION")

    @classmethod
    def debug(cls, msg):
        "Only logs if the static variable {DEBUG} is set to True."
        cls.log(msg, "DEBUG")

    @classmethod
    def clear(cls):
        """Clears the log file"""
        cls.FILE.truncate(0)

    @classmethod
    def object(cls, object):
        """Intended for use on objects. They usually have a lot of information;
        therefore, we enclose the information with lines to make the log more readable."""
        cls.FILE.write(
            f"-----------------------       object log\n"
            + str(object)
            + f"\n-----------------------\n"
        )