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

        self.afl_content['ah_by_ax'] = afl_none['ah_by_ax']
        self.afl_button['ah_by_ax'] = afl_none['ah_by_ax']
        self.afl_content['ah_by_chernow'] = afl_none['ah_by_chernow']
        self.afl_button['ah_by_chernow'] = afl_none['ah_by_chernow']

        self.afl_content['ah_by_chernow'] = afl_none['ah_by_chernow']
        self.afl_button['ah_by_chernow'] = afl_none['ah_by_chernow']

        self.afl_content['big_sleep'] = afl_none['big_sleep']
        self.afl_button['big_sleep'] = afl_none['big_sleep']

        self.afl_content['chinatown'] = afl_none['chinatown']
        self.afl_button['chinatown'] = afl_none['chinatown']

        self.afl_content['fawlty_towers'] = afl_none['fawlty_towers']
        self.afl_button['fawlty_towers'] = afl_none['fawlty_towers']

        self.afl_content['fn_encyclopedia'] = afl_none['fn_encyclopedia']
        self.afl_button['fn_encyclopedia'] = afl_none['fn_encyclopedia']

        self.afl_content['gw_chernow'] = afl_none['gw_chernow']
        self.afl_button['gw_chernow'] = afl_none['gw_chernow']

        self.afl_content['ja_by_ax'] = afl_none['ja_by_ax']
        self.afl_button['ja_by_ax'] = afl_none['ja_by_ax']
        self.afl_content['ja_by_hbo'] = afl_none['ja_by_hbo']
        self.afl_button['ja_by_hbo'] = afl_none['ja_by_hbo']
        self.afl_content['ja_by_mccullough'] = afl_none['ja_chernow']
        self.afl_button['ja_by_mccullough'] = afl_none['ja_by_mccullough']

        self.afl_content['kiss_me_deadly'] = afl_none['kiss_me_deadly']
        self.afl_button['kiss_me_deadly'] = afl_none['kiss_me_deadly']

        self.afl_content['maltese_falcon'] = afl_none['maltese_falcon']
        self.afl_button['maltese_falcon'] = afl_none['maltese_falcon']

        self.afl_content['ph_by_kukla'] = afl_none['ph_by_kukla']
        self.afl_button['ph_by_kukla'] = afl_none['ph_by_kukla']

        self.afl_content['star_trek_tos'] = afl_none['star_trek_tos']
        self.afl_button['star_trek_tos'] = afl_none['star_trek_tos']

        self.afl_content['star_wars_psych'] = afl_none['star_wars_psych']
        self.afl_button['star_wars_psych'] = afl_none['star_wars_psych']

        self.afl_content['tj_by_burns'] = afl_none['tj_by_burns']
        self.afl_button['tj_by_burns'] = afl_none['tj_by_burns']
        self.afl_content['tj_himself'] = afl_none['tj_himself']
        self.afl_button['tj_himself'] = afl_none['tj_himself']

        self.afl_content['white_heat'] = afl_none['white_heat']
        self.afl_button['white_heat'] = afl_none['white_heat']

        self.afl_content['x_files'] = afl_none['x_files']
        self.afl_button['x_files'] = afl_none['x_files']

        self.afl_content['xxx'] = afl_none['xxx']
        self.afl_button['xxx'] = afl_none['xxx']
