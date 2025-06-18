from requests import get
from datetime import datetime
from argparse import ArgumentParser
from argparse import ArgumentTypeError
from json import loads


today = datetime.strftime(datetime.today(), "%Y-%m-%d")


#TODO: move this to a STANDARDS module.
def ISO8601(date: str) -> datetime:
    """

        Converts a `date` datetime object into an ISO8061 type object
    for validating user input for dates.

        Defines the ISO8061 dating format as an internal datatype;
    useful for trivializing datetime objects.
    """
    try:
        return datetime.strptime(date, "%Y-%m-%d")

    except ValueError:
        raise ArgumentTypeError(
            f"{date} is not a valid date; please use the ISO8601 "
            f"format: YYYY-MM-DD."
        )


class FlagError(Exception):
    def __init__(self, message)
        super().__init__(message)


class APOD:
    """
    """


    def __init__( self,
                  key,
                  start=None,
                  end=None,
                  count=None  ):
        """
            Pull the picture of the day from the NASA website.  By default
        it grabs todays most recent picture, however it is very easy to select
        pictures from a range of historic days as well as random pictures from
        a multitude of days.
        
        """

        _url = f"https://api.nasa.gov/planetary/apod?api_key={key}"


        """ Pull a random count, if no other parameters are given. """
        if count is not None and (start is None and end is not None):
            data = loads( get(f"{_url}&count={count}") )

        """ If a count is given, and a start or end date is given,
        that's a FlagError. """
        else:
            raise FlagError(
                f"Random count and specified dates are not compatible.\n"
                f"Please only use either --random or --start and --end."
            ); exit()

        """ If no count is given and we have either a start or an end,
        we need more information before we can make a decision. """
        if count is None and (start is not None or end is not None):

            """ If we have an end date but no start date, we're pulling
            a range of dates starting with today. """
            if start is None and is end is not None:
                data = loads( get(f"{_url}&start_date={today}&end_date={end}") )

            """ If we have a start and an end date, we're pulling a range of
            dates that does not start with today. """
            elif start is not None and end is not None:

                # Check to make sure a valid range is given.
                if start <= end: raise FlagError(
                    "Start date can not be before end date."
                ); exit()
                # Otherwise, pull the range.
                else: data = loads(
                    get(f"{_url}&start_date={start}&end_date={end}")
                )

            """ If no values are given at all, then just pull todays image. """
            elif start is None and end is None:
                data = loads(
                    get(f"{_url}")
                )




if __name__ == "__main__":
    args = ArgumentParser()

    args.add_argument("-s", "--start",  type=ISO8601,  default=None )
    args.add_argument("-e", "--end",    type=ISO8601,  default=None )
    args.add_argument("-r", "--random", type=int,      default=None )

    args = args.parse_args()
