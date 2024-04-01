import time
import json
import random
import psycopg2
import requests
from datetime import datetime


def send_image_requests(cur):
    """send requests to satellite for unfulfilled requests"""

    # get image requests & don't resend fulfilled and pending requests
    cur.execute("SELECT * FROM requests WHERE fulfilled='FALSE' AND pending='FALSE'")
    results = cur.fetchall()

    if not len(results):
        return

    print("TRANSMITTING REQUESTS...")
    for request in results:
        # NOTE: these idx's will change if db changes...
        time_stamp = request[0]
        sat_id = request[1]

        # send request to droid to take image of target satellite
        requests.get(f"http://satellite:5050/take-image/{sat_id}")
        # mark request as pending
        cur.execute(f"UPDATE requests SET pending='TRUE' WHERE time='{time_stamp}'")


def download_all_images(cur, droid_id):
    """download all images from satellite to db"""

    # get image requests to be fulfilled but that have already been sent to sat/droid
    cur.execute("SELECT * FROM requests WHERE fulfilled='FALSE' AND pending='TRUE'")
    results = cur.fetchall()

    # if no pending requests
    if not len(results):
        return

    print("DOWNLOADING IMAGES...")
    for request in results:
        # NOTE: these idx's will change if db changes...
        time_stamp = request[0]
        sat_id = request[1]

        # query droid for image based on request
        try:
            json_data = requests.get(f"http://satellite:5050/transmit-image/{sat_id}").json()

            # FIX: this datetime.now() call
            cur.execute(
                f"""INSERT INTO images (time_taken, taken_by, id_sat, img) VALUES
                ('{datetime.now()}', '{droid_id}', '{sat_id}', '{json.dumps(json_data)}')
                """
            )

            cur.execute(f"UPDATE requests SET fulfilled='TRUE' WHERE time='{time_stamp}'")
        except:
            print(f"FAILURE: unable to obtain image for {sat_id} or failure to upload to db")
            continue


def main(cur):
    while True:
        # NOTE: future work could allow droids to be added to mcs while running
        droid = "DROID"
        print(f"ESTABLISHING COMMUNICATION WITH {droid}")
        download_all_images(cur, droid)
        send_image_requests(cur)
        print(f"COMMUNICATION WITH {droid} LOST...")
        # system to intermittetly create contacts with satellite
        time.sleep(random.randint(5, 10))


if __name__ == "__main__":
    # Ensure connection to db before attempting to connect
    connected = False
    while not connected:
        try:
            conn = psycopg2.connect(
                host="pg",
                dbname="takehome",
                user="takehome",
                password="takehome",
                port="5432",
            )
            print("connection established")
            connected = True
        except psycopg2.OperationalError:
            print("connection to db failed: attempting reconnect in 1sec...")
            time.sleep(1)

    cur = conn.cursor()
    conn.autocommit = True

    # Ensure db tables are created before attempting to access
    db_init = False
    while not db_init:
        try:
            cur.execute("SELECT * FROM images")
            db_init = True
        except:  # noqa: E722
            print("Postgresql tables not initialized: checking again in 3sec...")
            time.sleep(3)

    main(cur)
