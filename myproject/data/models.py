from django.db import models

class City(models.Model):
	stateChoices = [
		('AL', 'Alabama'),
		('AK', 'Alaska'),
		('AZ', 'Arizona'),
		('AR', 'Arkansas'),
		('CA', 'California'),
		('CO', 'Colorado'),
		('CT', 'Connecticut'),
		('DE', 'Delaware'),
		('FL', 'Florida'),
		('GA', 'Georgia'),
		('HI', 'Hawaii'),
		('ID', 'Idaho'),
		('IL', 'Illinois'),
		('IN', 'Indiana'),
		('IA', 'Iowa'),
		('KS', 'Kansas'),
		('KY', 'Kentucky'),
		('LA', 'Louisiana'),
		('ME', 'Maine'),
		('MD', 'Maryland'),
		('MA', 'Massachusetts'),
		('MI', 'Michigan'),
		('MN', 'Minnesota'),
		('MS', 'Mississippi'),
		('MO', 'Missouri'),
		('MT', "Montana"),
		('NE', 'Nebraska'),
		('NV', 'Nevada'),
		('NH', 'New Hampshire'),
		('NJ', 'New Jersey'),
		('NM', 'New Mexico'),
		('NY', 'New York'),
		('NC', 'North Carolina'),
		('ND', 'North Dakota'),
		('OH', 'Ohio'),
		('OK', 'Oklahoma'),
		('OR', 'Oregon'),
		('PA', 'Pennsylvania'),
		('RI', 'Rhode Island'),
		('SC', 'South Carolina'),
		('SD', 'South Dakota'),
		('TN', 'Tennessee'),
		('TX', 'Texas'),
		('UT', 'Utah'),
		('VT', 'Vermont'),
		('VA', 'Virginia'),
		('WA', 'Washington'),
		('WV', 'West Virginia'),
		('WI', 'Wisconsin'),
		('WY', 'Wyoming')
					]
	name = models.CharField(max_length=30)
	state = models.CharField(max_length=15, choices=stateChoices)
	sensor_location = models.CharField(max_length=30, default="")
	wind_speed = models.IntegerField(default = 0)
	humidity = models.IntegerField(default = 0)
	temperature = models.IntegerField(default = 0)
	CO = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)
	SO2 = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)
	PM10 = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)
	NO2 = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)
	O3_8 = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)
	PM25 = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)
	wind_direction = models.CharField(max_length=3, default="N")
	time_created = models.DateTimeField(auto_now=True)



	def __str__(self):
		return self.name + ', ' + self.state

	class Meta:
		ordering = ('name',)

class Vehicle(models.Model):
	manufacturer = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	year = models.IntegerField(null=True)
	CO = models.DecimalField(max_digits=10, decimal_places=6)
	HC = models.DecimalField(max_digits=10, decimal_places=6)
	NO = models.DecimalField(max_digits=10, decimal_places=6)
	CO2 = models.DecimalField(max_digits=10, decimal_places=6)
	PM25 = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)

	city = models.ForeignKey(City, models.CASCADE, related_name='vehicles')
	time_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.year) + ' ' + self.manufacturer + ' ' + self.name

class Powerplant(models.Model):
	name = models.CharField(max_length=30)
	CO = models.DecimalField(max_digits=10, decimal_places=6)
	HC = models.DecimalField(max_digits=10, decimal_places=6)
	NO = models.DecimalField(max_digits=10, decimal_places=6)
	CO2 = models.DecimalField(max_digits=10, decimal_places=6)
	city = models.ForeignKey(City, models.CASCADE, related_name='powerplants')
	time_created = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name

