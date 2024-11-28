#!/usr/bin/python
#  your ApplicationKey and ApiKey created in https://www.ecowitt.net/user/index (after login)
ApplicationKey = '61759DF4094EBA1A61E070A285A2DAF7'
ApiKey = 'fe33f769-d487-433c-a31d-8e504df4076f'

# MAC address of corresponding meteostation
MAC_station = '48:E7:29:5F:72:44'

# Units for requested data, see :  https://doc.ecowitt.net/web/#/apiv3en?page_id=17
UnitsEcowitt = '&temp_unitid=1&pressure_unitid=3&wind_speed_unitid=7&rainfall_unitid=12&solar_irradiance_unitid=16'

# https://api.ecowitt.net/api/v3/device/history?application_key=APPLICATION_KEY&api_key=API_KEY&mac=YOUR_MAC_CODE_OF_DEVICE&start_date=2022-01-01 00:00:00&end_date=2022-01-01 23:59:59&cycle_type=auto&call_back=outdoor,indoor.humidity

