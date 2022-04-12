from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
from order.models import Order
import csv


# from django.http import HttpResponse


# Create your views here.

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            col_names = next(reader)  # Get the column names from CSV
            for i, row in enumerate(reader):
                if col_names[0] == 'Final_Fee':  # Pathao CSV
                    if i == 0:
                        pass
                    else:
                        Order.objects.filter(smbdOrderID=row[1]).update(smbdOrderShippingVendorPayable=row[0])
                else:
                    if i == 0:
                        pass
                    else:  # print(row)
                        Order.objects.create(
                            smbdOrderID=row[0],
                            smbdOrderDate=row[1],
                            smbdOrderTotalBeforeCoupons=int(row[2]),
                            smbdOrderShipping=int(row[6]),
                            smbdOrderFees=float(row[5]),
                            smbdOrderDiscounts=float(row[3]),
                            smbdOrderCouponNames=row[4],
                            smbdOrderAfterCoupons=int(row[7]),
                            smbdOrderProductCost=float(row[8]),
                            smbdOrderShippingVendor=row[10],
                            smbdOrderPaymentMethod=row[9],
                            smbdOrderShippingVendorPayable='0.0',
                            smbdOrderDateCompleted=row[11]
                        )
                        obj.activated = True
                        obj.save()
    return render(request, 'csvs/upload.html', {'form': form})
