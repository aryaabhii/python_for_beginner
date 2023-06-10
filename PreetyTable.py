from prettytable import PrettyTable
var = PrettyTable()

var.field_names = ["Roll no.", "Name", "Marks", "class"]
var.add_rows(
    [
        [1, "Abhijeet Kumar", 280, "BCA"],
        [2, "Abhishek Kumar", 380, "BBM"],
        [3, "Sneha Kumari", 400, "Bsc.it"],
        [4, "Somya Kumari", 380, "B.com"],
        [5, "Zoya Khan", 380, "Inter"]
    ]
)

print (var)
