import pytest
import requests
from os import environ
from my_decorators import error_generator
from mock import mock_get_dogecoing

import responses
from pytest_schema import schema

companies_url = "http://127.0.0.1:8000/companies/"
coinapi = "https://rest.coinapi.io/v1/assets/DOGE"


@pytest.mark.skip_in_ci
def test_zero_companies_server_agnostic() -> None:
    response = requests.get(companies_url)
    assert response.status_code == 200
    assert response.text == "[]"


@pytest.mark.skip_in_ci
def test_create_company_with_layoff_status_should_succeed() -> None:
    response = requests.post(
        url=companies_url, json={"name": "test_company_layoffs", "status": "Layoffs"}
    )
    assert response.status_code == 201
    response_content = response.json()
    assert response_content["name"] == "test_company_layoffs"
    assert response_content["status"] == "Layoffs"
    assert response_content["application_link"] == ""
    assert response_content["notes"] == ""

    cleanup_company(str(response_content["id"]))


def cleanup_company(company_id: str) -> None:
    response = requests.delete(url=companies_url + company_id)
    assert response.status_code == 204


@pytest.mark.crypto
def test_get_dogecoin_returns_valid_schema() -> None:
    response = requests.get(
        url=coinapi, headers={"X-CoinAPI-Key": environ["COINAPI_KEY"]}
    )
    expected_schema = [
        {
            "asset_id": "DOGE",
            "name": "DogeCoin",
            "type_is_crypto": int,
            "data_quote_start": str,
            "data_quote_end": str,
            "data_orderbook_start": str,
            "data_orderbook_end": str,
            "data_trade_start": str,
            "data_trade_end": str,
            "data_symbols_count": int,
            "volume_1hrs_usd": float,
            "volume_1day_usd": float,
            "volume_1mth_usd": float,
            "price_usd": float,
            "id_icon": str,
            "data_start": str,
            "data_end": str,
        }
    ]
    assert response.status_code == 200, error_generator(
        "status_code", "200", str(response.status_code)
    )
    assert schema(expected_schema) == response.json()


@responses.activate
@pytest.mark.crypto
def test_get_mocked_dogecoin() -> None:
    mock_get_dogecoing(url=coinapi)
    actual_response = requests.get(url=coinapi)
    expected_response = [
        {
            "asset_id": "EDEN",
            "name": "EDEN-1",
            "type_is_crypto": 1,
            "data_quote_start": "2014-07-31T13:05:46.0000000Z",
            "data_quote_end": "2022-03-12T09:41:55.4610000Z",
            "data_orderbook_start": "2014-07-31T13:05:46.0000000Z",
            "data_orderbook_end": "2020-08-05T14:37:58.7197513Z",
            "data_trade_start": "2014-02-21T05:16:16.8330000Z",
            "data_trade_end": "2022-03-12T09:43:13.8730000Z",
            "data_symbols_count": 5284,
            "volume_1hrs_usd": 17193631.49,
            "volume_1day_usd": 9749407400854.86,
            "volume_1mth_usd": 35093965394285.28,
            "price_usd": 0.1165589471122932890589136338,
            "id_icon": "63e240f3-047f-41c7-9179-6784bc719f63",
            "data_start": "2014-02-21",
            "data_end": "2022-03-12",
        }
    ]
    assert actual_response.status_code == 200, error_generator(
        "status_code", "200", str(actual_response.status_code)
    )
    assert expected_response == actual_response.json()
