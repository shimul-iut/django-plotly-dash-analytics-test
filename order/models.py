from django.db import models


class Order (models.Model):
    smbdOrderID = models.CharField(max_length=10)
    smbdOrderDate = models.DateField()
    smbdOrderTotalBeforeCoupons = models.IntegerField()
    smbdOrderShipping = models.IntegerField()
    smbdOrderFees = models.DecimalField(max_digits=20, decimal_places=2)
    smbdOrderDiscounts = models.DecimalField(max_digits=20, decimal_places=2)
    smbdOrderCouponNames = models.CharField(max_length=100)
    smbdOrderAfterCoupons = models.IntegerField()
    smbdOrderProductCost = models.DecimalField(max_digits=20, decimal_places=2)
    smbdOrderShippingVendor = models.CharField(max_length=30)
    smbdOrderPaymentMethod = models.CharField(max_length=30)
    smbdOrderShippingVendorPayable = models.DecimalField(max_digits=20, decimal_places=2)
    smbdOrderDateCompleted = models.DateField()

    def __str__(self):
        return self.smbdOrderID






