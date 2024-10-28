from django.db import models


# Create your models here.
class Recruiter(models.Model):
    cname = models.CharField(max_length=80)
    fname = models.CharField(max_length=80)
    email = models.EmailField()
    phno = models.PositiveBigIntegerField()
    psw = models.CharField(max_length=15)
    webs = models.CharField(max_length=100)
    lp = models.CharField(max_length=100)
    loc = models.CharField(max_length=50)
    au = models.CharField(max_length=200)
    ind = models.CharField(max_length=50)
    wwo = models.CharField(max_length=200)

class Seeker(models.Model):
    fname = models.CharField(max_length=80)
    pic = models.ImageField(upload_to='passphotos/', blank=True, null=True)
    email = models.EmailField()
    psw = models.CharField(max_length=15)
    phno = models.PositiveBigIntegerField()
    gen = models.CharField(max_length=10)
    dob = models.DateField()
    add = models.CharField(max_length=200)
    hq = models.CharField(max_length=100)
    un = models.CharField(max_length=200)
    sd = models.DateField()
    ed = models.DateField()
    we = models.IntegerField()
    pc = models.CharField(max_length=200)
    pjt = models.CharField(max_length=50)
    pjl = models.CharField(max_length=100)
    atw = models.DateField()
    ks = models.CharField(max_length=500)
    lk = models.CharField(max_length=200)
    intern = models.CharField(max_length=500)
    proj = models.CharField(max_length=5000)
    certi = models.CharField(max_length=1000)
    ps = models.CharField(max_length=500)
    resume = models.FileField(upload_to='pdfs/')

class HiringSeekers(models.Model):
    jt = models.CharField(max_length=300)
    cn = models.CharField(max_length=200)
    jl = models.CharField(max_length=150)
    cl = models.ImageField(upload_to='logos/', blank=True, null=True)
    jtyp = models.CharField(max_length=100)
    er = models.CharField(max_length=500)
    kysk = models.CharField(max_length=1000)
    exp = models.PositiveIntegerField()
    abtcomp = models.CharField(max_length=2000)
    pos = models.PositiveIntegerField()
    jd = models.CharField(max_length=5000)
    jr = models.CharField(max_length=4000)
    sal = models.CharField(max_length=150)
    al = models.CharField(max_length=300)
    ld = models.DateField(default='2025-01-01')
    
class RemovedPost(models.Model):
    jt = models.CharField(max_length=300)
    cn = models.CharField(max_length=200)
    jl = models.CharField(max_length=150)
    cl = models.ImageField(upload_to='logos/', blank=True, null=True)
    jtyp = models.CharField(max_length=100)
    er = models.CharField(max_length=500)
    kysk = models.CharField(max_length=1000)
    exp = models.PositiveIntegerField()
    abtcomp = models.CharField(max_length=2000)
    pos = models.PositiveIntegerField()
    jd = models.CharField(max_length=5000)
    jr = models.CharField(max_length=4000)
    sal = models.CharField(max_length=150)
    al = models.CharField(max_length=300)
    ld = models.DateField(default='2025-01-01')

class ApplicantDetails(models.Model):
    fname = models.CharField(max_length=80)
    pic = models.ImageField(upload_to='passphotos/', blank=True, null=True)
    email = models.EmailField()
    phno = models.PositiveBigIntegerField()
    gen = models.CharField(max_length=10)
    dob = models.DateField()
    add = models.CharField(max_length=200)
    hq = models.CharField(max_length=100)
    un = models.CharField(max_length=200)
    sd = models.DateField()
    ed = models.DateField()
    we = models.IntegerField()
    pc = models.CharField(max_length=200)
    pjt = models.CharField(max_length=50)
    pjl = models.CharField(max_length=100)
    atw = models.DateField()
    ks = models.CharField(max_length=500)
    lk = models.CharField(max_length=200)
    intern = models.CharField(max_length=500)
    proj = models.CharField(max_length=5000)
    certi = models.CharField(max_length=1000)
    ps = models.CharField(max_length=500)
    resume = models.FileField(upload_to='pdfs/')
    
    jt = models.CharField(max_length=300)
    cn = models.CharField(max_length=200)
    jl = models.CharField(max_length=150, null=True)
    cl = models.ImageField(upload_to='logos/', blank=True, null=True)
    jtyp = models.CharField(max_length=100, null=True)
    er = models.CharField(max_length=500, null=True)
    kysk = models.CharField(max_length=1000, null=True)
    exp = models.PositiveIntegerField(null=True)
    abtcomp = models.CharField(max_length=2000, null=True)
    pos = models.PositiveIntegerField(null=True)
    jd = models.CharField(max_length=5000, null=True)
    jr = models.CharField(max_length=4000, null=True)
    sal = models.CharField(max_length=150, null=True)
    al = models.CharField(max_length=300, null=True)
    ld = models.DateField(default='2025-01-01')
    ad = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Under_Review', 'Under_Review'),
        ('Shortlisted', 'Shortlisted'),
        ('Hired', 'Hired'),
    ]
    status = models.CharField(max_length=20, default='Applied', choices=STATUS_CHOICES)
    progress_percentage = models.IntegerField(default=0)

    def update_progress(self):
        status_to_percentage = {
            'Applied': 10,
            'Under_Review': 40,
            'Shortlisted': 70,
            'Hired': 100
        }
        self.progress_percentage = status_to_percentage.get(self.status, 0)
        self.save()