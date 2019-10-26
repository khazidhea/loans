from datetime import date
import json


def test_day(client, mocker):
    datetime = mocker.patch('loans.views.datetime')
    datetime.today.return_value = date(2019, 10, 20)
    response = client.get('/api/day/')
    expected = json.dumps({'today': 'Sun'})
    assert response.content.decode() == expected
