class DailyData:
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def show_data(self):
        for index, value in enumerate(self.values):
            print(index, value)

    def __del__(self):
        print("DailyData object has ended")


data = DailyData([10, 25, 30, 45, 50])
data.show_data()