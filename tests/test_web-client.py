from datetime import datetime
from some_web_client import SomeResourceClient
import responses


@responses.activate
def test_web_client():
    valid_json_answer = {
        "lastActionTime": 1681129612,
        "timeDiff": 2934
    }
    responses.add(method=responses.GET,
                  url='https://www.avito.ru/web/2/user/get-status/43e99f0389907ec95262e6f7e929c70e6b6848a45f77ae7d8a3971bafdd4a79c',
                  json=valid_json_answer, status=200)
    some_resource_client = SomeResourceClient("https://www.avito.ru")
    res = some_resource_client.get_user_last_action_time(
        "43e99f0389907ec95262e6f7e929c70e6b6848a45f77ae7d8a3971bafdd4a79c")
    assert res == datetime.fromtimestamp(valid_json_answer["lastActionTime"] - valid_json_answer["timeDiff"])



