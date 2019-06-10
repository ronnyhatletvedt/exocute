# Create your models here.
import datetime
from django.db import models

class WeightClass(models.Model):
    weight_class = models.CharField(max_length=6, primary_key=True)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.weight_class_text

class NasdaqIndex(models.Model):
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE)
    week = models.CharField(max_length=8)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    distribution = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    standard_deviation = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.week + ' | ' + self.weight_class + ' | ' + self.price

class NasdaqAverage(models.Model):
    week = models.CharField(max_length=8)
    price_average = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    volume = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.week + ' | ' + self.price_average + ' | ' + self.volume

class Country(models.Model):
    iso_country = models.CharField(max_length=3, primary_key=True)
    country = models.CharField(max_length=50, null=True, blank=True, default=None, help_text="The official name of the country.")
    continent_id = models.CharField(max_length=10, null=True, blank=True, default=None, help_text="A unique id for the continent.")
    north = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True, default=None, help_text="The northern latitide of the country.")
    south = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True, default=None, help_text="The southern latitide of the country.")
    west = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True, default=None, help_text="The western longitude of the country.")
    east = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True, default=None, help_text="The eastern longitude of the country.")
    class_1 = models.IntegerField(null=True, blank=True, default=None, help_text="First internal classification.")
    class_2 = models.IntegerField(null=True, blank=True, default=None, help_text="Second internal classification.")
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.iso_country + ' | ' + self.country

class Airport(models.Model):
    iata_code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True, default=None, help_text="Official name of the airport")
    type = models.CharField(max_length=50, null=True, blank=True, default=None, help_text="Official type (size) of airport.")
    iso_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, default=None, help_text="Official country code of the airport.")
    iso_region = models.CharField(max_length=50, null=True, blank=True, default=None, help_text="Official region code of the airport.")
    municipality = models.CharField(max_length=50, null=True, blank=True, default=None, help_text="The municipality the airport is located in.")
    latitude_deg = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True, default=None)
    longitude_deg = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True, default=None)
    class_1 = models.IntegerField(null=True, blank=True, default=None, help_text="First internal classification.")
    class_2 = models.IntegerField(null=True, blank=True, default=None, help_text="Second internal classification.")
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.iata_code

class Customer(models.Model):
    customer_id = models.CharField(max_length=4, primary_key=True)
    name_short = models.CharField(max_length=100, null=True, blank=True, default=None, help_text="The day to day name of the customer.")
    name_official = models.CharField(max_length=100, null=True, blank=True, default=None, help_text="The official name of the customer.")
    iso_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, default=None, help_text="Official country code of the airport.")
    class_1 = models.IntegerField(null=True, blank=True, default=None, help_text="First internal classification.")
    class_2 = models.IntegerField(null=True, blank=True, default=None, help_text="Second internal classification.")
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.iata_code + ' | ' + self.name

class CustomerDestination(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, default=None)
    shipment_address = models.CharField(max_length=255, null=True, blank=True, default=None, help_text="Official name of the airport")
    invoice_address = models.CharField(max_length=255, null=True, blank=True, default=None, help_text="Official name of the airport")
    latitude_deg = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True, default=None)
    longitude_deg = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.customer_id + ' | ' + self.shipment_address

class CustomerDestinationAirport(models.Model):
    customer_destination_id = models.ForeignKey(CustomerDestination, on_delete=models.CASCADE, null=True, blank=True, default=None)
    destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, blank=True, default=None)
    distance = models.IntegerField(null=True, blank=True, default=None, help_text="Driving distance in km to shipment address.")
    rank_1 = models.IntegerField(null=True, blank=True, default=None, help_text="Ranked on convenience.")
    rank_2 = models.IntegerField(null=True, blank=True, default=None, help_text="Ranked on availability.")
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.customer_id + ' | ' + self.shipment_address

class BaseOrder(models.Model):
    customer_destination_id = models.ForeignKey(CustomerDestination, on_delete=models.CASCADE, null=True, blank=True, default=None)
    base_order_date = models.DateField(null=True, blank=True, default=None, help_text="The date the base order was established (or last revised).")
    target_period = models.CharField(max_length=50, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.customer_id + ' | ' + self.base_order_date

class BaseOrderLine(models.Model):
    base_order_id = models.ForeignKey(BaseOrder, on_delete=models.CASCADE, null=True, blank=True, default=None)
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE, null=True, blank=True, default=None)
    weekday = models.CharField(max_length=10, null=True, blank=True, default=None)
    volume = models.IntegerField(null=True, blank=True, default=None, help_text="The base order volume (in boxes) for the given `weight_class`.")
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.base_order_id + ' | ' + self.weight_class + ' | ' + self.weekday + ' | ' + self.volume

