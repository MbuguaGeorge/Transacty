from django.db import models
from django.contrib.auth.models import AbstractUser
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.
class Code(models.Model):
    name = models.CharField(max_length=100)
    qr_code = models.ImageField(blank=True)
    url = models.URLField(max_length=100,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.url)
        canvas = Image.new('RGB',(290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Profile(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(('password'), max_length=128, help_text=("use'[algo]$[salt]$[hexdigest]'"))