class TrackOrders:
    def __init__(self):
        self._orders = []

    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        self._orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        dish = dict()
        for order in self._orders:
            if order[0] == customer:
                if order[1] not in dish:
                    dish[order[1]] = 1
                else:
                    dish[order[1]] += 1
        most_ordered_dish = max(dish, key=dish.get)
        return most_ordered_dish

    def get_never_ordered_per_customer(self, customer):
        dish_list = set()
        dish_ordered = set()
        for order in self._orders:
            dish_list.add(order[1])
            if order[0] == customer:
                dish_ordered.add(order[1])
        return dish_list.difference(dish_ordered)

    def get_days_never_visited_per_customer(self, customer):
        days_list = set()
        days_ordered = set()
        for order in self._orders:
            days_list.add(order[2])
            if order[0] == customer:
                days_ordered.add(order[2])
        return days_list.difference(days_ordered)

    def get_busiest_day(self):
        counted_days_list = dict()
        for order in self._orders:
            if order[2] not in counted_days_list:
                counted_days_list[order[2]] = 1
            else:
                counted_days_list[order[2]] += 1
        busiest_day = max(counted_days_list, key=counted_days_list.get)
        return busiest_day

    def get_least_busy_day(self):
        counted_days_list = dict()
        for order in self._orders:
            if order[2] not in counted_days_list:
                counted_days_list[order[2]] = 1
            else:
                counted_days_list[order[2]] += 1
        least_busy_day = min(counted_days_list, key=counted_days_list.get)
        return least_busy_day
