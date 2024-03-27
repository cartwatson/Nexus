import os
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

    cur.execute(
        f"""SELECT img FROM images
        WHERE id_sat='{satellite_id}'
        """
    )
    results = cur.fetchall()

    if not results:
        return jsonify({"ERROR": f"No images found for {satellite_id}"}), 204

    return jsonify({results})


@app.route("/get-droid-images")
def get_images_from_droid():
    """get images of tracked satellite take by DROID"""
    cur.execute("SELECT img FROM images WHERE id_sat='DROID'")
    results = cur.fetchall()
    if not results:
        return jsonify({"ERROR": "No images found for DROID"}), 204

    return jsonify({results})


if __name__ == "__main__":
    # init psycopg2
    conn = psycopg2.connect(
        host="pg",
        dbname="takehome",
        user="takehome",
        password="takehome",
        port="5432",
    )

    cur = conn.cursor()
    conn.autocommit = True

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

    cur.close()
    conn.close()
