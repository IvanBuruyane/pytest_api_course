import responses


def mock_get_dogecoing(url) -> None:
    responses.add(
        method=responses.GET,
        url=url,
        json=[
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
        ],
        status=200,
    )
