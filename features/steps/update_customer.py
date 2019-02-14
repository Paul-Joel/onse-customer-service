from behave import when


@when('I update customer "{id}" to "{name}"')
def update_customer(context, id, name):
    (first_name, surname) = name.split(' ', 2)
    response = context.web_client.post(
        '/customers/' + id,
        json={'firstName': first_name, 'surname': surname})

    assert response.status_code == 200, response.status_code
    json = response.get_json()
    if "customerId" in json:
        context.customer_id = json['customerId']
