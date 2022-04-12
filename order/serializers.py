from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['pk', 'smbdOrderID', 'smbdOrderDate', 'smbdOrderTotalBeforeCoupons', 'smbdOrderShipping', 'smbdOrderFees', 'smbdOrderDiscounts', 'smbdOrderCouponNames', 'smbdOrderAfterCoupons', 'smbdOrderProductCost',
                  'smbdOrderShippingVendor', 'smbdOrderPaymentMethod', 'smbdOrderShippingVendorPayable', 'smbdOrderDateCompleted']
