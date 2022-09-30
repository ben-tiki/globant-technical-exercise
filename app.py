import os

from flask import Flask
from flask import json
from flask import render_template
from flask import redirect
from flask import Response

from modules.fetch_data import main

from modules.plot_histogram import plot_hist

app = Flask(__name__)


@app.route('/')
def index():
    """
    Function that redirects the "/" route to "/allBerryStats".
    """

    return redirect('/allBerryStats')


@app.route("/allBerryStats", methods=['GET'])
def allBerryStats():
    """ 
    Function that returns the metrics of the berrys. (in JSON format)
    
    Returns:
        growth_metrics_dict {dict} -- Dictionary with the growth metrics of the berrys.

    """
    # execute the main function
    growth_metrics_dict = main()

    # create response
    response = Response(response=json.dumps(growth_metrics_dict),
                        mimetype='application/json')

    return response

@app.route("/allBerryDashboard", methods=['GET'])
def allBerryDashboard():
    """ 
    Function that returns the metrics of the berrys.(in HTML format)
    
    Returns:
        growth_metrics_dict {dict} -- Dictionary with the metrics of the berrys.

    """
    # execute the main function
    growth_metrics_dict = main(for_dashboard=True)

    # get the image as a string
    pngImageB64String = plot_hist(growth_metrics_dict)

    return render_template("dashboard.html", image=pngImageB64String, growth_metrics_dict=growth_metrics_dict)


@app.route("/berries", methods=['GET'])
def berries():
    """
    Function that returns the list of berrys.
    """
    # execute the main function
    growth_metrics_dict = main()

    return render_template("berries.html", berries_names=growth_metrics_dict['berries_names'])


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(port=port)