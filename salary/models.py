from django.db import models
from tms.utils import TimeStamps

from users.models import Driver

class Salary(TimeStamps):
    salary_for = models.CharField(max_length=200,null=True)
    salary_for_id = models.IntegerField(null=True)
    description = models.CharField(max_length=256)
    amount = models.DecimalField(decimal_places=0,max_digits=20)
    advancement = models.BooleanField(default=False)
    month = models.CharField(max_length=16)

    def __str__(self):
        return self.salary_for


    def salary_for_name(self):
        if str(self.salary_for).lower() == "driver":
            name = Driver.objects.get(id=self.salary_for_id)
            if name == None:
                return 'name';
            else:
                return name.name;

        else:
            return "Custom user"