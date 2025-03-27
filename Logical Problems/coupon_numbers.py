import random

class Coupons:
    @staticmethod
    def generate_random(n):
        """
        Generates a random number between 0 and N

        Parameters :
        n: an integer denoting the number of coupons

        Returns:
        A random number between 0 to N
        """
        return random.randint(0,n-1)
    
    @staticmethod
    def process_coupon(n):
        """
        Gives the numbers of times it would take to randomly generate N coupons

        Parameters:
        n: an integer denoting the number of coupons

        Returns:
        The number of times it would take to generate all coupon numbers
        """       
        coupons_found = set()
        total_random_numbers = 0
        while len(coupons_found)<n:
            coupons_found.add(Coupons.generate_random(n))
            total_random_numbers += 1

        return total_random_numbers
    
no_of_coupons = int(input())
print(Coupons.process_coupon(no_of_coupons))
        
