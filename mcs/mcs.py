import time
import random
import psycopg2

# NOTES:
# request looks like
# datetime                                      target_sat, fulfillled, pending
# (datetime.datetime(2024, 3, 27, 7, 1, 44, 308839), 'object0', False, False)
# upload images to psql
# https://www.postgresql.org/docs/7.4/jdbc-binary-data.html


def send_image_requests(cur):
    """send requests to satellite for unfulfilled requests"""

    # get image requests # sort out ones that are already fulfilled
    cur.execute("SELECT * FROM requests WHERE fulfilled='FALSE' AND pending='FALSE'")
    results = cur.fetchall()

    pending_requests = len(results)

    if not pending_requests:
        return

    print("REQUESTING...")  # DEBUG: REMOVE BEFORE PROD
    for request in results:
        print(request)  # DEBUG: REMOVE BEFORE PROD
        # send request to droid to take image of target satellite
        # mark request as pending
        cur.execute(f"UPDATE requests SET pending='TRUE' WHERE time='{request[0]}'")
    return


def download_all_images(cur):
    """download all images from satellite to db"""

    # set image request to fulfilled in db table
    cur.execute("SELECT * FROM requests WHERE fulfilled='FALSE' AND pending='TRUE'")
    results = cur.fetchall()

    unfulfilled_requests = len(results)

    if not unfulfilled_requests:
        return

    print("DOWNLOADING...")  # DEBUG: REMOVE BEFORE PROD
    for request in results:
        print(request)  # DEBUG: REMOVE BEFORE PROD
        # query droid for image based on request
        # if image exists, update request
        cur.execute(f"UPDATE requests SET fulfilled='TRUE' WHERE time='{request[0]}'")
        # push image to db
    pass


def main(cur):
    while True:
        print("ESTABLISHING COMMUNICATION WITH DROID")
        download_all_images(cur)
        send_image_requests(cur)
        print("COMMUNICATION LOST...")
        # system to intermittetly create contacts with satellite
        time.sleep(random.randint(5, 10))


if __name__ == "__main__":
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
            print("connection to db failed: attempting reconnect in 1sec")
            time.sleep(1)

    cur = conn.cursor()
    conn.autocommit = True

    main(cur)
