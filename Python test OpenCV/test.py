import pandas
#Reading csv file with pandas and giving name to each colunm
index= ["color","color_name","hex","R","G","B"]
csv = pandas.read_csv(r'C:\Users\DK0626\source\repos\PythonClusteringApplication1\PythonClusteringApplication1\colors.csv', names = index, header = None)
print(csv)