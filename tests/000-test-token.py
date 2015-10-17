import t

from BaruwaAPI.exceptions import BaruwaAPIError


@t.ApiRequest('xxxx')
def test_auth_token(api):
    t.raises(BaruwaAPIError, api.get_users)
