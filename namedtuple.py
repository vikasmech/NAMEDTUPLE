from collections import namedtuple
from faker import Faker
import datetime
from time import perf_counter
from functools import wraps
import random





#print(fake.blood)

# Use the Faker library to get 10000 random profiles. Using namedtuple, 
# calculate the largest blood type, 
# mean-current_location, oldest_person_age, and average age 
# (add proper doc-strings). 

#import faker from Faker
def timed(fn: "Function"):
    """
    Decorator to calculate run time of a function.
    """
    @wraps(fn)
    def inner(*args, **kwargs) -> "Function Output":
        """
        Inner function to calculate the time.
        """
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        time_elapsed = (end - start)
        print('Run time: {0:.6f}s'.format(time_elapsed))
        return result
    return inner

fake = Faker()
@timed
def fake_profile_generator(n:int):
    """
    to create the fake profile using faker using namedtuple
    """
    Faker.seed(21)
    
    profiles = []
    profile = namedtuple("profile",fake.profile().keys())
    for _ in range(n):
        profiles.append(profile(**fake.profile()))
    return profiles

@timed
def generate_profiles_using_dictionary(n: int):
    """
    To create a fake profiles of given number of people using dictornary
    """
    Faker.seed(21)
    profiles = []
    for _ in range(n):
        profiles.append(fake.profile())
    return profiles

@timed
def calculate_from_namedtuple(profiles):
    """
    given a list of profiles calculate 
    """
    num_profiles = len(profiles)
    date_today = datetime.date.today()
    blood_gp = dict()
    max_age = {'age': 0, 'profile': None}
    cur_loc_coord_sum = [0, 0]
    sum_ages = 0
    for profile in profiles:
        blood_gp[profile.blood_group] = blood_gp.get(profile.blood_group,0) + 1
        age = int((date_today - profile.birthdate).days/365)
        if  age > max_age['age']:
            max_age['age'] = age
            max_age['profile'] = profile
        cur_loc_coord_sum[0] += profile.current_location[0]
        cur_loc_coord_sum[1] += profile.current_location[1]
        sum_ages += age
    max_bg = max(blood_gp,key=blood_gp.get)
    average_age = sum_ages/num_profiles
    cur_loc_coord_sum[0] /= num_profiles
    cur_loc_coord_sum[1] /= num_profiles
    return max_bg,cur_loc_coord_sum,max_age['age'],average_age 

@timed
def calculate_from_dictonary(profiles):
    """
    given a list of profiles calculate 
    """
    num_profiles = len(profiles)
    date_today = datetime.date.today()
    blood_gp = dict()
    max_age = {'age': 0, 'profile': None}
    cur_loc_coord_sum = [0, 0]
    sum_ages = 0
    for profile in profiles:
        bg = profile["blood_group"]
        blood_gp[bg] = blood_gp.get(bg,0) + 1
        age = int((date_today - profile["birthdate"]).days/365)
        if  age > max_age['age']:
            max_age['age'] = age
            max_age['profile'] = profile
        cur_loc_coord_sum[0] += profile["current_location"][0]
        cur_loc_coord_sum[1] += profile["current_location"][1]
        sum_ages += age
    max_bg = max(blood_gp,key=blood_gp.get)
    average_age = sum_ages/num_profiles
    cur_loc_coord_sum[0] /= num_profiles
    cur_loc_coord_sum[1] /= num_profiles
    return max_bg,cur_loc_coord_sum,max_age['age'],average_age 

#profiles = fake_profile_generator(10000)
#print(calculate_from_namedtuple(profiles))
#print(generate_profiles_using_dictionary(1))
#profiles = generate_profiles_using_dictionary(10000)
#print(calculate_from_dictonary(profiles))


def company_data_gen(n=100):
    """Create fake data (you can use Faker for company names) for imaginary stock 
    exchange for top 100 companies (name, symbol, open, high, close). 
    Assign a random weight to all the companies.
    """
    all_companies = []
    Stocks = namedtuple("Stocks", 'name symbol open high close company_weight')
    for _ in range(n):
        name = fake.company()
        open_ = round(random.uniform(0, 5000), 2)
        high_num = round(random.uniform(0.6, 1.4), 2)  
        high = open_ * high_num if high_num > 1.0 else open_
        close = random.uniform(open_ - random.randint(-5, 5), high + random.randint(-8, 10))
        if close > high:
            high = close

        all_companies.append(
            Stocks(name=name, symbol=name[:3].upper(), open=open_, high=round(high, 2), close=round(close, 2), company_weight=round(random.normalvariate(.5,.1), 3)))
    return all_companies
    
def calculator(all_companies):
    """Calculates and show what value the stock market started at,
    what was the highest value during the day, 
    and where did it end. """
    stock_index_start = round(sum(x.open * x.company_weight for x in all_companies), 4)
    stock_index_end = round(sum(x.close * x.company_weight for x in all_companies), 4)
    stock_index_high = round(sum(x.high * x.company_weight for x in all_companies), 4)
    return stock_index_start,stock_index_high,stock_index_end

all_companies = company_data_gen(n=100)
print(calculator(all_companies))