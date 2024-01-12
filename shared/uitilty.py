from django.core.validators import RegexValidator
phone_regex = RegexValidator(
    regex=r'^\+998([- ])?(90|91|93|94|95|98|99|33|97|71|88|97)([- ])?(\d{3})([- ])?(\d{2})([- ])?(\d{2})$',
    message="Phone number must be True"
                            )




