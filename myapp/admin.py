from django.contrib import admin
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



# Register your models here.
admin.site.register(blog)

admin.site.register(sales_pg)
admin.site.register(aff_mkt_pg)
admin.site.register(human_psy)

admin.site.register(sp1)
admin.site.register(sp2)
admin.site.register(sp3)
admin.site.register(amp1 ) 
admin.site.register(amp2)
admin.site.register(amp3) 
admin.site.register(hmp1)
admin.site.register(hmp2)
admin.site.register(hmp3)




