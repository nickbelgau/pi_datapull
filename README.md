# **PI Datapull**


## **Description**

This script pulls tags stored on a PI server over a specific interval, converts the timestamps from UTC to PST, and exports the timeseries data.


## **Using the File**

A connection to the requested PI server should be made in advance by the User.
This is handled outside of Python.
To install the module, identify van earlier version to avoid issues.
pip install PIconnect==0.7

To properly execute the code, the user should replace the dummy tags and server with actual tags and a PI server, formatted as strings.
Additional tags can be added to the tag list.

## **Future Improvements**

Tags can be imported via excel instead of specifying within the script such that the program can be more interactive with other programs.

## **Works Cited**

This script was made by referencing the PI Connect module documentation.

https://piconnect.readthedocs.io/en/develop/
