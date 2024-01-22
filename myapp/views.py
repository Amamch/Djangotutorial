from os import name
from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse


from .models import blog

from .models import sales_pg
from .models import aff_mkt_pg
from .models import human_psy



from .models import sp1
from .models import sp2
from .models import sp3
from .models import amp1  
from .models import amp2
from .models import amp3 
from .models import hmp1
from .models import hmp2
from .models import hmp3





# Create your views here.

def index(request):    
        blogs = blog.objects.all()
        return render(request, 'index.html', {'blogs':blogs})
    
def sale_pg(request):    
        sales_home = sales_pg.objects.all()
        return render(request, 'sales.html', {'sales_home':sales_home})

def aff_mkts_pg(request):    
        aff_mkts_pgs = aff_mkt_pg.objects.all()
        return render(request, 'affmkt.html', {'aff_mkts_pgs':aff_mkts_pgs})
        

def human_psyc(request):    
        human_psych = human_psy.objects.all()
        return render(request, 'human_psy.html', {'human_psych':human_psych})



def sp (request): 
        spaa = sp1.objects.all()
        return render(request, 'sp1.html', {'spaa':spaa})
def spa (request): 
        spab = sp2.objects.all()
        return render(request, 'sp2.html', {'spab':spab})
def spb (request): 
        spac = sp3.objects.all()
        return render(request, 'sp3.html', {'spac':spac})



def amp (request): 
        ampaa = amp1.objects.all()
        return render(request, 'amp-1.html', {'ampaa':ampaa})

def ampa (request): 
        ampab = amp2.objects.all()
        return render(request, 'amp-2.html', {'ampab':ampab})

def ampb (request): 
        ampac = amp3.objects.all()
        return render(request, 'amp-3.html', {'ampac':ampac})




def hmp (request): 
        hmpaa = hmp1.objects.all()
        return render(request, 'hmp-1.html', {'hmpaa':hmpaa})

def hmpa (request): 
        hmpab = hmp2.objects.all()
        return render(request, 'hmp-2.html', {'hmpab':hmpab})

def hmpb (request): 
        hmpac = hmp3.objects.all()
        return render(request, 'hmp-3.html', {'hmpac':hmpac})








    


