import os
import time
from datetime import datetime
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.route("/add-satellite/<satellite_id>")
def add_tracked_satellite(satellite_id):
    """Add tracked satellite to database"""

    cur.execute(
        f"""INSERT INTO satellites (user_id) VALUES
        ('{satellite_id}')
        """
    )

    return jsonify({"added-id": satellite_id}), 200


@app.route("/get-image-from-satellite/<satellite_id>")
def get_image_from_satellite(satellite_id):
    """request image of a tracked satellite, store these requests"""

    request = f"SELECT img FROM images WHERE id_sat='{satellite_id}'"

    # Make request for image
    cur.execute(request)
    results = cur.fetchall()

    success = len(results)
    # Record request for image
    cur.execute(
        f"""INSERT INTO requests (id_sat, time, request, img_returned) VALUES
        ('{satellite_id}', '{datetime.now()}', \
        '{request.replace("'", "''")}', '{str(success).upper()}')
        """
    )

    if not success:
        # NOTE: possibility this should be a 204
        return jsonify({"ERROR": f"{satellite_id} exists but no images found"}), 200
    # TODO: do something with results as they'll be raw image data
    return jsonify({"results": results}), 200


@app.route("/get-droid-images")
def get_images_from_droid():
    """get images of tracked satellite take by DROID"""

    # NOTE: if get_image_from_satellite later takes image_id, return all images
    return get_image_from_satellite('DROID')


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
            print("connection failed: attempting reconnect in 1sec")
            time.sleep(1)

    cur = conn.cursor()
    conn.autocommit = True

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

    cur.close()
    conn.close()
