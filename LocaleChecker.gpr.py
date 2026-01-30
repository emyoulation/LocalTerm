from gramps.gui import plug
from gramps.version import major_version, VERSION_TUPLE

if VERSION_TUPLE < (5, 2, 0):
    additional_args = {
        "status": STABLE,
    }
else:
    additional_args = {
        "audience": DEVELOPER,
        "status": STABLE,
        # "maintainers": "",
        # "maintainers_email": "",
    }

register(GRAMPLET,
    id="Locale Checker Gramplet",
    name=_("Locale Checker"),
    description=_("Dashboard with the current Locale and installed languages"),
    version = '1.0.0',
    gramps_target_version=major_version,
    authors=["Brian McCullough"],
    authors_email=["emyoulation@yahoo.com"],
    fname="LocaleChecker.py",
    height=300,
    gramplet='LocaleChecker',
    gramplet_title=_("Locale Checker"),
    # help_url="Addon:Locale_Checker_Gramplet",
    help_url="https://github.com/emyoulation/LocalTerm",
    navtypes=["Dashboard"],
    include_in_listing=True,
    **additional_args,
    )
