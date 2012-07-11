# Incuna Profiles

Some Incuna-specific extensions to [Django extensible profiles](http://github.com/incuna/django-extensible-profiles/). Probably of little use to anyone else, but may serve as good examples of how we've used the extensible profile system.

## Installation
Install the package with your favourite package manager:

    pip install incunaprofiles

Add `incunaprofiles` to your `INSTALLED_APPS`:

    ...
    'incunaprofiles',
    ...


## Extensions
Two currently exist:
* hcp
* opportunities


In a `models.py` (usually the project one) add:

    Profile.register_extensions(
        'incunaprofiles.modules.hcp.extensions.hcp',
        'incunaprofiles.modules.opportunities.extension'
    )

Make sure you add the relevant models to your `INSTALLED_APPS` *after* `incunaprofiles`:

    ...
    'incunaprofiles.modules.hcp',
    'incunaprofiles.modules.opportunities',
    ...
