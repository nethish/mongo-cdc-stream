# -*- coding: utf-8 -*-

from pprint import pprint
from time import sleep

from pymongo import MongoClient
from pymongo.errors import PyMongoError


def main():
    client = MongoClient(
        host="localhost",
        port=27017,
        directConnection=True,
        username=None,
        password=None,
    )

    while True:
        try:
            print("Connecting to MongoDB server and waiting for streams events...")

            with client.watch(pipeline=None, resume_after=None) as stream:
                for event in stream:
                    print(
                        f"Received event: {event.get('operationType')} "
                        f"for document: {event.get('documentKey', {}).get('_id')}."
                    )

                    pprint(event)

        except PyMongoError as error:
            print(
                f"An error has been raised. "
                f"Trying to resume after 30 seconds. "
                f"Error: {error}."
            )

            sleep(30)


if __name__ == "__main__":
    main()
