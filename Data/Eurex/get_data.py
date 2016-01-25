from urllib import urlretrieve
import pandas as pd
import requests
import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO
import datetime as dt
from os import path


url_path = 'http://www.stoxx.com/download/historical_values/'
data_folder = 'data/'  # Save file to local target destination.

stoxxeu600_url = url_path + 'hbrbcpe.txt'
stoxxeu600_filepath = data_folder + "stoxxeu600.txt"

vstoxx_url = url_path + 'h_vstoxx.txt'
vstoxx_filepath = data_folder + "vstoxx.txt"

def get_index_data(index_url, save_path):
    urlretrieve(index_url, save_path)

def check_data_files():
    # check stoxxeu600 file
    if path.isfile(stoxxeu600_filepath):
        if check_file_date(stoxxeu600_filepath):
            get_index_data(stoxxeu600_url, stoxxeu600_filepath)  # creates csv of data
            print 'got new stoxxeu600 data'
    else:  # no file found, get data
        get_index_data(stoxxeu600_url, stoxxeu600_filepath)  # creates csv of data
    # check vstoxx file
    if path.isfile(vstoxx_filepath):
        if check_file_date(vstoxx_filepath):
            get_index_data(vstoxx_url, vstoxx_filepath)  # creates csv of data
            print 'got new vstoxx data'
    else:  # no file found, get data
        get_index_data(vstoxx_url, vstoxx_filepath)  # creates csv of data


def check_file_date(data_file):
    today = dt.datetime.today().date()
    file_date = dt.datetime.fromtimestamp(path.getmtime(data_file)).date()
    if file_date < today:
        return True  # need to update
    else:
        return False  # file up to date


def get_stoxxeu600():
    columns = ['Date', 'SX5P', 'SX5E', 'SXXP', 'SXXE', 'SXXF', 'SXXA', 'DK5F', 'DKXF', 'EMPTY']
    # content = StringIO(requests.get(stoxxeu600_url).content)  # daily, so no necessary to download each time
    stoxxeu600 = pd.read_csv(stoxxeu600_filepath,  # change to file path and uncomment get_index_data line to read from file
                     index_col=0,
                     parse_dates=True,
                     dayfirst=True,
                     header=None,
                     skiprows=4,
                     names=columns,
                     sep=';'
                     )
    del stoxxeu600['EMPTY']
    return stoxxeu600

def get_vstoxx():
    # get_index_data(vstoxx_url, vstoxx_filepath)  # creates csv of data
    # content = StringIO(requests.get(vstoxx_url).content)  # daily, so no necessary to download each time
    vstoxx = pd.read_csv(vstoxx_filepath,  # change to file path and uncomment get_index_data line to read from file
                 index_col=0,
                 parse_dates=True,
                 dayfirst=True,
                 header=2)
    return vstoxx

def trim_and_merge(stoxxeu600_frame, vstoxx_frame):
    cutoff_date = max(stoxxeu600_frame.index.min(), vstoxx_frame.index.min())
    merged_data = pd.DataFrame(
    {'EUROSTOXX' :stoxxeu600['SX5E'][stoxxeu600.index >= cutoff_date],
     'VSTOXX':vstoxx['V2TX'][vstoxx.index >= cutoff_date]})

    return merged_data





check_data_files()
stoxxeu600 = get_stoxxeu600()
vstoxx = get_vstoxx()
merged = trim_and_merge(stoxxeu600, vstoxx)
print