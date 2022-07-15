from django_components import component


@component.register("calendar")
class Calendar(component.Component):
    """
    Note that Django will look for templates inside `[your app]/components` dir
    To customize which template to use based on context override get_template_name instead
    """
    template_name = "calendar/calendar.html"


    def get_context_data(self, date):
        """
        This component takes one parameter, a date string to show in the template
        """
        return {
            "date": date,
        }

    class Media:
        """
        Media class is used to define the css and js files that will be used in the template
        """
        css = 'hypercomponents/templates/components/calendar/calendar.css'
        js = 'hypercomponents/templates/components/calendar/calendar.js'

@component.register("calendar_slots")
class CalendarSlots(component.Component):
    """
    Note that Django will look for templates inside `[your app]/components` dir
    To customize which template to use based on context override get_template_name instead
    """
    template_name = "calendar_slots/calendar.html"


    def get_context_data(self, date):
        """
        This component takes one parameter, a date string to show in the template
        """
        return {
            "date": date,
        }

    class Media:
        """
        Media class is used to define the css and js files that will be used in the template
        """
        css = 'hypercomponents/templates/components/calendar_slots/calendar.css'
        js = 'hypercomponents/templates/components/calendar_slots/calendar.js'
