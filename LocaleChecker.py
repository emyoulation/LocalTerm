# LocaleChecker.py - CLEAN FINAL VERSION
from gramps.gen.plug import Gramplet
from gramps.gen.utils.grampslocale import GrampsLocale
from gramps.gen.const import GRAMPS_LOCALE as glocale
import os

try:
    _trans = glocale.get_addon_translator(__file__)
except ValueError:
    _trans = glocale.translation
_ = _trans.gettext

class LocaleChecker(Gramplet):
    def init(self):
        self.set_use_markup(True)
        self.has_run = False

    def main(self):
        if self.has_run:
            return
        self.has_run = True

        gl = GrampsLocale()

        # Reverse language dict for code -> name lookup
        language_dict = gl.get_language_dict()
        code_to_name = {v: k for k, v in language_dict.items()}

        # Current locale - FIXED property call
        self.render_text("\n<b>Current Locale</b>\n")
        self.render_text("Locale Code: %s\n" % gl.locale_code())
        self.render_text("Language: %s\n" % str(gl.language))
        self.render_text("Lang: %s\n" % gl.lang)
        self.render_text("Country: %s\n" % getattr(gl, 'country', 'N/A'))

        current_lang_base = gl.lang.split('_')[0] if '_' in gl.lang else gl.lang
        english_name = code_to_name.get(current_lang_base, 'Unknown')
        self.render_text("English Name: %s (%s)\n\n" % (english_name, current_lang_base))

        # Localedir + languages
        localedir = getattr(gl, 'localedir', None)
        if localedir:
            self.render_text("Locale Directory: %s\n\n" % localedir)

            if os.path.isdir(localedir):
                langs = [d for d in os.listdir(localedir)
                        if os.path.isdir(os.path.join(localedir, d))]

                self.render_text("\n<b>Additional Installed Languages (%d)</b>\n" % len(langs))

                # Clean plain text for language list (no superfluous bold)
                for lang in sorted(langs):
                    if lang not in ['.', '..']:
                        english_name = code_to_name.get(lang, 'Unknown')
                        self.append_text("  %s: %s\n" % (lang, english_name))
