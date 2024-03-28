import os
import base64
import random
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/take-image/<target_sat>")
def take_image(target_sat):
    """take an image of a target satellite"""

    # obtain image of "satellite"
    with open(f"hidden-images/sat{random.randint(0, 3)}.png", "rb") as image:
        f = image.read()
        b = bytearray(f)
        image_bytearray = base64.b64encode(b).decode('utf-8')

    # return bytea
    return jsonify({"image_data": image_bytearray}), 200


@app.route("/transmit-image/<target_sat>")
def transmit_image(target_sat):
    """transmit image of target sat to mcs"""
    pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(debug=True, host="0.0.0.0", port=port)
