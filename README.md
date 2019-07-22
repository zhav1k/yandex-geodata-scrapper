This is a yandex geocoder,written in Python 3, which is used to obtain location coordicates (longitude and latitude) by it's address.
# How to Use

1. First of all, you need to get an API_KEY by registering on https://developer.tech.yandex.ru
2. Afterwards, you can create an empty dataframe by yourself or use a function __create_df__, which contains **full_address**, **longitude**, **latitude** columns.
3. Then, you use function __extract_coordinates__ which takes as an input your dataframe(wich contains column with all adresses you are interested in), name of the column with addresses, empty dataframe from the previous step, your api key.


An output of the function is a dataframe, which contains the following columns: full address, longitude, latitude.
