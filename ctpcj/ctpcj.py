"""Starting point for discovering all information available
on the Cluj-Napoca Public Transportation website."""

import requests
import urllib.parse

from bs4 import BeautifulSoup


class Ctpcj:
    """Provides starting points for discovering all information
    available on the Cluj-Napoca Public Transportation website."""

    base_url = 'http://ctpcj.ro/'
    schedule_base_url = 'http://ctpcj.ro/orare/csv/'

    @classmethod
    def schedule(cls, line_number):
        """Gets the schedule for the specified line.

        Args:
            line_schedule (str):
                The number/name of the line to get
                the schedule for.

        Returns (dict):
            A dictionary containing the schedule for week
            days, saturday and sunday.
        """

        schedule_filenames = {
            'week': 'orar_{}_lv.csv'.format(line_number),
            'saturday': 'orar_{}_s.csv'.format(line_number),
            'sunday': 'orar_{}_d.csv'.format(line_number)
        }

        line_schedule = {}

        for name in schedule_filenames:
            line_schedule[name] = cls.__get_schedule(
                schedule_filenames[name]
            )

        return line_schedule

    @classmethod
    def __get_schedule(cls, filename):
        """Acquires the specified CSV schedule file from the
        CTPCJ server and parses it into a dictionary.

        Args:
            filename (str):
                The name of the CSV file to retrieve.

        Returns (dict):
            A dictionary containing the result of the parsed
            CSV file.
        """

        url = urllib.parse.urljoin(
            cls.schedule_base_url,
            filename
        )

        req = requests.get(url)
        if req.status_code == 404:
            return None

        csv_file = req.text
        file_lines = csv_file.split('\n')

        info_lines = file_lines[:5]
        schedule_lines = file_lines[5:]

        route_name = info_lines[0].split(',')[1]
        date = info_lines[2].split(',')[1]
        in_stop = info_lines[3].split(',')[1]
        out_stop = info_lines[4].split(',')[1]

        schedule = {
            'name': route_name,
            'date': date,
            'in_stop': in_stop,
            'out_stop': out_stop,
            'in': [],
            'out': []
        }

        for time_entry in schedule_lines:
            if ',' not in time_entry:
                continue

            times = time_entry.split(',')

            schedule['in'].append(times[0])
            schedule['out'].append(times[1])

        return schedule

    @classmethod
    def urban_lines(cls):
        """Gets all urban lines.

        Returns (dict):
            An array of dictionaries of all urban lines.
        """

        return cls.__collect_lines(
            'urban',
            '/index.php/en/timetables/urban-lines'
        )

    @classmethod
    def metropolitan_lines(cls):
        """Gets all metropolitan lines.

        Returns (dict):
            An array of dictionaries of all metropolitan lines.
        """

        return cls.__collect_lines(
            'metropolis',
            '/index.php/en/timetables/metropolitan-lines'
        )

    @classmethod
    def all_lines(cls):
        """Gets all available lines (urban, metropolitan).

        Returns (dict):
            An array of dictionaries of all available lines.
        """

        lines = cls.urban_lines() + cls.metropolitan_lines()
        return lines

    @classmethod
    def __collect_lines(cls, area, line_url):
        """Collects all available lines into a dictionary from
        the specified URL (on the CTPCJ website).

        Args:
            area (str):
                A string describing the page/area the lines are
                being collected from. This will be embedded in
                each line's dictionary.

            line_url (str):
                The relative CTPCJ website URL to collect the
                lines from.

        Returns (dict):
            A dictionary containing all the collected lines.
        """

        lines = []

        url = urllib.parse.urljoin(
            cls.base_url,
            line_url
        )

        soup = BeautifulSoup(
            requests.get(url).text.encode('utf-8'),
            'html.parser'
        )

        line_elements = soup.find_all('div', class_='element')

        for element in line_elements:
            # Extract the route (start and end station).. These
            # are contained in a single string separated by a dash
            # surrounded by spaces
            route_text = element.find(class_='ruta').text
            route = route_text.split(' - ')
            if len(route) < 2:

                # Hack in case of bad formatting
                route = route_text.split('- ')
                if len(route) < 2:
                    route = route_text.split('-')
                    if len(route) < 2:
                        continue

            # Extract the line number and the URL to the page
            # that contains more detailed information about the line
            link = element.find('a')
            number = link.text.replace('Line ', '').strip()
            url = urllib.parse.urljoin(cls.base_url, link.get('href'))

            # Determine the line type by checking for
            # specific CSS classes

            element_class = element.get('class')
            line_type = 'trolley'

            if 'buses' in element_class:
                line_type = 'bus'
            elif 'minibuses' in element_class:
                line_type = 'mini-bus'
            elif 'trams' in element_class:
                line_type = 'tram'

            # Build the object that contains all the information
            # about the line
            line = {
                'line': number,
                'url': url,
                'type': line_type,
                'area': area,
                'route': {
                    'start': route[0],
                    'end': route[1]
                }
            }

            lines.append(line)

        return lines
