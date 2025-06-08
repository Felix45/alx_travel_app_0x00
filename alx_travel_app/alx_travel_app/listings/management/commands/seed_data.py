from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from random import randint, choice
from faker import Faker

class Command(BaseCommand):
    help = 'Seed the database with initial data for listings, bookings, and reviews.'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Create Listings
        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=6),
                description=fake.text(max_nb_chars=200),
                price_per_night=round(randint(50, 500) + randint(0, 99) / 100, 2)
            )
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))

        # Create Bookings
        listings = Listing.objects.all()
        for _ in range(5):
            booking = Booking.objects.create(
                listing=choice(listings),
                user=fake.name(),
                total_price=round(randint(100, 1000) + randint(0, 99) / 100, 2),
                start_date=fake.date_between(start_date='-1y', end_date='today'),
                end_date=fake.date_between(start_date='today', end_date='+1y')
            )
            self.stdout.write(self.style.SUCCESS(f'Created booking for: {booking.listing.title} by {booking.user}'))

        # Create Reviews
        for _ in range(15):
            review = Review.objects.create(
                listing=choice(listings),
                user=fake.name(),
                rating=randint(1, 5),
                comment=fake.text(max_nb_chars=100)
            )
            self.stdout.write(self.style.SUCCESS(f'Created review for: {review.listing.title} by {review.user}'))