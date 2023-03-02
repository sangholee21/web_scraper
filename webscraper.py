from wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")
file = open(f"{keyword}.csv", "w")

file.write("Position,Company,Location,URL\n")

file.close()

wwr = extract_wwr_jobs(keyword)

for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
  print(job)
  print("/////")
