# CTPCJ API
CTPCJ (Public Transport Company S.A Cluj-Napoca) is Cluj-Napoca's public transportation company. It organizes all public transportation in the city and provides schedules online on their website (ctpcj.ro).

This Python packages provides both a Python library as well as a REST web server that give access to the schedules and a lot of information from the CTPCJ website programmatically.

## How does it work?
As said, CTPCJ does not provide an API. This package directly scrapes
all the data from their website, making it as a real time and up-to-date
as possible. It's slow at the moment as every request requires one or
more HTTP requests to the CTPCJ website and to process it. However, the plan is to add some caching to make sure 99% of the requests don't go through to the CTPCJ websites. They only update their websites a couple of times a month.

## Work in progress
This is a work in progress, but basic stuff already works. Features now:

* Get a list of all available transportation lines, including their start and end points.
* Get the schedule for a specific line.

Features planned:

* See available connections between lines
* Get the coordinates of a specific stops
* List and search through stops
* Include links to images/graphs of lines as displayed on the website
* Cache everything to speed up requests and reduce load on the CTPCJ website

## Code quality
The entire code base is fully PEP8 compliant and scores 10.00/10 on PyLint with the default configuration.
