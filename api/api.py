import os
import io
import time
import json
from PIL import Image
from datetime import datetime
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.route("/add-satellite/<satellite_id>")
def add_tracked_satellite(satellite_id):
    """Add tracked satellite to database"""

    try:
        cur.execute(
            f"""INSERT INTO satellites (id) VALUES
            ('{satellite_id}')
            """
        )
    except:
        return jsonify({"FAILURE": f"Already tracking: {satellite_id}"}), 500

    return jsonify({"SUCCESS": f"Now tracking: {satellite_id}"}), 200


@app.route("/request-image-of-satellite/<target_sat>")
def request_image_of_satellite(target_sat):
    """request image of a tracked satellite"""

    cur.execute(
        f"""INSERT INTO requests (target_sat, time, fulfilled, pending) VALUES
        ('{target_sat}', '{datetime.now()}', 'FALSE', 'FALSE')
        """
    )

    return jsonify({"SUCCESS": f"Request for image of {target_sat} submitted"}), 200


def get_image(satellite_id, taken_by=None):
    """get image of a specific satellite"""

    request = f"SELECT img FROM images WHERE id_sat='{satellite_id}'"
    if taken_by:
        request += f"AND taken_by='{taken_by}'"

    # Make request for image
    cur.execute(request)
    # results = cur.fetchall()

    row = cur.fetchone()
    if row:
        json_data = json.loads(row[0].tobytes())
        base64_encoded_image = json_data["image_data"]
        image_bytes = bytes.fromhex(base64_encoded_image)
        image = Image.open(io.BytesIO(image_bytes))
        image.save(f"images/{satellite_id}.png")
    else:
        print("No image data found in the database")

    return jsonify({"SUCCESS": "Image retrieved and displayed successfully"}), 200


@app.route("/get-images-from-droid/<satellite_id>")
def get_images_from_droid(satellite_id):
    """get images of a tracked satellite taken by DROID"""
    return get_image(satellite_id, taken_by="DROID")


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

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

    cur.close()
    conn.close()
