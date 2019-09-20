import requests
import geopy.distance


def get_response(url):
    """
    Gets the json object from the url (if it exists. Prints error is it does not exist.
    :param url: the url for the request.
    :return: the json object from the url.
    """
    url_output = requests.get(url)

    # check whether the request was successful
    if url_output.status_code == 200:
        return url_output.json()
    else:
        print("An error occurred")


def calc_distance(lat_origin, long_origin, lat_dest, long_dest):
    """
    Returns the number of meters from the origin point to the destination point using
    the latitude and longitude of both points.
    :param lat_origin: the latitude of the origin point.
    :param long_origin: the longitude of the origin point.
    :param lat_dest: the latitude of the destination point.
    :param long_dest: the longitude of the destination point.
    :return: the number of meters from the origin point to the destination.
    """
    origin = (lat_origin, long_origin)
    destination = (lat_dest, long_dest)

    return geopy.distance.vincenty(origin, destination).meters


url = 'https://raw.githubusercontent.com/storypark/web_developer_screener/master/staff_list.json'
data = get_response(url)

# access the staff from the json object
staff = data['staff']

for person in staff:
    print(person['id'])