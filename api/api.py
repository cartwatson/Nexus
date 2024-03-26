from flask import Flask, jsonify

api = Flask(__name__)


@api.route("/add-satellite/satellite_id")
def add_tracked_satellite(satellite_id):
    """Add tracked satellite to database"""
    # make post request to db container
    pass


@api.route("/get-image-from-satellite/<satellite_id>")
def get_image_from_satellite(satellite_id):
    """request image of a tracked satellite, store these requests"""
    # CLARIFICATION: does this need a specific image id as well???
    # make get request from db container
    # return data as json object, status code # eg: jsonify(python_dict), 200
    return jsonify({"satellite_id": satellite_id}), 200  # DEBUG: REMOVE BEFORE PROD
    pass


@api.route("/get-droid-images")
def get_images_from_droid():
    """get images of tracked satellite take by DROID"""
    # make get request to db container
    # return list of images
    pass


if __name__ == "__main__":
    api.run(debug=True)
