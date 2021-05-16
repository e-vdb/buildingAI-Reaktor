# Exercise 8: Fishing in the Nordics

# intermediate level

def mainInt():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    fishers_country=[100*i/total_fishers for i in fishers]

    for country, fishers_country in zip(countries, fishers_country):
        print("%s %.2f%%" % (country, fishers_country)) 

mainInt()


# advance level

countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 
total_male_fishers = sum(male_fishers)
total_female_fishers = sum(female_fishers)

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
        total_fishers=total_female_fishers 
       
    else:
        fishers = male_fishers
        total_fishers=total_male_fishers
        
    fishers_country=[100*i/total_fishers for i in fishers]
    
    guess = None
    biggest = 0.0
    for country,fraction in zip(countries,fishers_country):
        if fraction>biggest:
            biggest=fraction
            guess=country
    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
