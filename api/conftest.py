from typing import Callable, List

import pytest

from api.coronavstech.companies.models import Company


@pytest.fixture()
def create_company(**kwargs) -> Callable:
    def _company_factory(**kwargs):
        company_name = kwargs.pop("name", "Test Company INC")
        return Company.objects.create(name=company_name)

    return _company_factory


@pytest.fixture()
def create_several_companies(request, create_company) -> List:
    companies = []
    names = request.param
    for name in names:
        companies.append(create_company(name=name))
    return companies


@pytest.fixture()
def amazon() -> Company:
    return Company.objects.create(name="Amazon")
