try:
    import requests
    from bs4 import BeautifulSoup

    doctors_link = []
    full_link = []

    for i in range(1,253):
        a = 'https://www.healthgrades.com/find-a-doctor/a-z/a-' + f'{i}'
        results = requests.get(a)

        src = results.content

        soup = BeautifulSoup(src, features='lxml')

        linkss = soup.find_all('li', class_='link-column__list')


        for link in linkss:
            a_tag = link.find('a').attrs['href']
            doctors_link.append(a_tag)



        for doctor in doctors_link:
            a = 'https://www.healthgrades.com' + doctor
            full_link.append(a)

    doctors_name = []
    doctors_speciality = []
    doctors_contact = []
    doctors_address = []

    for link in full_link:
        results = requests.get(link)

        src = results.content

        soup = BeautifulSoup(src, features='lxml')

        target_name = soup.find('h1')
        target_address = soup.find('address', class_='address')
        target_contact = soup.find_all('a', class_="hg-track insurance-phone highlight-link")

        try:
            doctor_name = target_name.text
        except:
            doctor_name = None
        try:
            doctor_address = target_address.text
        except:
            doctor_address = None
        try:
            doctor_contact = target_contact[0].text
        except:
            doctor_contact = None
        doctor_speciality = link.split('com/')[1].split('/')[0]

        doctors_name.append(doctor_name)
        doctors_speciality.append(doctor_speciality)
        doctors_contact.append(doctor_contact)
        doctors_address.append(doctor_address)


    import pandas as pd

    data = {'name':doctors_name,'speciality':doctors_speciality,'contact':doctors_contact,'address':doctors_address}

    df = pd.DataFrame.from_dict(data)
    with open('data.csv', 'w') as f:
        df.to_csv(f)

    print('done')

except:
    print('try again')
