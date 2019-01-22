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
        'star_trek_tos': '',
        'fawlty_towers': '',
        'tj_himself': '',
        'tj_by_burns': '',
        'x_files': '',
        'ah_chernow': '',
        'ah_ax_video': '',
        'twin_peaks': '',
        'wild_at_heart': '',
        'wild_heart_book': '',
        'weirdsville_usa': '',
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
        """

        self.afl_content['star_trek_tos'] = afl_none['star_trek_tos']
        self.afl_button['star_trek_tos'] = afl_none['star_trek_tos']

        self.afl_content['fawlty_towers'] = afl_none['fawlty_towers']
        self.afl_button['fawlty_towers'] = afl_none['fawlty_towers']

        self.afl_content['tj_himself'] = afl_none['tj_himself']
        self.afl_button['tj_himself'] = afl_none['tj_himself']
        self.afl_content['tj_by_burns'] = afl_none['tj_by_burns']
        self.afl_button['tj_by_burns'] = afl_none['tj_by_burns']

        self.afl_content['x_files'] = afl_none['x_files']
        self.afl_button['x_files'] = afl_none['x_files']

        self.afl_content['ah_chernow'] = afl_none['ah_chernow']
        self.afl_button['ah_chernow'] = afl_none['ah_chernow']
        self.afl_content['ah_ax_video'] = afl_none['ah_ax_video']
        self.afl_button['ah_ax_video'] = afl_none['ah_ax_video']

        self.afl_content['twin_peaks'] = afl_none['twin_peaks']
        self.afl_button['twin_peaks'] = afl_none['twin_peaks']
        self.afl_content['wild_at_heart'] = afl_none['wild_at_heart']
        self.afl_button['wild_at_heart'] = afl_none['wild_at_heart']
        self.afl_content['wild_heart_book'] = afl_none['wild_heart_book']
        self.afl_button['wild_heart_book'] = afl_none['wild_heart_book']
        self.afl_content['weirdsville_usa'] = afl_none['weirdsville_usa']
        self.afl_button['weirdsville_usa'] = afl_none['weirdsville_usa']

        self.afl_content['xxx'] = afl_none['xxx']
        self.afl_button['xxx'] = afl_none['xxx']