class Order(models.Model):
    customer_destination_id = models.ForeignKey(CustomerDestination, on_delete=models.CASCADE, null=True, blank=True, default=None)
    order_date = models.DateField(null=True, blank=True, default=None, help_text="The date the order was established (or last revised).")
    target_week = models.CharField(max_length=50, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.customer_id + ' | ' + self.order_date

class CustomerShipment(models.Model):
    awb = models.CharField(max_length=12, null=True, blank=True, default=None)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, default=None)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, blank=True, default=None)
    estimated_departure = models.DateField(null=True, blank=True, default=None)
    target_arrival = models.DateField(null=True, blank=True, default=None)
    estimated_arrival = models.DateField(null=True, blank=True, default=None)
    actual_arrival = models.DateField(null=True, blank=True, default=None)
    created = models.DateTimeField('created', default=datetime.datetime.now)
    updated = models.DateTimeField('updated', default=datetime.datetime.now)
    def __str__(self):
        return self.awb + ' | ' + self.order_id

class CustomerShipmentLine(models.Model):
    customer_shipment_id = models.ForeignKey(CustomerShipment, on_delete=models.CASCADE, null=True, blank=True, default=None)
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE, null=True, blank=True, default=None)
    volume = models.IntegerField(null=True, blank=True, default=None, help_text="The order line volume (in boxes) for the given `weight_class`.")
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.base_order_id + ' | ' + self.weight_class + ' | ' + self.weekday + ' | ' + self.volume

class Quote(models.Model):
    customer_destination_id = models.ForeignKey(CustomerDestination, on_delete=models.CASCADE, null=True, blank=True, default=None)
    target_week = models.CharField(max_length=10, null=True, blank=True, default=None)
    tatus = models.CharField(max_length=12, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.customer_destination_id + ' | ' + self.target_week

class QuoteDuration(models.Model):
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True, default=None)
    duration = models.IntegerField(null=True, blank=True, default=None, help_text="The timespan the quote is valid.")
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.quote_id + ' | ' + self.duration + ' | ' + self.updated

class PriceQuoteLine(models.Model):
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True, default=None)
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    class_1 = models.IntegerField(null=True, blank=True, default=None, help_text="Quote or counteroffer (ask).")
    status = models.IntegerField(null=True, blank=True, default=None, help_text="Internal grading until closed.")
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.quote_id + ' | ' + self.weight_class + ' | ' + self.price + ' | ' + self.updated

class VolumePipeLine(models.Model):
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True, default=None)
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE)
    volume = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    class_1 = models.IntegerField(null=True, blank=True, default=None, help_text="Quote or counteroffer (ask).")
    status = models.IntegerField(null=True, blank=True, default=None, help_text="Internal grading until closed.")
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.quote_id + ' | ' + self.weight_class + ' | ' + self.price + ' | ' + self.updated

class WeekPriceTarget(models.Model):
    week = models.CharField(max_length=10, null=True, blank=True, default=None)
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.week + ' | ' + self.weight_class + ' | ' + self.price + ' | ' + self.updated

class WeekCostTarget(models.Model):
    week = models.CharField(max_length=10, null=True, blank=True, default=None)
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.week + ' | ' + self.weight_class + ' | ' + self.price + ' | ' + self.updated

class DestinationPriceTarget(models.Model):
    destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, blank=True, default=None)
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE)
    price_relative = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.week + ' | ' + self.weight_class + ' | ' + self.price + ' | ' + self.updated

class CustomerPriceTarget(models.Model):
    customer_destination_id = models.ForeignKey(CustomerDestination, on_delete=models.CASCADE, null=True, blank=True, default=None)
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE)
    price_relative = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.week + ' | ' + self.weight_class + ' | ' + self.price + ' | ' + self.updated

class DestinationCost(models.Model):
    destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, blank=True, default=None)
    cost = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=None)
    created = models.DateTimeField('created',  default=datetime.datetime.now)
    updated = models.DateTimeField('updated',  default=datetime.datetime.now)
    def __str__(self):
        return self.week + ' | ' + self.weight_class + ' | ' + self.price + ' | ' + self.updated