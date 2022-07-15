from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r"^django_components/demo_calendar/$", views.demo_calendar, name="demo_calendar"),
    re_path(r"^django_components/demo_calendar_slots/$", views.demo_calendar_slots, name="demo_calendar_slots"),
    re_path(r"^django_components/demo_calendar_slots_with_super/$", views.demo_calendar_slots_with_super, name="demo_calendar_slots_with_super"),
    re_path(r"^tagify/demo_00_basic/$", views.tagify_demo_00_basic, name="tagify_demo_00_basic"),
    # re_path(r"^v32_vqp/example_handsontable", views.v32_vqp_example_handsontable, name="v32_vqp_example_handsontable"),
    # re_path(r"^v32_vqp/product_packages/create/$", views.product_package_create_get, name="product_packages-create"),
    # re_path(r"^v32_vqp/product_packages/(?P<pk>\d+)/delete/$", views.product_package_delete, name="product_packages-delete"),
    # re_path(r"^v32_vqp/product_packages/(?P<pk>\d+)/$", views.product_package_pk, name="product_packages-pk"),
    # re_path(r"^v32_vqp/product_packages/$", views.product_packages, name="product_packages"),
    # re_path(r"^convert/(?P<pk>\d+)", views.convert, name="convert"),
    # re_path(r"^v32_vqp/is_this_vendor_ok_to_convert/$", views.is_this_vendor_ok_to_convert, name="is_this_vendor_ok_to_convert"),
    # re_path(r"^v32_vqp/vendors_by_sub_project/$", views.load_vendors_by_sub_project, name="vendors_by_sub_project"),
    # re_path(r"^v32_cpop/v1_quotations/purchase_orders/mass_email_psp/$", views.green_email_mass_email_psp, name="green_email_mass_email_psp"),
    # re_path(r"^about_to_upload_po_released", views.about_to_upload_po_released, name="about_to_upload_po_released"),
    # re_path(r"^upload_po_released", views.upload_po_released, name="upload_po_released"),
    # re_path(r"^about_to_delete_linkage_document/(?P<pk>\d+)", views.about_to_delete_linkage_document, name="about_to_delete_linkage_document"),
    # re_path(r"^delete_linkage_document/(?P<pk>\d+)", views.delete_linkage_document, name="delete_linkage_document"),
    # re_path(r"^toggle_user/(?P<pk>\d+)", views.toggle_user, name="toggle_user"),
]
