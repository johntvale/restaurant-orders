import csv


def get_requests_count(order, maria_requests):
    product = order[1]
    if product not in maria_requests:
        maria_requests[product] = 1
    else:
        maria_requests[product] += 1


def food_difference(set_food, order):
    ordered_by_joao = set()
    if order[1] not in ordered_by_joao:
        ordered_by_joao.add(order[1])


def file_writer(items_to_write):
    with open("data/mkt_campaign.txt", mode="w") as mkt_campaign:
        for item in items_to_write:
            print(item, file=mkt_campaign)


def data_separator(
    order, maria_requests, arnaldo_requests,
    joao_food_requests, joao_day_requests
):
    if order[0] == "maria":
        get_requests_count(order, maria_requests)
    if order[0] == "arnaldo":
        get_requests_count(order, arnaldo_requests)
    if order[0] == "joao":
        joao_food_requests.add(order[1])
        joao_day_requests.add(order[2])


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        maria_requests = {}
        arnaldo_requests = {}
        joao_food_requests = set()
        joao_day_requests = set()
        food_list = set()
        days_list = set()

        with open(path_to_file, encoding="utf-8", mode="r") as file:
            data = csv.reader(file)
            for order in data:
                food_list.add(order[1])
                days_list.add(order[2])
                data_separator(
                    order, maria_requests, arnaldo_requests,
                    joao_food_requests, joao_day_requests)

        maria_most_requested_prod = max(maria_requests, key=maria_requests.get)
        arnaldo_qty_requested = arnaldo_requests["hamburguer"]
        joao_never_requested_prod = food_list.difference(joao_food_requests)
        joao_never_requested_day = days_list.difference(joao_day_requests)

        file_writer([
            maria_most_requested_prod, arnaldo_qty_requested,
            joao_never_requested_prod, joao_never_requested_day,
        ])
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

# source: (get max value)
# https://pythonguides.com/python-find-max-value-in-a-dictionary/#:~:text=By%20using%20max()%20and%20dict.,maximum%20value%20in%20a%20dictionary.&text=To%20obtain%20the%20maximum%20value,paired%20with%20the%20maximum%20value.
