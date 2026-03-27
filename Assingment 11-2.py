import matplotlib.pyplot as plt
companies = ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "TCS", "Amdocs"]
recruitments = [120, 150, 170, 90, 110, 130, 200, 80]
plt.bar(companies, recruitments)
plt.title("Company Recruitment Data")
plt.xticks(rotation=45)
plt.show()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.title("Customized Pie Chart")
plt.show()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()
labels = ["IBM", "Amdocs"]
values = [90, 80]
plt.bar(labels, values)
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.show()