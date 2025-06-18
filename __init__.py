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


class APOD:
    """
    """


    def __init__( self,
                  key,
                  start=None,
                  end=None,
                  count=None  ):
        """
        
        """

        _url = "https://api.nasa.gov/planetary/apod?api_key={key}"

        # Pull `count` number of random images.
        if count is not None and start is None:
            data = get(
                f"{_url}&count={count}"
            )

        # Pull back-dated images starting from `start` up to `end`.
        if end is not None:
            data = get(
                f"{_url}&start_date={start}&end={end}"
            )

        # Pull a single, specific date.
        if end is None and start is not None:
            data = get(
                f"{_url}&date={start}
            )

        # Pull todays date.
        if start is None:
            data = get( _url )

        data = loads(data)


if __name__ == "__main__":
    args = ArgumentParser()

    args.add_argument("-s", "--start",  type=ISO8601,  default=None )
    args.add_argument("-e", "--end",    type=ISO8601,  default=None )
    args.add_argument("-r", "--random", type=int,      default=None )

    args = args.parse_args()
