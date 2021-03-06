from tap_kit import TapExecutor, BaseClient, main_method

from .streams import STREAMS
from .dummy_catalog import dummy_catalog

REQUIRED_CONFIG_KEYS = ["start_date", 'api_key']


class GreenhouseTap(TapExecutor):
    auth_type = 'basic_key'
    url = 'https://harvest.greenhouse.io/v1/'
    pagination_type = 'next'
    replication_key_format = 'iso8061'


def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        GreenhouseTap,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
