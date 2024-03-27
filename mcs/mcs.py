import time
import random
import psycopg2

# NOTES:
# upload images to psql
# https://www.postgresql.org/docs/7.4/jdbc-binary-data.html


# When the MCS is able to communicate with the satellite, send imaging requests to the satellite that the MCS finds in the database.
def send_image_requests():
    """get all images from satellite"""
    # send requests to satellite for unfulfilled requests
    pass


# Periodically send a “download all images” command to the satellite to get all images stored on the satellite and insert into the database.
def download_all_images():
    """download all images from satellite to db"""
    # query for images
    # push image to db
    pass


def main():
    connected = False
    while not connected:
        try:
            # init psycopg2
            conn = psycopg2.connect(
                host="pg",
                dbname="takehome",
                user="takehome",
                password="takehome",
                port="5432",
            )
            print("connection established")
            connected = True
        except:  # noqa: E722
            print("connection failed: attempting reconnect in 1sec")
            time.sleep(1)

    cur = conn.cursor()
    conn.autocommit = True

    while True:
        print("ESTABLISHING COMMUNICATION WITH DROID")
        send_image_requests()
        download_all_images()
        print("COMMUNICATION LOST...")
        # system to intermittetly create contacts with satellite
        time.sleep(random.randint(5, 10))


if __name__ == "__main__":
    main()
