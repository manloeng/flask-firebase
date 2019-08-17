from faker import Faker
import json
fake = Faker('en_GB')

# will generate the same data
# fake.seed(4321)

# for loop of range x
# for _ in range(10):
#     print(fake.name())


# print(fake.password())
# print(fake.email())
# print(fake.image_url())

# print(fake.job())


# print(fake.company())
# print(fake.address())
# print(fake.company_email())

users = []
def usergenerator():
    for _ in range(10):
        first_name = fake.first_name()

        user = {
            'username': first_name + fake.building_number(),
            'name' : first_name + " " + fake.last_name(),
            'password' : fake.password(),
            'email': fake.email(),
            'avatar_url': fake.image_url()
        }
        users.append(user)


usergenerator()


with open('users.json', 'w') as json_file:
    json.dump(users, json_file)