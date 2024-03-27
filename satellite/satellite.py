import os
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/take_image/<target_sat>")
def take_image(target_sat):
    """take an image of a target satellite"""
    pass


@app.route("/transmit_image/<target_sat>")
def transmit_image(target_sat):
    """transmit image of target sat to mcs """
    pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
