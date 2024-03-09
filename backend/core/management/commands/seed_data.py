from django.core.management.base import BaseCommand
from core.models import SmallingoVideo

class Command(BaseCommand):
    help = 'Seed initial data'

    def handle(self, *args, **kwargs):
        if not SmallingoVideo.objects.exists():
            SmallingoVideo.objects.create(url="https://firebasestorage.googleapis.com/v0/b/testlingo-e48de.appspot.com/o/videolingo.mp4?alt=media&token=28e6cb7d-7906-4fff-8a41-c49191c1074a")
            SmallingoVideo.objects.create(url="https://www.uio.no/english/research/strategic-research-areas/life-science/research/convergence-environments/abino/videos/5_performance.avi")
            SmallingoVideo.objects.create(url="https://raw.githubusercontent.com/VeiZhang/Test/master/video/ac3.mkv")
            self.stdout.write(self.style.SUCCESS('Seed data created successfully'))
        else:
            self.stdout.write(self.style.NOTICE('Seed data already exists'))
