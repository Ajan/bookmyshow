# Ticket Availability Checker

This script checks the availability of movie tickets on BookMyShow website and sends an email notification if tickets are available for a specific show at a particular venue.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository or download the script file `ticket_availability_checker.py` directly.

2. Install the required dependencies by running the following command:

- pip install requests beautifulsoup4


## Configuration

Before running the script, you need to configure the following parameters in the code:

- `site`: Replace with the URL of the movie and city on BookMyShow.
- `date`: Replace with the desired date in the format `YYYYMMDD`.
- `venue`: Replace with the venue code of the desired theater (can be found by inspecting the element data-id for the venue).
- `show`: Replace with the preferred show timing.
- `delay`: Time gap in seconds between two script runs.
- `TO`: Email address to which you want to receive the availability notification.
- `GMAIL_USER` and `GMAIL_PASS`: Your Gmail credentials. Ensure that you have allowed access for "less secure apps" in your Gmail account settings.

## Usage

Run the script using the following command:

- python ticket_availability_checker.py


The script will check the availability of tickets in the specified interval (defined by `delay`). If tickets are available, it will send an email notification to the configured email address.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was developed based on an initial version by [Aakarsh B](https://github.com/Aakarsh-B).
