from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Diagonal': 'diagonal',
        'Display Type': 'display_type',
        'Processor Freq': 'processor_freq',
        'Ram': 'ram',
        'Video': 'video',
        'Time Without Charge': 'time_without_charge'
    },
    'smartphone': {
        'Diafonal': 'diagonal',
        'Display Type': 'display_type',
        'Resolution': 'resolution',
        'Accum Volume': 'accum_volume',
        'Ram': 'ram',
        'SD': 'sd',
        'SD Volume Max': 'sd_volume_max',
        'Cam (MP)': 'main_cam_mp',
        'Frontal Cam (MP)': 'frontal_cam_mp'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('SD Volume Max', None)
        else:
            PRODUCT_SPEC['smartphone']['SD Volume Max'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

