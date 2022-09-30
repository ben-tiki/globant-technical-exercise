import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
import statistics


def get_count():
    """
    Function that consumes the API and returns the number of berrys.

    Returns:
        berry_count {int} -- Number of berrys.
    """
    try:

        # we make an initial request to obtain the number of berrys
        # maybe berrys are added in the future, so we need to know how many there are (to avoid hardcoding)
        berry_count_request = requests.get('https://pokeapi.co/api/v2/berry')

        if berry_count_request.status_code == 200:
            berry_count = berry_count_request.json()['count']
        else:
            berry_count = 0

        return berry_count

    except Exception:

        return 0


async def get_data(berry_count: int):
    """
    Function that consumes the API and returns the data of the berrys. From id 1 to the berry_count.

    Arguments:
        berry_count {int} -- Number of berrys.

    Returns:
        berry_data {list} -- List of dictionaries with the data of the berrys.
    """

    try:

        # creates a list to populate with each request
        berry_data = []
        with ThreadPoolExecutor(max_workers=25) as executor:
            loop = asyncio.get_event_loop()
            tasks = [
                loop.run_in_executor(
                    executor,
                    requests.get,
                    'https://pokeapi.co/api/v2/berry/{}'.format(berry_id)
                )
                for berry_id in range(1, berry_count + 1)
            ]

            # iterates over the responses
            for response in await asyncio.gather(*tasks):
                # if the request was successful (status code 200), then we append the data to the list
                if response.status_code == 200:
                    berry_response = response.json()
                    berry_data.append({
                        'id': berry_response['id'],
                        'name': berry_response['name'],
                        'growth_time': berry_response['growth_time']
                    })

                else:
                    # if in any case the request was not successful, berry data is empty
                    berry_data = {}

            return berry_data

    except Exception:

        return {}


def format_data(berry_data: list, for_dashboard: bool = False):
    """
    Function that formats the data of the berrys.
    
    Arguments:
        berry_data {list} -- List of dictionaries with the data of the berrys.

    Returns:
        growth_metrics_dict {dict} -- Dictionary with the metrics of the berrys.
    """

    try:
        # we create a dictionary to populate with the metrics
        growth_time_list = [berry['growth_time'] for berry in berry_data]
        growth_metrics_dict = {"berries_names": [berry['name'] for berry in berry_data],
                               'min_growth_time': min(growth_time_list),
                               'median_growth_time': round(statistics.median(growth_time_list), 2),
                               'max_growth_time': max(growth_time_list),
                               "variance_growth_time": round(statistics.variance(growth_time_list), 2),
                               'mean_growth_time': round(statistics.mean(growth_time_list), 2),
                               "frequency_growth_time": round(statistics.mode(growth_time_list), 2),
                               }

        if for_dashboard:
            # if the function is called from the dashboard, then we add data necessary for the plot
            growth_metrics_dict['growth_time_list'] = growth_time_list

        return growth_metrics_dict

    except Exception:
        return {}


def main(for_dashboard: bool = False):
    """
    Main function.
    """
    while True:

        berry_count = get_count()

        if berry_count == 0:
            return {"error": "Error getting the number of berrys"}

        berry_data = asyncio.run(get_data(berry_count))

        if berry_data == {}:
            return {"error": "Error getting the data of the berrys"}

        growth_metrics_dict = format_data(berry_data, for_dashboard)

        if growth_metrics_dict == {}:
            return {"error": "Error formatting the data of the berrys"}

        return growth_metrics_dict


if __name__ == '__main__':

    main()
