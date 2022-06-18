#
# See https://stackoverflow.com/questions/55248703/how-use-flask-route-with-class-based-view
#

from flask import Blueprint, Response, current_app, jsonify, request, send_from_directory

class StaticController(object):

	def __init__(self, static_folder: str):
		self._static_folder = static_folder

		self.blueprint = Blueprint('Static', __name__)
		self.blueprint.add_url_rule('/<path:name>', methods=["GET"], view_func=self._download_file)

	def _download_file(self, name: str):
		return send_from_directory(self._static_folder, name)
