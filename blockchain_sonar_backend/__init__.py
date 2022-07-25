#
# Application Factory.
# See for details https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/#basic-factories
#

from flask import Flask, Response, json
from werkzeug.exceptions import HTTPException

import os

from .version import __version__

def create_app():
	print("%s v%s" % (__name__, __version__))

	app = Flask(__name__, static_folder=None)
	
	# https://stackoverflow.com/a/54151093/2011679
	app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

	
	app.config.from_prefixed_env("BSE")

	from blockchain_sonar_backend.controllers.explorer_v1 import ExplorerV1Controller;
	from blockchain_sonar_backend.controllers.static import StaticController

	explorer_v1_controller_instance = ExplorerV1Controller()

	app.register_error_handler(HTTPException, _handle_exception)
	app.register_blueprint(explorer_v1_controller_instance.blueprint, url_prefix="/v1")

	root_path = app.root_path
	frontend_path = os.path.join(root_path, "..", "..", "frontend")
	if os.path.isdir(frontend_path):
		static_controller = StaticController(frontend_path)
		app.register_blueprint(static_controller.blueprint, url_prefix="/")
		app.logger.info("Frontend directory was found: %s" % frontend_path)
	else:
		app.logger.warn("Frontend directory was not found: %s" % frontend_path)

	return app

def _handle_exception(e: HTTPException) -> None:
	"""Return empty response instead of HTML for HTTP errors."""
	# start with the correct headers and status code from the error
	response: Response = e.get_response()
	response.status = "%s %s" % (response.status_code, e.name)
	response.data = b""
	response.headers = {"BS-REASON-PHRASE": e.name}
	return response
