import csv


def get_requests_count(order, maria_orders):
    product = order[1]
    if product not in maria_orders:
        maria_orders[product] = 1
    else:
        maria_orders[product] += 1


def file_writer(items_to_write):
    with open("data/mkt_campaign.txt", mode="w") as mkt_campaign:
        for item in items_to_write:
            print(item, file=mkt_campaign)


def data_separator(
    order, maria_orders, arnaldo_orders,
    joao_dish_orders, joao_day_orders
):
    if order[0] == "maria":
        get_requests_count(order, maria_orders)
    if order[0] == "arnaldo":
        get_requests_count(order, arnaldo_orders)
    if order[0] == "joao":
        joao_dish_orders.add(order[1])
        joao_day_orders.add(order[2])


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        maria_orders = {}
        arnaldo_orders = {}
        joao_dish_orders = set()
        joao_day_orders = set()
        dish_list = set()
        days_list = set()

        with open(path_to_file, encoding="utf-8", mode="r") as file:
            data = csv.reader(file)
            for order in data:
                dish_list.add(order[1])
                days_list.add(order[2])
                data_separator(
                    order, maria_orders, arnaldo_orders,
                    joao_dish_orders, joao_day_orders)

        maria_most_ordered_dish = max(maria_orders, key=maria_orders.get)
        arnaldo_qty_orders = arnaldo_orders["hamburguer"]
        joao_never_ordered_dish = dish_list.difference(joao_dish_orders)
        joao_never_ordered_day = days_list.difference(joao_day_orders)

        file_writer([
            maria_most_ordered_dish, arnaldo_qty_orders,
            joao_never_ordered_dish, joao_never_ordered_day,
        ])
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

# source: (get max value)
# https://pythonguides.com/python-find-max-value-in-a-dictionary/#:~:text=By%20using%20max()%20and%20dict.,maximum%20value%20in%20a%20dictionary.&text=To%20obtain%20the%20maximum%20value,paired%20with%20the%20maximum%20value.
