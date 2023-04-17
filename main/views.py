from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.views.generic import View
from django.db.models import Sum
from .models import Entry
from .forms import UploadFileForm
import pandas as pd
import io
import logging
logger = logging.getLogger(__name__)

class ParserView(View):
    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.FILES['file']
            self.handle_uploaded_data(data)
        return redirect('/')

    def get(self, request):
        template = loader.get_template('main/index.html')
        entry_list = Entry.objects.all()
        total_data = Entry.objects.values('date')\
            .annotate(qliq_factual_1_total=Sum('qliq_factual_1'),\
                qliq_factual_2_total=Sum('qliq_factual_2'),\
                qoil_factual_1_total=Sum('qoil_factual_1'),\
                qoil_factual_2_total=Sum('qoil_factual_1'),
                qliq_forecast_1_total=Sum('qliq_forecast_1'),\
                qliq_forecast_2_total=Sum('qliq_forecast_2'),\
                qoil_forecast_1_total=Sum('qoil_forecast_1'),\
                qoil_forecast_2_total=Sum('qoil_forecast_2'))
        form = UploadFileForm()
        context = {
            'entry_list': entry_list,
            'total_data': total_data,
            'form': form
        }
        return HttpResponse(template.render(context, request))

    def handle_uploaded_data(self, data):
        buf = io.BytesIO()
        for chunk in data.chunks(): buf.write(chunk)
        workbook = pd.read_excel(buf,\
            names = ['company', 'qliq_factual_1', 'qliq_factual_2',\
                     'qoil_factual_1', 'qoil_factual_2', 'qliq_forecast_1',\
                     'qliq_forecast_2', 'qoil_forecast_1', 'qoil_forecast_2'],\
            skiprows = 2)
        model_instances = [Entry(**record) for idx, record in workbook.iterrows()]
        Entry.objects.bulk_create(model_instances)
