from typing import Callable, List

import pytest
import json
from django.urls import reverse
from api.coronavstech.companies.models import Company

companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db

# ----------------Test Get Companies------------------------------


def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_company_exists_should_succeed(client, amazon) -> None:
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == amazon.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""
    amazon.delete()


# ----------------Test Post Companies------------------------------


def test_create_company_without_arguments_should_fail(client) -> None:
    response = client.post(path=companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_existing_company_should_fail(client) -> None:
    Company.objects.create(name="apple")
    response = client.post(path=companies_url, data={"name": "apple"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }


def test_create_company_with_only_name_all_fields_should_be_default(client) -> None:
    response = client.post(path=companies_url, data={"name": "test_company"})
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("name") == "test_company"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_layoff_status_should_succeed(client) -> None:
    response = client.post(
        path=companies_url, data={"name": "test_company_layoffs", "status": "Layoffs"}
    )
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("name") == "test_company_layoffs"
    assert response_content.get("status") == "Layoffs"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_wrong_status_should_fail(client) -> None:
    response = client.post(
        path=companies_url,
        data={"name": "test_company_wrong_status", "status": "wrongStatus"},
    )
    assert response.status_code == 400
    assert "wrongStatus" in str(response.content)
    assert "is not a valid choice" in str(response.content)


@pytest.mark.xfail
def test_should_be_ok_if_fails(self) -> None:
    self.assertEqual(1, 2)


@pytest.mark.skip
def test_should_be_skipped(self) -> None:
    pass


# ----------------Learn about fixtures------------------------------


@pytest.mark.parametrize(
    "create_several_companies",
    [["Tiktok", "Twitch", "Test Company INC"], ["Facebook", "Instagram"]],
    indirect=True,
    ids=["3 T companies", "Zuckerberg's companies"],
)
def test_multiple_companies_exist_should_succeed(
    client, create_several_companies
) -> None:
    company_names = set(map(lambda x: x.name, create_several_companies))
    response_companies = client.get(companies_url).json()
    assert len(company_names) == len(response_companies)
    response_company_names = set(
        map(lambda company: company.get("name"), response_companies)
    )
    assert company_names == response_company_names
