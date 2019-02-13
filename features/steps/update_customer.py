from behave import when, then, given

from customer_service.model.customer import Customer


@when('I update customer "{id}" to "{name}"')
def update_customer(context, id, name):
    (first_name, surname) = name.split(' ', 2)
    response = context.web_client.post(
        '/customers/' + id,
        json={'firstName': first_name, 'surname': surname})

    assert response.status_code == 201, response.status_code
    context.customer_id = response.get_json()['customerId']

