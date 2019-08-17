from faker import Faker
import json
fake = Faker('en_GB')

# will generate the same data
fake.seed(4321)

users = []
businesses = []
jobPosition = []
locations = []

def usergenerator():
    for _ in range(10):
        first_name = fake.first_name()

        user = {
            'username': first_name + fake.building_number(),
            'name' : first_name + " " + fake.last_name(),
            # 'password' : fake.password(),
            'email': fake.email(),
            'avatar_url': fake.image_url()
        }
        users.append(user)


def businessgenerator():
    for _ in range(10):

        business = {
            "businessName":  fake.company(),
            "businessAddress": fake.address(),
            "businessEmail": fake.company_email(),
        }
        businesses.append(business)


def jobgenerator():
    for _ in range(5):
        job = {
            'jobTitle': fake.job()
        }
        jobPosition.append(job)


def locationgenerator():
    for _ in range(5):
        location = {
            'location': fake.city()
        }
        locations.append(location)


usergenerator()
businessgenerator()
jobgenerator()
locationgenerator()

with open('users.json', 'w') as json_file:
    json.dump(users, json_file)


with open('business.json', 'w') as json_file:
    json.dump(businesses, json_file)


with open('jobPosition.json', 'w') as json_file:
    json.dump(jobPosition, json_file)


with open('locations.json', 'w') as json_file:
    json.dump(locations, json_file)