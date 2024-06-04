import os
import io
import time
import json
from PIL import Image
from datetime import datetime
from flask import Flask, request
from flask_cors import CORS
import psycopg2
import utils


app = Flask(__name__)
cors = CORS(app)


# home route to test if api endpoint is working
@app.route("/")
def api_status():
    return utils.return_json(True, "API is running...", None, 200)


# expects id of satellite to track as param on request
@app.route("/track-satellite")
def add_tracked_satellite():
    """Add tracked satellite to database"""

    sat_id = request.args.get('id')

    if sat_id is not None:
        # validate name further
        valid_id, message = utils.valid_satellite_name(sat_id)
        if not valid_id:
            return utils.return_json(False, f"{sat_id} is an invalid name! {message}", None, 500)
            

        # valid param given, attempt to track satellite
        sat_id = sat_id.lower()
        try:
            cur.execute(
                f"""INSERT INTO satellites (id) VALUES
                ('{sat_id}')
                """
            )
        except psycopg2.errors.UniqueViolation:
            return utils.return_json(False, f"Already tracking {sat_id}!", None, 500)
        except psycopg2.errors:
            return utils.return_json(False, f"Error occured while attempting to add {sat_id} as tracked in database!", None, 500)

        return utils.return_json(True, f"Now tracking {sat_id}", None, 201)

    # if no URL params provided, return list of all tracked satellites
    try:
        cur.execute("SELECT * FROM satellites")
        satellites = cur.fetchall()
        # Get column headers from cursor.description
        columns = [desc[0] for desc in cur.description]
        # Convert each tuple to a dictionary using column headers
        satellites_processed = [dict(zip(columns, row)) for row in satellites]
        return utils.return_json(True, "Provided data is a list of all tracked satellites.", satellites_processed, 200)
    except:
        return utils.return_json(False, "Unable to get list of tracked satellites!", None, 500)


@app.route("/request-image")
def request_image_of_satellite():
    """request image of a tracked satellite"""

    sat_id = request.args.get('id')
    if sat_id is None:
        return utils.return_json(False, "No id provided!", None, 400)

    try:
        cur.execute(
            f"""INSERT INTO requests (target_sat, time, fulfilled, pending) VALUES
            ('{sat_id}', '{datetime.now()}', 'FALSE', 'FALSE')
            """
        )
    except psycopg2.IntegrityError:
        return utils.return_json(False, f"Error submitting request for image of {sat_id}: satellite not tracked!", None, 500)
    except Exception:
        return utils.return_json(False, f"Unknown error submitting request for image of {sat_id}.", None, 500)

    return utils.return_json(True, f"Request for image of {sat_id} submitted.", None, 201)


def get_image(sat_id, taken_by=None):
    """get image of a specific satellite"""

    request = f"SELECT img FROM images WHERE id_sat='{sat_id}'"
    if taken_by:
        request += f"AND taken_by='{taken_by}'"

    # Make request for image
    cur.execute(request)
    # results = cur.fetchall()

    row = cur.fetchone()
    image_save_dest = f"images/{sat_id}.png"
    if row:
        json_data = json.loads(row[0].tobytes())
        base64_encoded_image = json_data["image_data"]
        image_bytes = bytes.fromhex(base64_encoded_image)
        image = Image.open(io.BytesIO(image_bytes))
        image.save(image_save_dest)
    else:
        return utils.return_json(False, f"No image found in database for {sat_id}!", None, 500)

    return utils.return_json(True, f"Image of {sat_id} retrieved, saved in {image_save_dest}", base64_encoded_image, 200)


@app.route("/images")
def get_images_from_droid():
    """get images of a tracked satellite taken by DROID"""

    # get key-value URL params
    sat_id = request.args.get('id')
    droid_id = request.args.get('droid')

    if sat_id is not None:
        if droid_id is not None:
            return get_image(sat_id, taken_by=droid_id)
        return get_image(sat_id, taken_by="DROID")
    # if sat_id and droid_id not provided return all images
    try:
        cur.execute("SELECT id FROM satellites")
        satellites = cur.fetchall()
        satellites_processed = [ x for xs in satellites for x in xs ]
        images = {}
        for satellite in satellites_processed:
            image_data = get_image(satellite)[0]["Data"]
            if image_data is not None:
                images[satellite] = image_data
        if images != {}:
            return utils.return_json(True, "JSON object of binary data of images, all images saved in container (app/images/<satellite_id>.png)", images, 200)
        return utils.return_json(False, "No images found!", None, 500)
    except psycopg2.errors:
        return utils.return_json(False, "Error attempting to return all images", None, 500)


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
        except Exception:
            print("Postgresql tables not initialized: checking again in 3sec...")
            time.sleep(3)

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

    cur.close()
    conn.close()
