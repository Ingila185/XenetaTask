from django.db import migrations

SQL = """
CREATE OR REPLACE FUNCTION get_average_prices()
RETURNS TABLE (price Integer, day date)
LANGUAGE sql
AS $function$

    SELECT price, day
    FROM public.prices;
$function$;
"""

class Migration(migrations.Migration):
    
    dependencies = [
        ('RateListAPI', '0001_initial'),
    ]

    operations = [migrations.RunSQL(SQL)]