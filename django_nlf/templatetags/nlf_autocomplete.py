from random import choice
from string import ascii_letters

from django import template
from django.urls import reverse

from django_nlf.schema.urls import SCHEMA_URL_NAME


register = template.Library()


@register.inclusion_tag("django_nlf/nlf_autocomplete.html")
def nlf_autocomplete(
    app_label,
    model,
    include_js=True,
    input_type="search",
    input_id=None,
    placeholder="",
    renderer_options=None,
    suggestion_options=None,
    debounce=None,
):
    renderer_options = {} if renderer_options is None else renderer_options
    suggestion_options = {} if suggestion_options is None else suggestion_options
    if input_id is None:
        input_id = "".join(choice(ascii_letters) for _ in range(6))

    schema_url = reverse(SCHEMA_URL_NAME, kwargs={"app": app_label, "model": model})
    suggestion_options.update(schemaUrl=schema_url)
    js_options = {"rendererOptions": renderer_options, "suggestionOptions": suggestion_options}

    if debounce is not None:
        js_options.update(debounce=debounce)

    return {
        "include_js": include_js,
        "is_textarea": input_type == "textarea",
        "input_type": input_type,
        "placeholder": placeholder,
        "input_id": input_id,
        "js_options": js_options,
    }
