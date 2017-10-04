"""QUERY SERVICE"""

import logging
from requests import Request, Session


class RasdamanService(object):

    @staticmethod
    def get_rasdaman_coverages():
        logging.info('[RasdamanService] Getting Rasdaman Coverages')
        headers = {'Content-Type': 'application/xml'}
        payload = {
            'SERVICE': 'WCS',
            'ACCEPTVERSIONS': '2.0',
            'REQUEST': 'GetCapabilities'
        }

        request = Request(
            method='GET',
            url='http://localhost:8080/rasdaman/ows',
            headers=headers,
            params=payload
        )

        session = Session()
        prepped = session.prepare_request(request)
        response = session.send(prepped)
        return response.text