from django.conf import settings
from django.db import migrations

def create_default_channel(apps, schema_editor):
    Channel = apps.get_model("channel", "Channel")
    if not Channel.objects.all().exists() and settings.POPULATE_DEFAULTS:
        Channel.objects.create(
            name="India",  # Or settings.DEFAULT_NAME if you add one
            slug=settings.DEFAULT_CHANNEL_SLUG,  # Use "in" from settings
            currency_code="INR",
            default_country="IN",
            is_active=True,
        )

class Migration(migrations.Migration):
    dependencies = [
        ("channel", "0003_alter_channel_default_country"),
    ]
    operations = [
        migrations.RunPython(create_default_channel, migrations.RunPython.noop)
    ]
