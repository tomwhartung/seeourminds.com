""" Module to manage affiliate marketing links

Purpose: allow managing affiliate marketing links in one place
Author: Tom W. Hartung
Date: Winter, 2019
Copyright: (c) 2019 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:

"""


class AffiliateLinks:

    """
    Use python dictionaries to make it easier to update affiliate links
    """

    #
    # Source Link Dictionaries:
    #
    afl_default = {
        'ah_by_ax': 'https://groja.com/conversion/afl_default',
        'ah_by_chernow': 'https://groja.com/conversion/afl_default',
        'bf_by_isaacson': 'https://groja.com/conversion/afl_default',
        'big_sleep': 'https://groja.com/conversion/afl_default',
        'chinatown': 'https://groja.com/conversion/afl_default',
        'fawlty_towers': 'https://groja.com/conversion/afl_default',
        'fn_encyclopedia': 'https://groja.com/conversion/afl_default',
        'gw_by_chernow': 'https://groja.com/conversion/afl_default',
        'ja_by_ax': 'https://groja.com/conversion/afl_default',
        'ja_by_hbo': 'https://groja.com/conversion/afl_default',
        'ja_by_mccullough': 'https://groja.com/conversion/afl_default',
        'kiss_me_deadly': 'https://groja.com/conversion/afl_default',
        'maltese_falcon': 'https://groja.com/conversion/afl_default',
        'ph_by_kukla': 'https://groja.com/conversion/afl_default',
        'star_trek_tos': 'https://groja.com/conversion/afl_default',
        'star_wars_psych': 'https://groja.com/conversion/afl_default',
        'tj_himself': 'https://groja.com/conversion/afl_default',
        'tj_by_burns': 'https://groja.com/conversion/afl_default',
        'white_heat': 'https://groja.com/conversion/afl_default',
        'x_files': 'https://groja.com/conversion/afl_default',
        'xxx': 'https://groja.com/conversion/afl_default',
    }

    afl_none = {
        'ah_by_ax': '',
        'ah_by_chernow': '',
        'bf_by_isaacson': '',
        'big_sleep': '',
        'chinatown': '',
        'fawlty_towers': '',
        'fn_encyclopedia': '',
        'gw_by_chernow': '',
        'ja_by_ax': '',
        'ja_by_hbo': '',
        'ja_by_mccullough': '',
        'kiss_me_deadly': '',
        'maltese_falcon': '',
        'ph_by_kukla': '',
        'star_trek_tos': '',
        'star_wars_psych': '',
        'tj_by_burns': '',
        'tj_himself': '',
        'white_heat': '',
        'x_files': '',
        'xxx': '',
    }

    #
    # Active Link Dictionaries:
    #
    afl_content = {}
    afl_button = {}

    def __init__(self):

        """
        Assign source links to active links
        Use expressions like this to reference the values in templates
            {{ afl_content.xxx }}
            {{ afl_button.xxx }}
        """

        self.afl_content['ah_by_ax'] = self.afl_default['ah_by_ax']
        self.afl_button['ah_by_ax'] = self.afl_default['ah_by_ax']
        self.afl_content['ah_by_chernow'] = self.afl_default['ah_by_chernow']
        self.afl_button['ah_by_chernow'] = self.afl_default['ah_by_chernow']

        self.afl_content['bf_by_isaacson'] = self.afl_default['bf_by_isaacson']
        self.afl_button['bf_by_isaacson'] = self.afl_default['bf_by_isaacson']

        self.afl_content['big_sleep'] = self.afl_default['big_sleep']
        self.afl_button['big_sleep'] = self.afl_default['big_sleep']

        self.afl_content['chinatown'] = self.afl_default['chinatown']
        self.afl_button['chinatown'] = self.afl_default['chinatown']

        self.afl_content['fawlty_towers'] = self.afl_default['fawlty_towers']
        self.afl_button['fawlty_towers'] = self.afl_default['fawlty_towers']

        self.afl_content['fn_encyclopedia'] = self.afl_default['fn_encyclopedia']
        self.afl_button['fn_encyclopedia'] = self.afl_default['fn_encyclopedia']

        self.afl_content['gw_by_chernow'] = self.afl_default['gw_by_chernow']
        self.afl_button['gw_by_chernow'] = self.afl_default['gw_by_chernow']

        self.afl_content['ja_by_ax'] = self.afl_default['ja_by_ax']
        self.afl_button['ja_by_ax'] = self.afl_default['ja_by_ax']
        self.afl_content['ja_by_hbo'] = self.afl_default['ja_by_hbo']
        self.afl_button['ja_by_hbo'] = self.afl_default['ja_by_hbo']
        self.afl_content['ja_by_mccullough'] = self.afl_default['ja_by_mccullough']
        self.afl_button['ja_by_mccullough'] = self.afl_default['ja_by_mccullough']

        self.afl_content['kiss_me_deadly'] = self.afl_default['kiss_me_deadly']
        self.afl_button['kiss_me_deadly'] = self.afl_default['kiss_me_deadly']

        self.afl_content['maltese_falcon'] = self.afl_default['maltese_falcon']
        self.afl_button['maltese_falcon'] = self.afl_default['maltese_falcon']

        self.afl_content['ph_by_kukla'] = self.afl_default['ph_by_kukla']
        self.afl_button['ph_by_kukla'] = self.afl_default['ph_by_kukla']

        self.afl_content['star_trek_tos'] = self.afl_default['star_trek_tos']
        self.afl_button['star_trek_tos'] = self.afl_default['star_trek_tos']

        self.afl_content['star_wars_psych'] = self.afl_default['star_wars_psych']
        self.afl_button['star_wars_psych'] = self.afl_default['star_wars_psych']

        self.afl_content['tj_by_burns'] = self.afl_default['tj_by_burns']
        self.afl_button['tj_by_burns'] = self.afl_default['tj_by_burns']
        self.afl_content['tj_himself'] = self.afl_default['tj_himself']
        self.afl_button['tj_himself'] = self.afl_default['tj_himself']

        self.afl_content['white_heat'] = self.afl_default['white_heat']
        self.afl_button['white_heat'] = self.afl_default['white_heat']

        self.afl_content['x_files'] = self.afl_default['x_files']
        self.afl_button['x_files'] = self.afl_default['x_files']

        self.afl_content['xxx'] = self.afl_default['xxx']
        self.afl_button['xxx'] = self.afl_default['xxx']
