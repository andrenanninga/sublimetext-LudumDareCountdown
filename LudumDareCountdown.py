import sublime, sublime_plugin
from datetime import datetime

LUDUMDARECOUNTDOWN_SETTINGS_FILE = 'LudumDareCountdown.sublime-settings'
LUDUMDARECOUNTDOWN_INTERVAL_KEY = 'LudumDareCountdown_interval'
LUDUMDARECOUNTDOWN_CATEGORY_KEY = 'LudumDareCountdown_category'
LUDUMDARECOUNTDOWN_ONLYDEADLINECOUNTDOWN_KEY = 'LudumDareCountdown_showOnlyDeadlineCountdown'
DEFAULT_FORMAT = '%H:%M:%S'

LUDUM_START = datetime(2015, 4, 17, 2, 0, 0)
COMPO_END   = datetime(2015, 4, 19, 2, 0, 0)
JAM_END     = datetime(2015, 4, 20, 2, 0, 0)

class StatusBarLudumDareCountdown(sublime_plugin.EventListener):
	def on_activated(self, view):
		settings = sublime.load_settings(LUDUMDARECOUNTDOWN_SETTINGS_FILE)

		update_interval = settings.get(LUDUMDARECOUNTDOWN_INTERVAL_KEY, 1000)
		category = settings.get(LUDUMDARECOUNTDOWN_CATEGORY_KEY, 'compo')
		only_deadline_countdown = settings.get(LUDUMDARECOUNTDOWN_ONLYDEADLINECOUNTDOWN_KEY, False)

		Countdown(DEFAULT_FORMAT).display_time(view, update_interval, category, only_deadline_countdown)

class Countdown():
	status_key = 'ludumDareCountdown'

	def __init__(self, format = DEFAULT_FORMAT):
		self._format = format

	def convert_timedelta(self, duration):
		days, seconds = duration.days, duration.seconds
		hours = seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = seconds % 60

		return days, hours, minutes, seconds

	def display_time(self, view, update_interval, category, only_deadline_countdown):
		now = datetime.utcnow()
		out = ''

		if (LUDUM_START - now).total_seconds() < 0:
			if category == 'compo':
				countdown = COMPO_END - now
			elif category == 'jam':
				countdown = JAM_END - now
		else:
			if only_deadline_countdown == False:
				countdown = LUDUM_START - now

		if(countdown.total_seconds() > 0):
			days, hours, minutes, seconds = self.convert_timedelta(countdown)
			if days: out += str("%s days - " % (days))
			if hours: out += str("%02d:%02d:%02d" % (hours, minutes, seconds))
			elif minutes: out += str("00:%02d:%02d" % (minutes, seconds))
			elif seconds: out += str("00:00:%02d" % (seconds))

			view.set_status(self.status_key, out)

			sublime.set_timeout(lambda: self.display_time(view, update_interval, category, only_deadline_countdown), update_interval)

