import time
from typing import Optional
from logger import Logger


class Timer:
    """A class for measuring time intervals."""

    def __init__(self, name: str) -> None:
        self.name = f"Timer{name.title()}"
        self.logger = Logger(self.name)
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None

    def start(self) -> None:
        """Starts the timer."""
        self.start_time = time.time()
        self.logger.info("Timer started.")

    def stop(self) -> None:
        """Stops the timer and logs the elapsed time in minutes and seconds."""
        if self.start_time is None:
            self.logger.warning("Timer was not started.")
            return

        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time

        # Calculate minutes and seconds
        minutes = int(self.elapsed_time // 60)
        seconds = self.elapsed_time % 60

        # Log elapsed time in minutes and seconds
        self.logger.info(
            f"Timer stopped. Elapsed time: {minutes} minutes and {seconds:.2f} seconds."
        )

    def reset(self) -> None:
        """Resets the timer."""
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        self.logger.info("Timer reset.")

    def get_elapsed_time(self) -> Optional[float]:
        """Returns the elapsed time if the timer has been stopped."""
       if self.elapsed_time is None:
            self.logger.warning("Timer has not been stopped yet.")
            return None
        return self.elapsed_time
