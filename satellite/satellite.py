import os
import random
import shutil
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/take-image/<target_sat>")
def take_image(target_sat):
    """take an image of a target satellite"""

    # "take" image
    shutil.copy(
        f"hidden-images/sat{random.randint(0, 3)}.png",
        # NOTE: this wont work for more than one image of each satellite
        f"taken-images/{target_sat}.png",
    )

    return jsonify({"SUCCESS": "Image taken successfully"}), 200


@app.route("/transmit-image/<target_sat>")
def transmit_image(target_sat):
    """transmit image of target sat to mcs"""

    image_path = f"taken-images/{target_sat}.png"

    # obtain image of "satellite"
    with open(image_path, "rb") as f:
        image_bytes = f.read()
        base64_encoded_image = image_bytes.hex()

    # return bytea
    return {"image_data": base64_encoded_image}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(debug=True, host="0.0.0.0", port=port)
