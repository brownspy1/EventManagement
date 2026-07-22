import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, time, timedelta
from event.models import Category, Event, Participant

class Command(BaseCommand):
    help = 'Seeds the database with 10 Categories, 10 Events, and 10 Participants.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Clearing existing Categories, Events, and Participants..."))
        # Clear data
        Participant.objects.all().delete()
        Event.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Database cleared. Starting seeding..."))

        # 1. Create 10 Categories
        category_data = [
            ("Tech & Programming", "Events focused on software development, coding, and technology trends."),
            ("Business & Startups", "Seminars and networking for entrepreneurs, startups, and business owners."),
            ("Design & Arts", "Workshops on UI/UX, graphic design, animation, and digital arts."),
            ("Health & Wellness", "Sessions on physical health, mental wellbeing, yoga, and meditation."),
            ("Music & Festivals", "Live concerts, music workshops, and cultural celebrations."),
            ("Sports & Fitness", "Athletic events, marathon training, and personal fitness workshops."),
            ("Science & Research", "Conferences showcasing cutting-edge scientific discoveries and research."),
            ("Marketing & Growth", "Digital marketing strategies, SEO, branding, and content creation."),
            ("Food & Culinary", "Cooking masterclasses, food tastings, and culinary history lectures."),
            ("Career & Networking", "Professional guidance, resume building, and industry networking events.")
        ]

        categories = []
        for name, desc in category_data:
            cat = Category.objects.create(name=name, description=desc)
            categories.append(cat)
            self.stdout.write(f"Created Category: {cat.name}")

        # 2. Create 10 Events
        event_locations = [
            "Silicon Valley Hall, San Jose",
            "Metropolitan Plaza, New York",
            "Creative Hub, San Francisco",
            "Greenery Gardens, Austin",
            "Symphony Auditorium, Chicago",
            "Active Arena, Los Angeles",
            "National Laboratory, Boston",
            "Media Lab, Seattle",
            "Gourmet Kitchen Studio, Portland",
            "Grand Conference Center, Denver"
        ]

        events = []
        today = date.today()
        for i, cat in enumerate(categories):
            # Stagger events into the future
            event_date = today + timedelta(days=random.randint(5, 60))
            event_time = time(random.randint(9, 18), 0)
            
            event = Event.objects.create(
                name=f"Summit: {cat.name}",
                description=f"An exciting gathering focusing on the latest advancements and networking in {cat.name}.",
                date=event_date,
                time=event_time,
                location=event_locations[i],
                category=cat
            )
            events.append(event)
            self.stdout.write(f"Created Event: {event.name}")

        # 3. Create 10 Participants
        participant_names = [
            "Alex Mercer", "Emma Watson", "John Doe", "Sophia Patel", 
            "Michael Brown", "Olivia Smith", "David Miller", "Isabella Jones", 
            "Daniel Garcia", "Mia Martinez"
        ]

        for name in participant_names:
            first_name = name.split()[0].lower()
            email = f"{first_name}@example.com"
            
            # Keep trying until we have a unique email (just in case)
            suffix = 1
            while Participant.objects.filter(email=email).exists():
                email = f"{first_name}{suffix}@example.com"
                suffix += 1

            participant = Participant.objects.create(name=name, email=email)
            
            # Register for 1 to 3 random events
            registered = random.sample(events, k=random.randint(1, 3))
            participant.registered_events.set(registered)
            participant.save()

            event_names = ", ".join([e.name for e in registered])
            self.stdout.write(f"Created Participant: {participant.name} ({participant.email}) registered for: {event_names}")

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
