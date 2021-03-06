from django.db import models


class Resume(models.Model):
    
    # Constants
    MAX_NAME_LEN  = 124
    MAX_ADDR_LEN  = 124
    MAX_CITY_LEN  = 32
    MAX_STATE_LEN = 16
    MAX_ZIP_LEN   = 16
    MAX_PHONE_LEN = 16
    MAX_EMAIL_LEN = 256

    # Fields
    first_name    = models.CharField(max_length=MAX_NAME_LEN)
    last_name     = models.CharField(max_length=MAX_NAME_LEN)
    address_line1 = models.CharField(max_length=MAX_ADDR_LEN)
    address_line2 = models.CharField(max_length=MAX_ADDR_LEN, blank=True)
    city          = models.CharField(max_length=MAX_CITY_LEN)
    state         = models.CharField(max_length=MAX_STATE_LEN)
    zip_code      = models.CharField(max_length=MAX_ZIP_LEN, blank=True)
    phone_number  = models.CharField(max_length=MAX_PHONE_LEN)
    email         = models.EmailField(max_length=MAX_EMAIL_LEN)
    create_datetime        = models.DateTimeField(auto_now_add=True)
    last_modified_datetime = models.DateTimeField(auto_now=True)

    def get_full_name(self):
        """
        Returns first_name and last_name with the first letter or each name
        capitalized, the rest lower-case, with a space separating each name.
        """
        s = self.first_name[:1].capitalize()
        s += self.first_name[1:].lower()
        s += ' '
        s += self.last_name[:1].capitalize()
        s += self.last_name[1:].lower()
        return s
    get_full_name.short_description = 'Full Name'

    def __unicode__(self):
        return self.get_full_name()

class Employer(models.Model):

    MAX_NAME_LEN  = 124
    MAX_ADDR_LEN  = 124
    MAX_CITY_LEN  = 32
    MAX_STATE_LEN = 16
    MAX_ZIP_LEN   = 16
    
    resume        = models.ForeignKey(Resume)
    name          = models.CharField(max_length=MAX_NAME_LEN)
    address_line1 = models.CharField(max_length=MAX_ADDR_LEN)
    address_line2 = models.CharField(max_length=MAX_ADDR_LEN, blank=True)
    city          = models.CharField(max_length=MAX_CITY_LEN)
    state         = models.CharField(max_length=MAX_STATE_LEN)
    zip_code      = models.CharField(max_length=MAX_ZIP_LEN, blank=True)
    
    def __unicode__(self):
        return self.name

class Position(models.Model):

    MAX_TITLE_LEN = 124

    employer = models.ForeignKey(Employer)
    title = models.CharField(max_length=MAX_TITLE_LEN)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.title

class Education(models.Model):
    """
    Model class for education field of resume. `max_length` for CharFields
    is set using constanct from Resume class.
    """
    resume = models.ForeignKey(Resume, blank=True, null=True)
    name = models.CharField(max_length=Resume.MAX_NAME_LEN)
    degree = models.CharField(max_length=Resume.MAX_NAME_LEN)
    city = models.CharField(max_length=Resume.MAX_CITY_LEN)
    state = models.CharField(max_length=Resume.MAX_STATE_LEN)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

