import os
import io
import time
import json
from PIL import Image
from datetime import datetime
from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def return_json(success, message, data=None, status_code=500):
    """Create response for api"""
    return {
        "Success": success,
        "Message": message,
        "Data" : data
    }, status_code


# expects id of satellite to track as param on request
@app.route("/track-satellite")
def add_tracked_satellite():
    """Add tracked satellite to database"""
    
    sat_id = request.args.get('id')
    # if no params provided, return list of all tracked satellites
    if sat_id is None:
        try:
            cur.execute("SELECT id FROM satellites")
            satellites = cur.fetchall()  # NOTE: check type here
            return return_json(True, "Provided data is all tracked satellites.", satellites, 200)
        except:
            return return_json(False, "Unable to get list of tracked satellites!", None, 500)
    
    try:
        cur.execute(
            f"""INSERT INTO satellites (id) VALUES
            ('{sat_id}')
            """
        )
    except psycopg2.errors.UniqueViolation:
        return return_json(False, f"Already tracking {sat_id}!", None, 500)
    except psycopg2.errors:
        return return_json(False, f"Error attempting to add satellite as tracked in database!", None, 500)

    return return_json(True, f"Now tracking{sat_id}", None, 200)


@app.route("/request-image")
def request_image_of_satellite():
    """request image of a tracked satellite"""

    target_sat = request.args.get('id')
    if target_sat is None
        return return_json(False, "No id provided!", None, 400)

    try:
        cur.execute(
            f"""INSERT INTO requests (target_sat, time, fulfilled, pending) VALUES
            ('{target_sat}', '{datetime.now()}', 'FALSE', 'FALSE')
            """
        )
    except psycopg2.errors:
        return return_json(False, f"Error submitting request for image of {sat_id}.", None, 500)

    return return_json(True, f"Request for image of {sat_id} submitted.", None, 200)


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
        return return_json(False, f"No image found in database for {sat_id}!", None, 500)

    return return_json(True, f"Image of {sat_id} retrieved, saved in {image_save_dest}", base64_encoded_image, 200)


@app.route("/images")
def get_images_from_droid():
    """get images of a tracked satellite taken by DROID"""
        
    try:
        sat_id = request.args.get('id')
        try:
            droid_id = request.args.get('droid')
            return get_image(sat_id, droid_id)
        except:
            # if droid id not specified, its implied its DROID
            return get_image(sat_id, taken_by="DROID")
    except: # TODO: find correct error code for when .get doesn't work
        # TODO: could return all images, make request for all satellite ids and push request through
        return return_json(False, "id of satellite not provided!", None, 400)
    

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
            print("connection to db failed: attempting reconnect in 1sec...")
            time.sleep(1)

    cur = conn.cursor()
    conn.autocommit = True
    
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

    cur.close()
    conn.close()
