from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,
        on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username
    
    def calculate_total(self):
        """Recalculate total based on related order items."""

        if not self.pk:
            return 0

        self.total = sum(item.price * item.quantity for item in self.item_set.all())
        return self.total
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)

        self.calculate_total()
        return super().save(*args, **kwargs)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,
        on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name
    
    def save(self, *args, **kwargs):
        """Save the item first, then update the order total."""
        super().save(*args, **kwargs)
        self.order.refresh_from_db()  # Ensure latest state
        self.order.save()

    def delete(self, *args, **kwargs):
        """Delete the item, then update the order total."""
        order = self.order
        super().delete(*args, **kwargs)
        order.refresh_from_db()  # Ensure latest state
        order.save()
